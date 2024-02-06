from .lib.module import Module 
from .lib.util import send 
from .lib.cmd import Cmd
import requests as req
import urllib.parse
import logging

def get(url) -> dict:
    try:
        res = req.get(url)
        if res.status_code != 200:
            return {}
        return res.json()
    except:
        return {}

def tohuman(num) -> str:
    if abs(num) > (1024*1024):
        num /= 1024.0
        num /= 1024.0
        return "%3.1f MiB/s" % (num,)

    num /= 1024.0
    return "%3.1f KiB/s" % (num,)

class TOR(Module):
    def __init__(self):
        super().__init__("tor", 
            [Sum(), Top(), Search()], 
            desc="Check TOR network status")

class Search(Cmd):
    def __init__(self):
        super().__init__("tor-search", 1, "Search for a TOR relay")

    def cmd(self, args, c) -> bool:
        data = get(f"https://onionoo.torproject.org/details?limit=1&search={urllib.parse.quote_plus(args[0].lower())}")
        if len(data.keys()) == 0:
            send(c, "Failed to fetch onionooo!")
            logging.error("Failed to fetch https://onionoo.torproject.org/details")
            return False

        if len(data["relays"]) == 0:
            send(c, "Relay not found")
            return True

        relay = data["relays"][0]
        send(c, 
f"""*🪪 Nickname*: {relay['nickname']}
*🔑 Fingerprint*: {relay['fingerprint']}
*🚀 Running*: {"yes" if relay['running'] else "no"}
*📈 Bandwidth*: {tohuman(relay['advertised_bandwidth'])}
*🏴 Country*: {relay['country_name']}
*💿 Platform*: {relay['platform']} ({relay['version_status']})
*🔎 Contact*: {relay['contact']}""")
        return True

class Top(Cmd):
    def __init__(self):
        super().__init__("tor-top", 1, "Search for top TOR relays for a country")

    def cmd(self, args, c) -> bool:
        if len(args[0]) != 2:
            send(c, "Bad country code!")
            return True

        data = get(f"https://onionoo.torproject.org/details?limit=15&country={args[0].lower()}&order=-consensus_weight")
        if len(data.keys()) == 0:
            send(c, "Failed to fetch onionooo!")
            logging.error("Failed to fetch https://onionoo.torproject.org/details")
            return False

        relays = ""
        for r in data["relays"]:
            relays += r["fingerprint"]+": *"+r["nickname"]+" (📈 "+tohuman(r['advertised_bandwidth'])+")*\n"

        if relays == "":
            send(c, f"Got no relays in located at {args[0].lower()}")
            return True

        send(c, 
f"""🧅 Top 15 Relays ({args[0].lower()}) 
===================
{relays}""")
        return True

class Sum(Cmd):
    def __init__(self):
        super().__init__("tor-sum", 0, "TOR network summary")

    def cmd(self, _, c) -> bool:
        data = get("https://onionoo.torproject.org/summary")
        if len(data.keys()) == 0:
            send(c, "Failed to fetch onionooo!")
            logging.error("Failed to fetch https://onionoo.torproject.org/summary")
            return False

        relays_date = data["relays_published"]
        bridges_date = data["bridges_published"]

        relays = data["relays"]
        bridges = data["bridges"]

        rcount = 0
        bcount = 0

        for r in relays:
            if "f" in r.keys() and r["r"]:
                rcount += 1

        for b in bridges:
            if "h" in b.keys():
                bcount += 1

        send(c, f"""*📊 Relays Published*: {relays_date} UTC
*📅 Total Relays*: {rcount}

*📊 Bridges Published*: {bridges_date} UTC
*📅 Total Bridges*: {bcount}""")
        return True
