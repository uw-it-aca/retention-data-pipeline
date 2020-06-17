from django.core.management.base import BaseCommand, CommandError
import os
import pyodbc
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.environ["FREETDSCONF"] = "db_config/freetds.conf"
        os.environ["ODBCSYSINI"] = "db_config"

        password = getattr(settings, "EDW_PASSWORD")
        user = getattr(settings, "EDW_USER")
        server = getattr(settings, "EDW_SERVER")
        constring = "Driver={FreeTDS};" \
                    f"SERVERNAME={server};" \
                    "Database=UWSDBDataStore;" \
                    "Port=1433;" \
                    "TDS_Version=7.2;" \
                    f"UID={user};" \
                    f"PWD={password}"
        con = pyodbc.connect(constring)
        cursor = con.cursor()
        cursor.execute("select * from sec.sr_curric_code where curric_last_yr = 9999")
        row = cursor.fetchone()
        if row:
            print(row)