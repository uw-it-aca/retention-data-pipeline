import os
import pyodbc
import pandas
from django.conf import settings

DB = "UWSDBDataStore"


def get_day1_enrollments(year, quarter):
    db_query = """
    SELECT
        CASE WHEN mm_spcl_program IN(1, 2, 13, 14, 16, 17, 31, 32, 33)
            THEN CAST(1 AS BIT)
            ELSE CAST(0 AS BIT)
        END AS eop_student,
        (mm_year*10 + mm_qtr) as yrq,
        mm_system_key, mm_year, mm_qtr
    FROM
        sec.sr_mini_master
    WHERE
        mm_year = {} AND mm_qtr = {} AND mm_proc_ind = 2
    """.format(year, quarter)
    results = _run_query(DB, db_query)
    return results


def get_ts_courses(year, quarter):
    db_query = """
    SELECT
        ts_year,
        ts_quarter,
        course_no,
        dept_abbrev,
        section_id,
        sln
    FROM
        sec.time_schedule
    WHERE
        ts_year = {}
        AND ts_quarter = {}
    """.format(year, quarter)
    results = _run_query(DB, db_query)
    return results


def get_registrations(year, quarter):
    db_query = """
        SELECT
            system_key,
            regis_yr,
            regis_qtr,
            sln
        FROM
            sec.registration_courses
        WHERE
            regis_yr = {}
            AND regis_qtr = {}
            AND request_status in ('A', 'C', 'R')
        """.format(year, quarter)
    results = _run_query(DB, db_query)
    return results


def get_netids(year, quarter):
    db_query = """
        SELECT
            system_key,
            uw_netid,
            student_no,
            student_name_lowc
        FROM
            sec.student_1
        WHERE
            last_yr_enrolled = {}
            AND last_qtr_enrolled = {}
    """.format(year, quarter)
    results = _run_query(DB, db_query)
    return results


def get_majors(year, quarter):

    db_query = """
        #TODO: Determine relationship w/ mini_maser and write query
        """.format(year, quarter)
    results = _run_query(DB, db_query)
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
    df = pandas.read_sql(query, con)
    return df
