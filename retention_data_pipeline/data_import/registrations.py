from retention_data_pipeline.models import StudentRegistration, Student
from retention_data_pipeline.dao.edw import get_day1_enrollments, get_netids


# def get_student_registrations(year, quarter):
#     d1_enrollemnts = get_day1_enrollments(year, quarter)
#     netids = get_netids(year, quarter)


def get_students_for_term(year, quarter):
    _get_sr_mini_master_students(year, quarter)



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

# def _enrich_student_data(year, quarter):
