from django.db import models

QUARTER_CHOICES = ((1, 'Winter'),
                   (2, 'Spring'),
                   (3, 'Summer'),
                   (4, 'Autumn'))


class Student(models.Model):
    CAMPUS_CHOICES = ((1, 'Seattle'),
                      (2, 'Tacoma'),
                      (3, 'Bothell'))
    last_yr_enrolled = models.PositiveSmallIntegerField()
    last_qtr_enrolled = models.PositiveSmallIntegerField(
        default=1, choices=QUARTER_CHOICES)
    system_key = models.PositiveIntegerField()
    uw_netid = models.CharField(max_length=128)
    student_no = models.PositiveIntegerField()
    student_name_lowc = models.TextField()
    proc_ind = models.PositiveSmallIntegerField()
    spcl_program = models.PositiveSmallIntegerField()
    major_campus = models.PositiveSmallIntegerField(
        default=1, choices=CAMPUS_CHOICES)
    deg_level = models.PositiveSmallIntegerField()
    major_abbr = models.CharField(max_length=6)


class Section(models.Model):
    year = models.PositiveSmallIntegerField()
    quarter = models.PositiveSmallIntegerField(
        default=1, choices=QUARTER_CHOICES)
    course_no = models.PositiveSmallIntegerField()
    dept_abbrev = models.CharField(max_length=6)
    section_id = models.CharField(max_length=3)
    sln = models.PositiveIntegerField()
