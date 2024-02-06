from .lib.module import Module 
from .lib.util import send 
from .lib.cmd import Cmd

afkstatus = []

class AFK(Module):
    def __init__(self):
        super().__init__("afk", 
            [Set(), Clear(), Notify()], 
            desc="Set/clear AFK status")

class Notify(Cmd):
    def __init__(self):
        super().__init__("", 0, "")

    def on_msg(self, msg) -> None:
        for a in afkstatus:
            if a["nick"] in msg["body"]:
                send(msg, f"⚠️ {msg['from'].resource}, {a['nick']} is AFK: {a['reason']}")

class Set(Cmd):
    def __init__(self):
        super().__init__("afk-set", 0, "Set AFK status")

    def cmd(self, args, c) -> bool:
        reason = "AFK" if len(args)==0 else ""
        for a in args:
            reason += a+" "

        for a in afkstatus:
            if a["nick"] == c['from'].resource:
                a["reason"] = reason
                send(c, f"✅ Updated your AFK status: {reason}")
                return True

        afkstatus.append({
            "nick": c['from'].resource,
            "reason": reason,
        })

        send(c, f"✅ Set your AFK status: {reason}")
        return True

class Clear(Cmd):
    def __init__(self):
        super().__init__("afk-clear", 0, "Clear AFK status")

    def cmd(self, _, c) -> bool:
        for a in afkstatus:
            if a["nick"] == c['from'].resource:
                afkstatus.remove(a)

        send(c, f"✅ Cleared your AFK status")
        return True
