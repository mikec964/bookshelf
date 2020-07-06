# recreate python environment
sudo apt-get update
sudo apt-install python3
# sudo apt-install python3-venv
# python3 -m venv venv
sudo apt-install python3-pip
# source venv/bin/activate
pip3 install -r requirements.txt
# fails building wheel for: Flask-Bcrypt, PyYML, SQLAlchemy
