# run with `sudo ./setup.sh`

cp bookshelf /etc/nginx/sites-enabled/
service nginx restart
service nginx status

cp gunicorn3.service /etc/systemd/system/
systemctl daemon-reload
service gunicorn3 restart
service gunicorn3 status
