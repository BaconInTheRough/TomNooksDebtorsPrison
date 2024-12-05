#!/bin/bash

ln -sf $HOME/TomNooksDebtorsPrison/sys/celeste-bot.service /etc/systemd/system/celeste-bot.service

systemctl daemon-reload
systemctl enable celeste-bot.service