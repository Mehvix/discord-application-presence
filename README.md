This application allows you to display what application you are running to Discord with Rich Presence. This is done by
running Powershell scripts that get your current process running. To run Powershell files in Python, you first need to
do a few things;

1.) You need to allow Powershell files to be opened via Python. You can learn how to do that here:
    https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6

2.) To properly read the data I would recommend setting the default encoding of Powershell to UTF-8. You can learn
    how to do that here:
    https://stackoverflow.com/questions/40098771/changing-powershells-default-output-encoding-to-utf-8

Also, if you an icon to be displayed it needs to be uploaded here:

https://discordapp.com/developers/applications/`Your Client ID`/rich-presence/assets
