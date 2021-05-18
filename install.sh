#!/bin/bash

# The setup script for SAM

if [ $(id -u) != 0 ]
then
    echo "This program must be runned as root."
    exit
fi

touch config

echo "Please enter your processor architecture :"
echo "1) x86 : 32-bits intel or AMD processor"
echo "2) x86-64 : 64-bits intel or AMD processor"
echo "3) armv6 : used by the Raspberry Pi 1 and Zero"
echo "4) armv7 : used by the Raspberry Pi 2 and 3"
echo "5) armv8 : used by the Raspberry Pi 4"
echo "6) arm64 : 64-bit ARM architecture"
echo "7) aarch64 : other 64-bit ARM architecture"
echo ""
read -p "Type a number (1-7) : " choice


if [ $choice == "1" ]
then
    echo "Architecture=x86" > config

elif [ $choice == "2" ]
then
    echo "Architecture=x86-64" > config

elif [ $choice == "3" ]
then
    echo "Architecture=armv6" > config
elif [ $choice == "4" ]
then
    echo "Architecture=armv7" > config
elif [ $choice == "5" ]
then
    echo "Architecture=armv8" > config
elif [ $choice == "6" ]
then
    echo "Architecture=arm64" > config
elif [ $choice == "7" ]
then
    echo "Architecture=aarch64" > config
else
    echo "$choice : out of range"
    rm config
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

echo "config --> /usr/share/sam/"
cp config /usr/share/sam/

echo "rm config"
rm config


