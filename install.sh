#!/bin/bash

# The setup script for SAM

if [ $(id -u) != 0 ]
then
    echo "This program must be runned as root."
    exit
fi

echo "Creating /usr/share/sam/"
mkdir /usr/share/sam

echo "Creating /var/cache/sam/"
mkdir /var/cache/sam

echo "Creating /usr/share/sam/program/"
mkdir /usr/share/sam/program/

echo "Creating /usr/share/sam/packages/"
mkdir /usr/share/sam/packages/

echo "installed.db --> /usr/share/sam/"
cp installed.db /usr/share/sam/

echo "sam.py --> /usr/share/sam/program/"
cp sam.py /usr/share/sam/program/

echo "makepkg.py --> /usr/share/sam/program/"
cp makepkg.py /usr/share/sam/program/

echo "remove.py --> /usr/share/sam/program/"
cp remove.py /usr/share/sam/program/

echo "sam-run.py --> /usr/share/sam/program/"
cp sam-run.py /usr/share/sam/program/

echo "unpkg.py --> /usr/share/sam/program/"
cp unpkg.py /usr/share/sam/program/

echo "utils.py --> /usr/share/sam/program/"
cp utils.py /usr/share/sam/program/

echo "chmod +x /usr/share/sam/program/sam.py"
chmod +x /usr/share/sam/program/sam.py

echo "chmod +x /usr/share/sam/program/sam-run.py"
chmod +x /usr/share/sam/program/sam-run.py

echo "ln -s /usr/share/sam/program/sam.py /usr/bin/sam"
ln -s /usr/share/sam/program/sam.py /usr/bin/sam

echo "ln -s /usr/share/sam/program/sam-run.py /usr/bin/sam-run"
ln -s /usr/share/sam/program/sam-run.py /usr/bin/sam-run