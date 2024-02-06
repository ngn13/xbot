# xbot | modular XMPP bot 
Simple, configurable and modular MUC XMPP bot written in python.

## Modules
- General (`general`): Simple commands: `help`, `echo`, `ping` and `info`
- AFK (`afk`): Set and clear AFK status with `afk-set` and `afk-clear`, if you are AFK, bot will warn
other members when they ping you, using the custom message you specified. 
- Redirect (`redirect`): Provides alternative privacy friendly frotend links. When enabled, if a user message contains 
YouTube, Twitter, Reddit, Medium or StackOverflow link, bot will message alternative frontend link for the same link.
- TOR (`tor`): Lets users see the TOR network summary (`tor-sum`), list top relays for countries (`tor-top`) and search 
for relays by fingerprint or name (`tor-search`)
