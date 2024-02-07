import json
import logging

class Config:
    def __init__(self) -> None:
        self.success = False
        try:
            with open("config.json", "r") as f:
                cfg = json.loads(f.read())
                self.JID = cfg["jid"]
                self.PREFIX = cfg["prefix"]
                self.PASSWORD = cfg["password"]
                self.MODULES = cfg["modules"]
                self.CONTACT = cfg["contact"]
                self.NICK = cfg["nick"]
                self.MUCS = cfg["mucs"]
            self.success = True 
        except Exception as e:
            logging.error(f"Configuration error: {e}")
            pass
