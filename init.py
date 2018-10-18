# coding=utf-8
import vlc
import json
import time
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

# Defining and Connecting
RP = pypresence.Presence(client_id=custom_client_id, pipe=custom_pipe, loop=custom_loop, handler=custom_handler)
RP.connect()


# VLC Settings
instance = vlc.Instance()


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

while True:
    time.sleep(15)
