FROM tutum/apache-php

RUN mkdir /app/uploads
RUN chown www-data:www-data /var/www/html/uploads
RUN chmod -R 755 /var/www/html/uploads

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get -y install python3-pip
RUN pip3 install watchdog

CMD bash /var/www/html/run.sh
EXPOSE 80
