class Module:
    def __init__(self, name: str, cmds: list, desc="") -> None:
        self.name = name
        self.desc = desc
        self.cmds = cmds 

    def on_msg(self, msg):
        for c in self.cmds:
            c.on_msg(msg)

    def find(self, name):
        for c in self.cmds:
            if c.name != "" and c.name == name:
                return c
        return None

