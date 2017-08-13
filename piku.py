#!/usr/bin/python
import subprocess
import os
import sys
from lib.subtitle import subtitle
from lib.irc import irc

try:
    channel = str(sys.argv[1]).lower()
    stream_source = "https://twitch.tv/" + channel
except:
    print("Usage: " + sys.argv[0] + " <twitch channel>")
    exit(1)

subfile_location = "pikupiku.ass"
host = "irc.twitch.tv"
port = 6667

################## Change this #########################
nick = "" # twitch nick (lower case?)
oauth = "" # Copy/Paste from https://twitchapps.com/tmi/
########################################################
if not nick or not oauth:
    print("You need to set nick/oauth in piku.py")
    exit(1)

channel = "#" + channel

sub = subtitle(subfile_location)

mpv_cmd = ['mpv', '--no-terminal', '-fs', '--sub-file='+subfile_location, '--script=./lib/mpv-sub-reload.lua', stream_source]
with open(os.devnull, 'w') as f:
    subprocess.Popen(mpv_cmd, stdout=f, stderr=subprocess.STDOUT)

server = irc(host, port, nick, oauth, channel, sub)
server.connect()

