# coding=utf-8
import vlc
import sys
import json
import time
import win32gui
import subprocess
import pypresence
import re#eeeeeeeeee
from subprocess import Popen

# from gi.repository import Playerctl, GLib


# Opens config.json
with open('config.json') as config:
    config = json.load(config)

# Extracts variables from json data (config)
CLIENT_ID = config['client_id']
PIPE = config['pipe']
LOOP = config['loop']
HANDLER = config['handler']
UPDATE_RATE = config['update_rate']

COMP_APPS = {
    'vlc': {
        'tag': 'VLC media player',
        'id': 267774,
    },
    'chrome': {
        'tag': 'Google Chrome',
        'id': 5839080,
    },
    'discord': {
        'tag': 'Discord',
        'id': 6227208,
    },
}

y = []
# Prints a '=' for how long the Client ID line is
for _ in range(int(len(str(CLIENT_ID)) + 13)):  # 13 because that's the length of 'Client ID:...'
    y.append("=")

print("".join(y))
# Just to make sure you have the right config selected
print("Client ID:   {}\n"
      "Pipe:        {}\n"
      "Loop:        {}\n"
      "Handler:     {}"
      .format(CLIENT_ID, PIPE, LOOP, HANDLER))

y = []
for _ in range(int(len(str(CLIENT_ID)) + 13)):  # 13 because that's the length of 'Client ID:...'
    y.append("=")
print("".join(y))
print("\n")

# Defining and Connecting
RP = pypresence.Presence(client_id=CLIENT_ID, pipe=PIPE, loop=LOOP, handler=HANDLER)
RP.connect()


# Getting Applications
def get_applications():
    """
    To properly run powershell files in Python, you first need to do a few things.

    1.) You need to allow Powershell files to be opened via Python. You can learn how to do that here:
        https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6

    2.) To properly read the data I would recommend setting the default encoding of Powershell to UTF-8. You can learn
        how to do that here:
        https://stackoverflow.com/questions/40098771/changing-powershells-default-output-encoding-to-utf-8
    """

    process = subprocess.Popen(["powershell.exe",
                                "C:\\Users\\maxla\\PycharmProjects\\discordVLC\\getprocess.ps1"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out = process.stdout.read().decode(encoding='UTF-8').rstrip()  # Decoding
    while "  " in str(out):  # Removing all the spaces PS uses
        out = str(out).replace("  ", " ")
    while "\r" in str(out):  # Removing \r because removing the spaces broke the formatting
        out = str(out).replace("\r", "")

    out = str(out).split("\n")  # Making each process into a list
    out = out[3:]  # Removing the first 3 which are all just
    print(out)


# Getting Applications in Focused Ordered
def get_focused():
    process = subprocess.Popen(["powershell.exe",
                                "C:\\Users\\maxla\\PycharmProjects\\discordVLC\\getfocused.ps1"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out = process.stdout.read().decode(encoding='UTF-8').rstrip()  # Decoding
    while "  " in str(out):  # Removing all the spaces PS uses
        out = str(out).replace("  ", " ")
    while "\r" in str(out):  # Removing \r because removing the spaces broke the formatting
        out = str(out).replace("\r", "")

    out = str(out).split("\n")  # Making each process into a list
    out = out[3:]  # Removing the first 3 which are all just
    print(out)


def start():
    """
    If you want to upload media it needs to be uploaded here:
    https://discordapp.com/developers/applications/{     YOUR CLIENT ID     }/rich-presence/assets
    and you need to use the same filename here as you did when uploading it.
    """

    # Actual stuff being displayed
    RP.update(state="state",
              details="deets",

              large_image="full",
              large_text="VLC Media Player",

              join="text1",
              spectate="text2",
              match="text3",
              instance=False
              )


start()
get_applications()
get_focused()

while True:
    time.sleep(UPDATE_RATE)
