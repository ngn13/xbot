from modules.lib.util import parse_cmd, send
from slixmpp.stanza.message import Message
from slixmpp.clientxmpp import ClientXMPP
from modules.lib.config import Config
from modules.lib import consts 
from modules import MODULES
import logging

class xbot(ClientXMPP):
    def __init__(self, cfg: Config):
        ClientXMPP.__init__(self, cfg.JID, cfg.PASSWORD)
        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("groupchat_message", self.muc_message)

        self.register_plugin("xep_0045")
        self.register_plugin("xep_0030")
        self.register_plugin("xep_0199") 

        self.cfg = cfg 
        self.modules = []

        for c in cfg.MODULES:
            found = False
            for m in MODULES:
                if m.name == c:
                    self.modules.append(m)
                    found = True
                    break

            if not found:
                logging.error(f"Module {c} not found, ignoring")

    def session_start(self, _):
        self.send_presence()
        self.get_roster()

        for m in self.cfg.MUCS: 
            logging.info(f"Joining MUC: {m}")
            self.plugin["xep_0045"].join_muc(
                m, self.cfg.NICK)
    
        logging.info(f"{self.cfg.JID} is now online!")

    def muc_message(self, c: Message):
        if c["mucnick"] == self.cfg.JID or self.cfg.JID in c["body"] or self.cfg.NICK in c["mucnick"]:
            return

        for m in self.modules:
            m.on_msg(c)

        if not c["body"].startswith(cfg.PREFIX):
            return
        
        parsed = parse_cmd(c["body"])
        for m in self.modules:
            cmd = m.find(parsed[0]) 
            if cmd == None:
                continue
            if cmd.name == "help" or cmd.name == "info":
                return cmd.run([MODULES], c)
            return cmd.run(parsed[1], c)

        send(c, f"{parsed[0]}: command not found")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
        format='[%(levelname)s] [%(asctime)s] %(message)s')

    cfg = Config()
    if not cfg.success:
        logging.error("Loading configuration failed")
        exit(1)
            
    logging.info(f"Starting xbot v{consts.VERSION}")
    xmpp = xbot(cfg)
    xmpp.connect()
    xmpp.process(forever=True)
