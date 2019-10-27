FROM tutum/apache-php


CMD ["apachectl", "-D", "FOREGROUND"]
EXPOSE 80
