# TomNooksDebtorsPrison

This is a Discord bot-farm for my server: Tom Nook's Debtors Prison

## Installation

### Ubuntu Server

#### Environment setup
I used pyenv to setup my python env

Installed python3.12.8 with all basic apt packages

```
pip3 install discord.py
```

#### Service install

I built this to run as a service on an Ubuntu server using `ubuntu` login

```
cd ~  # this should put you in /home/ubuntu/
git clone https://github.com/BaconInTheRough/TomNooksDebtorsPrison.git
```
You will then need to add you Discord Applications token as an environment variable to the service unit
file in `~/TomNooksDebtorsPrison/sys/celeste-bot.service` under [SERVICE] directives
```
Environment="CELESTE_BOT_TOKEN=<insert your token>"
```

Then run the service install:
```
sudo ~/TomNooksDebtorsPrison/scripts/install.sh
sudo systemctl start celeste-bot.service
```

### Other servers
For other servers that do not run systemd services you only need the /src directory
```
mkdir TomNooksDebtorsPrison && cd TomNooksDebtorsPrison
git init
git remote add origin https://github.com/BaconInTheRough/TomNooksDebtorsPrison.git
git config core.sparseCheckout true
echo "src/" >> .git/info/sparse-checkout
git pull origin main
```

set up a python environment with 3.12.8 and `pip3 install discord.py`

```
$(which python3) ~/TomNooksDebtorsPrison/src/celeste_bot.py
```