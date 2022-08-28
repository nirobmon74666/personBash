sudo apt install python3
sudo apt install pip
pip install selenium
pip install pyvirtualdisplay
sudo apt install -y xvfb
wget "https://raw.githubusercontent.com/nirobmon74666/personBash/main/geko/battle.py"
wget "https://raw.githubusercontent.com/nirobmon74666/personBash/main/geko/work.py"
wget "https://github.com/nirobmon74666/personBash/raw/main/geko/ub.xpi"
wget "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz"
sudo tar -xvf geckodriver-*
sudo chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
cd /root/.mozilla/firefox/*.default-release
pwd > /root/path.txt
