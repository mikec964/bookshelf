# run with `sudo ./setup-www.sh`

apt-get install nginx
cp bookshelf /etc/nginx/sites-enabled/
systemctl restart nginx

apt-get install gunicorn3
cp gunicorn3.service /etc/systemd/system/
systemctl daemon-reload
systemctl restart gunicorn3

systemctl status nginx
systemctl status gunicorn3
