FROM acait/django-container:1.0.35 as app-container

USER root
RUN apt-get update && apt-get install libpq-dev postgresql postgresql-contrib -y
USER acait

ADD --chown=acait:acait retention_data_pipeline/VERSION /app/retention_data_pipeline/
ADD --chown=acait:acait setup.py /app/
ADD --chown=acait:acait requirements.txt /app/
RUN . /app/bin/activate && pip install -r requirements.txt

ADD --chown=acait:acait . /app/
ADD --chown=acait:acait docker/ project/

FROM acait/django-test-container:1.0.35 as app-test-container

COPY --from=0 /app/ /app/
COPY --from=0 /static/ /static/
