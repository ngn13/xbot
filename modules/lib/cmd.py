from .util import send

class Cmd:
    def __init__(self, name: str, argc: int, desc: str) -> None:
        self.name = name
        self.argc = argc
        self.desc = desc

    def on_msg(self, msg) -> None:
        return

    def cmd(self, args, c) -> bool:
        return True

    def run(self, args, c) -> bool:
        if self.argc > len(args):
            send(c, f"Specify at least {self.argc} argument to use this command")
            return False
        return self.cmd(args, c)

