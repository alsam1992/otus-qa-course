#!/bin/sh

sudo apt-get update -y
sudo apt-get install python3-pip -y
sudo python3 -mpip install -r requirements.txt
sudo Xvfb :99 -ac &
sudo python3 -mpytest test_todo_mvc.py