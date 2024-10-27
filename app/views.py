from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.forms import *
from copy import deepcopy
from datetime import time
from django.template.loader import render_to_string

from app.database import *

ALARMS = [
    {
        'id': i,
        'time': f'{3 + i}:00',
        'days': [1, 2, i],
    } for i in range(1, 4)
]

DAY_NAMES = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')


def index(request: HttpRequest):
    alarms = deepcopy(ALARMS)  # call to DB
    for alarm in alarms:
        alarm['days'] = ', '.join(DAY_NAMES[day - 1] for day in alarm['days'])
    return render(request, 'index.html', context={'alarms': alarms})


def get_alarm_form_data(form: AlarmForm) -> tuple:
    time_h_m = map(int, form.data['time'].split(':'))
    alarm_time = time(*time_h_m)
    alarm_days = []
    for day_n in range(1, 8):
        if f'day{day_n}' in form.data:
            alarm_days.append(day_n)
    return (alarm_time, alarm_days)


def add_alarm1(request: HttpRequest):
    if request.method == 'GET':
        days = [{'n': i + 1, 'name': name} for i, name in enumerate(DAY_NAMES)]
        return render(request, 'edit_alarm.html', context={'n_repeats': 1, 'days': days})
    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            print('add alarm form valid!')
            alarm_time, alarm_days = get_alarm_form_data(form)
            print(alarm_time, alarm_days)  # call to DB
        return redirect('/')


def edit_alarm(request: HttpRequest, alarm_id: int):
    if request.method == 'GET':
        alarm = {'time': time(3, 40), 'days': [
            1, 3, 4], 'n_repeats': 2}  # call to DB
        time_str = '{:02d}:{:02d}'.format(
            alarm["time"].hour, alarm["time"].minute)
        days = [{'n': i + 1, 'name': name, 'checked': i + 1 in alarm['days']}
                for i, name in enumerate(DAY_NAMES)]
        return render(request, 'edit_alarm.html', context={'time': time_str, 'n_repeats': alarm['n_repeats'], 'days': days})
    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            print('add alarm form valid!')
            alarm_time, alarm_days = get_alarm_form_data(form)
            print(alarm_id, alarm_time, alarm_days)  # call to DB
        return redirect('/')

add_latest_quality(7)