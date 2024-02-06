from .lib.module import Module 
from .lib.config import Config 
from .lib.util import send 
from .lib.cmd import Cmd
from .lib import consts 
import logging

class General(Module):
    def __init__(self):
        super().__init__("general", 
            [Echo(), Ping(), Info(), Help()], 
            desc="General commands")

class Echo(Cmd):
    def __init__(self):
        super().__init__("echo", 1, "Repeat given message")

    def cmd(self, args, c) -> bool:
        con = ""
        for a in args:
            con += f"{a} "

        send(c, con)
        return True

class Ping(Cmd):
    def __init__(self):
        super().__init__("ping", 0, "Simple ping-pong command")

    def cmd(self, _, c) -> bool:
        send(c, "🏓 Pong!")
        return True

class Info(Cmd):
    def __init__(self):
        super().__init__("info", 0, "Get information about the bot")

    def cmd(self, args, c) -> bool:
        cfg = Config()
        if not cfg.success:
            logging.error("Failed to load config!")
            send(c, "Internal error")
            return False

        modules = ""
        for m in args[0]:
            modules += m.name+" "

        send(c, f"""ℹ️ xbot v{consts.VERSION} | github.com/ngn13/xbot 
================================================
🔎 This bot is being hosted by {cfg.CONTACT}, get in contact 
with them if needed. Report any bugs/issues on Github

📥 Modules: {modules}""")
        return True

class Help(Cmd):
    def __init__(self):
        super().__init__("help", 0, "Get information about all the commands")

    def cmd(self, args, c) -> bool:
        helpmsg = "💡 Listing help information for the commands\n"
        longest = 0

        for m in args[0]:
            for cmd in m.cmds:  
                if len(cmd.name) > longest:
                    longest = len(cmd.name)

        longest += 2
        helpmsg += "```\n"
        for m in args[0]:
            for cmd in m.cmds:  
                if cmd.name != "":
                    helpmsg += f"{cmd.name}{(longest-len(cmd.name))*' '}[{cmd.argc}] ➡️ {cmd.desc}\n"
        helpmsg += "```"

        send(c, helpmsg)
        return True
