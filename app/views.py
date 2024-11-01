from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.forms import *
from app import database
from datetime import datetime, time


DAY_NAMES = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')


def time_m_to_str(time_m: int) -> str:
    return '{:02d}:{:02d}'.format(time_m // 60, time_m % 60)


def time_str_to_m(time_str: str) -> int:
    time_h_m = tuple(map(int, time_str.split(':')))
    return time_h_m[0] * 60 + time_h_m[1]


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # TODO errors with URL params
            if form.data['password'] != form.data['password_repeat']:
                return redirect('/register/')
            print('register form valid!')
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            # if register_user(username, password):
            #     login(request, user)
            #     return redirect('/')
            # else:
            #     return redirect('/register/')
        return redirect('/')


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # TODO errors with URL params
            print('login form valid!')
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
        return redirect('/login/')


@login_required
def logout(request: HttpRequest):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('/login/')


@login_required
def index(request: HttpRequest):
    alarms = database.get_all_alarms()
    for alarm in alarms:
        alarm['days'] = ', '.join(DAY_NAMES[day - 1] for day in alarm['days'])
        alarm['time'] = time_m_to_str(alarm['time'])
    return render(request, 'index.html', context={'alarms': alarms, 'is_logged_in': True})


def get_alarm_form_data(form: AlarmForm) -> tuple:
    alarm_time = time_str_to_m(form.data['time'])
    alarm_days = []
    for day_n in range(1, 8):
        if f'day{day_n}' in form.data:
            alarm_days.append(day_n)
    return (alarm_time, alarm_days, form.data['n_repeats'])


@login_required
def add_alarm(request: HttpRequest):
    if request.method == 'GET':
        days = [{'n': i + 1, 'name': name} for i, name in enumerate(DAY_NAMES)]
        return render(request, 'edit_alarm.html', context={'header': 'Добавить будильник', 'n_repeats': 1, 'days': days, 'is_logged_in': True})

    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            alarm_time, alarm_days, n_repeats = get_alarm_form_data(form)
            database.add_alarm(alarm_time, alarm_days, n_repeats)
        return redirect('/')


@login_required
def edit_alarm(request: HttpRequest, alarm_id: int):
    if request.method == 'GET':
        alarm = database.get_alarm(alarm_id)
        time_str = time_m_to_str(alarm['time'])
        days = [{'n': i + 1, 'name': name, 'checked': i + 1 in alarm['days']}
                for i, name in enumerate(DAY_NAMES)]
        return render(request, 'edit_alarm.html', context={'header': 'Редактировать будильник', 'time': time_str, 'n_repeats': alarm['n_repeats'], 'days': days, 'is_logged_in': True})

    if request.method == 'POST':
        form = AlarmForm(request.POST)
        if form.is_valid():
            alarm_time, alarm_days, n_repeats = get_alarm_form_data(form)
            database.edit_alarm(alarm_id, alarm_time, alarm_days, n_repeats)
        return redirect('/')


@login_required
def remove_alarm(request: HttpRequest, alarm_id: int):
    if request.method == 'POST':
        database.delete_alarm_timetable(alarm_id)
    return redirect('/')


@login_required
def rate(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'rate.html', context={'ratings': range(1, 11), 'is_logged_in': True})

    if request.method == 'POST':
        form = QualityRatingForm(request.POST)
        if form.is_valid():
            print('rating form valid!')
            database.add_latest_quality(request.POST['rating'])
        return redirect('/')


@login_required
def recommendation(request: HttpRequest):
    # time_sleep_m, time_optimal_m, time_finish_m = (
    #     5*60, 7*60, 6*60)  # call to analitic.py
    weekday = datetime.today().weekday() + 1
    time_sleep_m, time_optimal_m, time_finish_m = database.get_user_analitic(
        weekday)
    print(time_sleep_m, time_optimal_m, time_finish_m)

    recommendation = None

    if abs(time_sleep_m - time_optimal_m) > 15:
        time_start_opt_m = time_finish_m - time_optimal_m
        while time_start_opt_m < 0:
            time_start_opt_m += 24 * 60
        time_start_opt_str = time_m_to_str(time_start_opt_m)

        time_finish_opt_m = time_finish_m - time_sleep_m + time_optimal_m
        while time_finish_opt_m > 24 * 60:
            time_finish_opt_m -= 24 * 60
        time_finish_opt_str = time_m_to_str(time_finish_opt_m)

        alarm_id = database.get_alarm_id(weekday)

        if alarm_id is not None:
            recommendation = {
                'issue': 'Вы спите слишком {}'.format('мало' if time_sleep_m < time_optimal_m else 'много'),
                'time_start_opt': time_start_opt_str,
                'alarm_id': alarm_id,
                'time_finish_opt': time_finish_opt_str,
            }

    return render(request, 'recommendation.html', context={'recommendation': recommendation, 'is_logged_in': True})
