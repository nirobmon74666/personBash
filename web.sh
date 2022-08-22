sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
sudo cp chromedriver /usr/lib
sudo cp chromedriver /usr/bin
sudo apt install -y xvfb
sudo apt install screen -y
