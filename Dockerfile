FROM tutum/apache-php

CMD mkdir /app/uploads
CMD chown www-data:www-data /var/www/html/uploads
CMD chmod -R 755 /var/www/html/uploads
CMD ["apachectl", "-D", "FOREGROUND"]
EXPOSE 80
