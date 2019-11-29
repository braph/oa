#!/bin/bash

# Bind ~/.openarena to a tmpfs for getting a clean configuration.
# Start a game to initialize some cvars.
# Execute `cvarlist` to dump the cvars with the defaults.

if (( UID == 0 )); then
  echo "DO NOT RUN THIS AS ROOT!"
  exit 1
fi

echo '!!! THIS WILL MOUNT A TMPFS ON ~/.openarena !!!'
echo '!!! SUDO REQUIRED !!! '''
echo '!!! PRESS ENTER 3 TIMES TO PROCEED !!!'
read;read;read
sudo mount -t tmpfs none "$HOME"/.openarena || exit
openarena +devmap oasago2 +wait 500 +echo CVARLIST_BEGIN +cvarlist +quit &> cvardump.out
sudo umount ~/.openarena

