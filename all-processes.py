# coding=utf-8
"""
This application allows you to display what application you are running to Discord with Rich Presence. This is done by
running Powershell scripts that get your current process running. To run Powershell files in Python, you first need to
do a few things;

1.) You need to allow Powershell files to be opened via Python. You can learn how to do that here:
    https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6

2.) To properly read the data I would recommend setting the default encoding of Powershell to UTF-8. You can learn
    how to do that here:
    https://stackoverflow.com/questions/40098771/changing-powershells-default-output-encoding-to-utf-8

Also, if you an icon to be displayed it needs to be uploaded here:
https://discordapp.com/developers/applications/<Your Client ID>/rich-presence/assets

If you can't figure something out or stuff is broke, feel free to DM me on Discord, Mehvix#7172
"""

import json
import subprocess
import time

import pypresence

# Opens config.json
with open('config.json') as config:
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

# Defining and Connecting
RP = pypresence.Presence(client_id=CLIENT_ID, pipe=PIPE, loop=LOOP, handler=HANDLER)
RP.connect()


# Getting Applications in Focused Ordered
def get_focused():
    process = subprocess.Popen(["powershell.exe",
                                "C:\\Users\\maxla\\PycharmProjects\\discordVLC\\getfocused.ps1"],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    try:
        out = process.stdout.read().decode(encoding='UTF-8').rstrip()  # Decoding - make sure you've read the readme
    except UnicodeDecodeError:
        start()
        return

    print(out)
    out = str(out).split("\n")  # Making each line into a list
    out = out[3:]  # Removing the first 3 which are all just notations

    split = str("".join(out)).split("  ")
    newsplit = []
    for x in split:  # Removes all spaces in out
        if x != "":
            newsplit.append(x)
    print(newsplit)

    # Examples:
    # ['pycharm64', ' discord-application-rp [C:\\Users\\maxla\\PycharmProjects\\discordVLC] - ...\\open-me.py [discord-application...']
    # ['chrome', 'Omni/Stone ep. 67 w/ Brian Kibler, Frodan & Special Guests: Disguised Toast + Trump! - YouTube - Google ...']
    # ['Discord', ' #??discussion - Discord', '6227208']
    # ['slack', ' Slack - BadgerBOTS', ' 132338']
    try:
        name = str(newsplit[0]).title()
        details = newsplit[1]
    except IndexError as error:
        print("There was an error!: {}".format(error))
        start()
        return

    if name == "Discord":
        details = details.replace("??", "")

    image = name.lower()  # todo add reddit, github, khan academny,
    if name == "Chrome":
        websites = ["YouTube", "Drive", "Sheets", "Docs", "Slides", "Gmail", "4chan", "Stack", "Udemy", "Khan",
                    "Syndicate", "HSReplay.net", "TypeRacer", "Twitter", "Twitch"]
        for page in websites:
            if page in details:
                image = page.lower()
                name = page.title()

    if name == "Vlc":
        name = "VLC"

    details = details.split(" - ")[0]

    RP.update(details=name,
              state=details,
              spectate="https://github.com/Mehvix/discord-application-presence/",
              instance=False,

              large_image=image.replace(" ", "_").replace(".", "_"),
              large_text=details
              )


def start():
    # Actual stuff being displayed
    RP.update(state="https://github.com/Mehvix/discord-application-presence/",
              details="Not currently in a application",
              spectate="https://github.com/Mehvix/discord-application-presence/",
              instance=False
              )


start()
while True:
    get_focused()
    time.sleep(UPDATE_RATE)
