from .lib.module import Module 
from .lib.cmd import Cmd, send

class Redirect(Module):
    def __init__(self):
        super().__init__("redirect", 
            [RedirectMsg()], 
            desc="Redirect links to privacy-friendly frontends")

class RedirectMsg(Cmd):
    def __init__(self):
        super().__init__("", 0, "")

        self.youtube = [
            "https://piped.lunar.icu",
            "https://pd.vern.cc",
            "https://piped.ngn.tf"
        ]

        self.twitter = [
            "https://nitter.1d4.us",
            "https://nt.vern.cc",
            "https://nitter.kavin.rocks",
        ]

        self.reddit = [
            "https://teddit.net",
            "https://teddit.zaggy.nl",
            "https://teddit.ngn.tf",
        ]

        self.medium = [
            "https://libmedium.batsense.net",
            "https://md.vern.cc",
            "https://med.ngn.tf",
        ]
        
        self.stackoverflow = [
            "https://code.whatever.social",
            "https://ao.vern.cc",
            "https://ao.ngn.tf",
        ]

        self.frontends = {
            "https://youtube.com": self.youtube,
            "https://youtu.be": self.youtube,
            "https://twitter.com": self.twitter,
            "https://www.x.com": self.twitter,
            "https://reddit.com": self.reddit,
            "https://medium.com": self.medium,
            "https://stackoverflow.com": self.stackoverflow,
        }

    def on_msg(self, msg) -> None:
        for word in msg["body"].split(" "):
            for key in self.frontends:
                if key in word:
                    res = "("
                    for l in self.frontends[key]:
                        res += f" {word.replace(key, l)} "
                    res += ")"
                    send(msg, res)
