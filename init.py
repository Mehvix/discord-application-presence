# coding=utf-8
import vlc
import sys
import json
import time
import subprocess
import pypresence

# Opens config.json
with open('config.json') as config:
    config = json.load(config)

# Extracts variables from json data (config)
custom_client_id = config['custom_client_id']
custom_pipe = config['custom_pipe']
custom_loop = config['custom_loop']
custom_handler = config['custom_handler']

y = []
# Prints a '=' for how long the Client ID line is
for _ in range(int(len(str(custom_client_id)) + 13)):  # 13 because that's the length of 'Client ID:...'
    y.append("=")

print("".join(y))
# Just to make sure you have the right config selected
print("Client ID:   {}\n"
      "Pipe:        {}\n"
      "Loop:        {}\n"
      "Handler:     {}"
      .format(custom_client_id, custom_pipe, custom_loop, custom_handler))

y = []
for _ in range(int(len(str(custom_client_id)) + 13)):  # 13 because that's the length of 'Client ID:...'
    y.append("=")
print("".join(y))
print("\n")

# Defining and Connecting
RP = pypresence.Presence(client_id=custom_client_id, pipe=custom_pipe, loop=custom_loop, handler=custom_handler)
RP.connect()


# Getting Applications
def get_applications():
    """
    To allow Windows to execute powershell files you first need to allow it access. You can learn how to do this here;
    https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6
    """

    p = subprocess.Popen(["powershell.exe",
                          "C:\\Users\\maxla\\PycharmProjects\\discordVLC\\getprocess.ps1"],
                         stdout=sys.stdout)
    print(p.communicate())


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

while True:
    time.sleep(15)
