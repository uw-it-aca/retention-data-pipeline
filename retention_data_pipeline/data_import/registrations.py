from retention_data_pipeline.models import StudentRegistration, Student
from retention_data_pipeline.dao.edw import (get_day1_enrollments,
                                             get_netids,
                                             get_international_students)


# def get_student_registrations(year, quarter):
#     d1_enrollemnts = get_day1_enrollments(year, quarter)
#     netids = get_netids(year, quarter)


def get_students_for_term(year, quarter):
    _get_sr_mini_master_students(year, quarter)
    _add_international_status(year, quarter)


def _get_sr_mini_master_students(year, quarter):
    """
    Queries the sr_mini_master table and gets active students for a given term
    Also includes EOP status
    """
    students = get_day1_enrollments(year, quarter)
    student_models = []
    for index, row in students.iterrows():
        major = row['mm_major_abbr']
        student = Student(year=year,
                          quarter=quarter,
                          system_key=row['mm_system_key'],
                          is_eop=row['eop_student'],
                          is_premajor=("PRE" in major or major == 'EPRMJ')
                          )
        student_models.append(student)
    Student.objects.bulk_create(student_models)


def _add_international_status(year, quarter):
    """
    Updates Student Objects with international status
    """
    intl_students = get_international_students()
    students = Student.objects.filter(year=year, quarter=quarter)
    for student in students:
        intl_matches = \
            intl_students[intl_students.SDBSrcSystemKey == student.system_key]
        if len(intl_matches.index) > 1:
            student.is_international = True
    Student.objects.bulk_update(students, ['is_international'])
