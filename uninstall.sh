#!/bin/bash

# The uninstall script for SAM

if [ $(id -u) != 0 ]
then
    echo "This program must be runned as root."
    exit
fi

echo "rm /usr/share/sam"
rm -rf /usr/share/sam

echo "rm /var/cache/sam"
rm -rf /var/cache/sam

echo "rm /usr/bin/sam"
rm /usr/bin/sam

echo "rm /usr/bin/sam-run"
rm /usr/bin/sam-run