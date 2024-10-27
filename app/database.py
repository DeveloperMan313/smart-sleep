from app.models import Alarm, Alarm_timetable, Timetable, Weekday
from datetime import date, time

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

def get_alarm(alarm_timetable_id: int) -> dict:
    timetable = Alarm_timetable.objects.get(id = alarm_timetable_id)
    res_dict = {'time': timetable.time, 'days': [], 'n_repeats': timetable.repeat_times}
    weekday_alarms = Alarm.objects.filter(alarm_timetable = alarm_timetable_id)
    for day in weekday_alarms:
        res_dict['days'].append(day.weekday)
    return res_dict

def add_latest_quality(quality: int):
    last_sleep = Timetable.objects.last()
    last_sleep.sleep_quality = quality
    last_sleep.save()

def add_sleep(day, start_time):
    Timetable.objects.all()
    weekday_alarm = Alarm.objects.get(weekday = day)
    new_sleep = Timetable(weekday = day, sleep_start = start_time, sleep_finish = weekday_alarm.alarm_timetable.time)
    new_sleep.save()
    if new_sleep.id >= 50:
        return

def get_weekday_sleep(day:int):
    result = []
    Timetable.objects.all()
    sleeps = Timetable.objects.filter(weekday = day)
    for sleep in sleeps:
        x = (sleep.sleep_finish - sleep.sleep_start)
        if x < 0:
            x += (24 * 60)
        result.append(x)
    return result