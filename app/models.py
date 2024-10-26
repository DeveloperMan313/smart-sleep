from django.db import models
from enum import Enum

class User(models.Model):
    user_id = models.IntegerField
    username = models.CharField(max_length = 20, unique = True)
    password_hash = models.CharField(max_length=40)

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    @classmethod
    def get_int(Day):
        return Weekday(Day).value

class Timetable(models.Model):
    timetable_id = models.IntegerField()
    weekday = models.IntegerField()
    date = models.DateField()
    sleep_start = models.TimeField()
    sleep_finish = models.TimeField()

class Sleep(models.Model):
    sleep_id = models.IntegerField()
    sleep_duration = models.IntegerField()
    sleep_quality = models.IntegerField(default=5)

class Alarm_timetable(models.Model):
    alarm_timetable_id = models.IntegerField()
    time = models.TimeField()
    repeat_times = models.IntegerField()

class Alarm(models.Model):
    alarm_id = models.IntegerField()
    alarm_timetable_id = models.IntegerField()
    one_off = models.BooleanField(default=True)
    weekday = models.IntegerField()

class Pre_alarm(models.Model):
    pre_alarm_id = models.IntegerField()
    pre_alarm_time = models.IntegerField()
    ligth_sleep = models.BooleanField()
