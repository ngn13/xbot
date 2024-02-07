# xbot | modular XMPP bot 
Simple, configurable and modular MUC XMPP bot written in python.

### 🗂 Modules
| Name       | Description                                          | Commands 
| ---------- | ---------------------------------------------------- | -------------------------------
| `general`  | Simple commands                                      | `help`, `echo`, `ping`, `info`
| `afk`      | Set & clear AFK status                               | `afk-set`, `afk-clear`
| `redirect` | Provides alternative privacy friendly frontend links | none
| `tor`      | Search for TOR relays, see network status etc.       | `tor-sum`, `tor-top`, `tor-search`

### 🚀 Install
1. Copy over the example configuration and modify it for your needs: [`config.json.example`](config.json.example)
2. Deploy the bot with docker:
```bash
docker run -d --restart=unless-stopped          \
           -v $PWD/config.json:/bot/config.json \
           ghcr.io/ngn13/xbot:latest 
```

### 🛠 Development
Start by cloning the repository and creating a virtual environment:
```bash
git clone https://github.com/ngn13/xbot.git
cd xbot && python3 -m venv venv
source venv/bin/activate.sh
```
When you are in the virtual environment, run the `requirements.sh` script to install all the requirements. 

You can extend the bot and more modules. To load your new module, add it to `modules/__init__.py` and to your configuration.
