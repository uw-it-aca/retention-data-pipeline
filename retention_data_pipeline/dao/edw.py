import os
import pyodbc
from django.conf import settings

db = "UWSDBDataStore"


def get_day1_enrollments(year, quarter):
    db_query = """
    SELECT
        CASE WHEN mm_spcl_program IN(1, 2, 13, 14, 16, 17, 31, 32, 33)
            THEN CAST(1 AS BIT)
            ELSE CAST(0 AS BIT)
        END AS eop_student,
        (mm_year*10 + mm_qtr) as yrq,
        mm_system_key, mm_year, mm_qtr
    FROM sec.sr_mini_master
    WHERE mm_year = {} AND mm_qtr = {} AND mm_proc_ind = 2
    """.format(year, quarter)
    results = _run_query(db, db_query)
    return results


def _run_query(database, query):
    os.environ["FREETDSCONF"] = "db_config/freetds.conf"
    os.environ["ODBCSYSINI"] = "db_config"

    password = getattr(settings, "EDW_PASSWORD")
    user = getattr(settings, "EDW_USER")
    server = getattr(settings, "EDW_SERVER")
    constring = "Driver={FreeTDS};" \
                f"SERVERNAME={server};" \
                f"Database={database};" \
                "Port=1433;" \
                "TDS_Version=7.2;" \
                f"UID={user};" \
                f"PWD={password}"
    con = pyodbc.connect(constring)
    cursor = con.cursor()
    cursor.execute(query)
    return cursor
