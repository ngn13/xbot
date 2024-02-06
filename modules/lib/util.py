from slixmpp.stanza import Message

def parse_cmd(msg: str):
    msg = msg[1:] 
    l = msg.split(" ")
    if len(l) == 0:
        return ["", []]
    return [l[:1][0], l[1:]]

def send(c: Message, msg):
    c.reply(msg).send()
