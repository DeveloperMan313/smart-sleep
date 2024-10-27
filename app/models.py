from django.db import models
from enum import Enum

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
    weekday = models.IntegerField()
    sleep_start = models.IntegerField()
    sleep_finish = models.IntegerField()
    sleep_quality = models.IntegerField(default = 5)

class Alarm_timetable(models.Model):
    time = models.IntegerField()
    repeat_times = models.IntegerField()

class Alarm(models.Model):
    alarm_timetable = models.ForeignKey(Alarm_timetable, on_delete=models.CASCADE)
    weekday = models.IntegerField()
