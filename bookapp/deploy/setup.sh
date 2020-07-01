# run with sudo
cp flaskapp /etc/nginx/sites-enabled/
service nginx restart

cp gunicorn3.service /etc/systemd/system/
cd /etc/systemd/system
systemctl daemon-reload
service gunicorn3 restart
