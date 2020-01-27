# http://www.mamicode.com/info-detail-2204421.html
sudo apt-get update
sudo apt-get install python-pip
sudo pip install shadowsocks
sudo chmod 777 /home
sudo chmod 777 /var/run
sudo chmod 777 /var/log
ssserver -c /home/ss.json -d start