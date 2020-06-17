FROM acait/django-container:1.0.22 as django

USER root
RUN apt-get update
RUN apt-get install -y libpq-dev unixodbc-dev freetds-dev tdsodbc
USER acait

ADD --chown=acait:acait retention_data_pipeline/VERSION /app/retention_data_pipeline/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/

RUN . /app/bin/activate && pip install -r requirements.txt
RUN . /app/bin/activate && pip install psycopg2

ADD --chown=acait:acait . /app/
#ADD --chown=acait:acait docker/app_deploy.sh /scripts/app_deploy.sh
#ADD --chown=acait:acait docker/ project/
#RUN chmod u+x /scripts/app_deploy.sh
RUN . /app/bin/activate
