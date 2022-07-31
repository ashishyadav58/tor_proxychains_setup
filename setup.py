import os

os.system("sudo apt update -y && sudo apt install tor proxychains4 git curl -y && rm -rf /etc/proxychains4.conf && cp -r proxychains4.conf /etc")
