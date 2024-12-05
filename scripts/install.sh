#!/bin/bash

ln -sf /home/ubuntu/TomNooksDebtorsPrison/sys/celeste-bot.service /etc/systemd/system/celeste-bot.service

systemctl daemon-reload
systemctl enable celeste-bot.service