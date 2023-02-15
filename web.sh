rm google-chrome-stable_current_amd64.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
sudo cp chromedriver /usr/lib
sudo chmod +x /usr/lib/chromedriver
sudo cp chromedriver /usr/bin
sudo chmod +x /usr/bin/chromedriver
sudo apt install -y xvfb
sudo apt install -y screen
#sudo cp resolv.conf /etc/
pip3 install pyvirtualdisplay
#source piyo/bin/activate
