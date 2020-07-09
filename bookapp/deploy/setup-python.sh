# recreate python environment
sudo apt-get update
sudo apt-install python3
# sudo apt-install python3-venv
# python3 -m venv venv
sudo apt-install python3-pip
# source venv/bin/activate
<<<<<<< HEAD
pip install -r requirements.txt
# fails building wheel for: Flask-Bcrypt, PyYML, SQLAlchemy
=======
pip3 install -r requirements.txt
# fails building wheel for: Flask-Bcrypt, PyYML, SQLAlchemy
>>>>>>> 63f6933b38db0d8e4f9e401d76e86b064ba306f4
