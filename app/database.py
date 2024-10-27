from app.models import User, Alarm, Alarm_timetable, Timetable, Weekday
from datetime import date, time

def init_db():
    User.objects.all()
    Alarm.objects.all()
    Alarm_timetable.objects.all()
    Timetable.objects.all()

def add_user(username_:str, password_:str):
    User.objects.all()
    new_user = User(username = username_, password_hash = password_)
    new_user.save()

def delete_user(username_):
    User.delete(username_)

def add_timetable(day: Weekday, start:int, finish:int):
    Timetable.objects.all()
    new_timetable = Timetable(weekday = day, sleep_start = start, sleep_finish = finish)
    new_timetable.save()

def add_alarm(time_:int, days:int, reps:int):
    Alarm_timetable.objects.all()
    new_alarm_timetable = Alarm_timetable(time = time_, repeat_times = reps)
    new_alarm_timetable.save()
    for day in days:
        new_alarm = Alarm(alarm_timetable = new_alarm_timetable, weekday = day)
        new_alarm.save()

def get_all_alarms() -> list[dict]:
    result = []
    alarms = Alarm_timetable.objects.all()
    for alarm in alarms:
        res_dict = {'id': alarm.id, 'time': alarm.time, 'days': []}
        weekday_alarms = Alarm.objects.filter(alarm_timetable = alarm)
        for day in weekday_alarms:
            res_dict['days'].append(day.weekday)
        result.append(res_dict)
    return result

def get_alarm(alarm_timetable_id: int) -> list[dict]:
    result = []
    timetable = Alarm_timetable.objects.get(id = alarm_timetable_id)
    res_dict = {'time': timetable.time, 'days': []}
    weekday_alarms = Alarm.objects.filter(alarm_timetable = alarm_timetable_id)
    for day in weekday_alarms:
        res_dict['days'].append(day.weekday)
    result.append(res_dict)
    return result
