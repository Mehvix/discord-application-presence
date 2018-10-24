# coding=utf-8
"""
Read all-processes.py if stuff isn't working.
If you can't figure something out or something broke feel free to DM me on Discord, Mehvix#7172
"""

import json
import os
import subprocess
import time

import pypresence

# Opens config.json
with open('vlc-config.json') as config:
    config = json.load(config)

# Extracts variables from json data (config)
CLIENT_ID = config['client_id']
PIPE = config['pipe']
LOOP = config['loop']
HANDLER = config['handler']
UPDATE_RATE = config['update_rate']

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

# Establishing a Connection
RP = pypresence.Presence(client_id=CLIENT_ID, pipe=PIPE, loop=LOOP, handler=HANDLER)
RP.connect()
start = time.time().__round__()
RP.update(start=start)


def connect():
    # Actual stuff being displayed
    process = subprocess.Popen(["powershell.exe",
                                "C:\\Users\\maxla\\PycharmProjects\\discordVLC\\getallprocesses.ps1"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    try:
        out = process.stdout.read().decode(encoding='UTF-8').rstrip()  # Decoding - make sure you've read the readme
    except UnicodeDecodeError:
        "ERROR"
        return
    print(out + "\n")
    out = out.replace("\r", "")
    out = out.split("\n")

    k = []
    for i in out:
        j = i.replace('  ', '')
        k.append(j)

    print(k)

    file_name = "No file playing"
    ending = ""

    for x in k:  # Finds VLC
        if " - VLC media player" in x:
            file = x.replace(" - VLC media player", "")[3:]  # 3 because it cuts off "vlc"
            ending = "".join(file.split(".")[-1])
            file_name = file.replace(ending, "")[:-1]

    RP.clear(pid=os.getpid())

    RP.update(details=file_name,
              state="File Type: {}".format(ending),
              large_image="vlc-zoom-out",
              large_text=file_name)


while True:
    connect()
    time.sleep(15)
