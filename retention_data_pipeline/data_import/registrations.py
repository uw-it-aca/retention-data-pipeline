from retention_data_pipeline.models import StudentRegistration
from retention_data_pipeline.dao.edw import get_day1_enrollments, get_netids


def get_student_registrations(year, quarter):
    d1_enrollemnts = get_day1_enrollments(year, quarter)
    netids = get_netids(year, quarter)
