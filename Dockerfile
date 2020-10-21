FROM acait/django-container:1.1.7 as app-container

USER root
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install libpq-dev postgresql postgresql-contrib unixodbc-dev freetds-dev -y
RUN apt-get update && apt-get install tdsodbc -y
USER acait

ADD --chown=acait:acait retention_data_pipeline/VERSION /app/retention_data_pipeline/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/
RUN . /app/bin/activate && pip install -r requirements.txt

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ project/

FROM acait/django-test-container:1.0.35 as app-test-container


COPY --from=app-container /app/ /app/
COPY --from=app-container /static/ /static/