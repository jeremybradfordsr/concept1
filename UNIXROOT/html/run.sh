!#/bin/bash
python3 /var/www/html/dirwatch.py&
apachectl -D FOREGROUND
