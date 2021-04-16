#!/bin/bash

# Install Brave
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt-get update -q
sudo apt-get install -q brave-browser
sudo apt-get remove -q firefox

# Install Spotify
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update -q && sudo apt-get install -q spotify-client

# Install Git
sudo apt-get install -q Git
git config --global user.name "Chris Walters"
git config --global user.email christopherman2cool@gmail.com

# Install VS Code
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt-get install -q apt-transport-https
sudo apt-get update -q 
sudo apt-get install -q code

# Install Discord
cd ~/Downloads
wget -qO discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"
sudo apt-get install -q discord.deb
rm -f discord.deb

# Install GIMP
sudo apt install -q gimp

