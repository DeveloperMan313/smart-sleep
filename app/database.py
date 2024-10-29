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
    x=0
    k=0
    Timetable.objects.all()
    weekday_alarm = Alarm.objects.get(weekday = day)
    new_sleep = Timetable(weekday = day, sleep_start = start_time, sleep_finish = weekday_alarm.alarm_timetable.time)
    new_sleep.save()

    cut = 2
    if cut != 0 and get_weekday_sleep(day) >= optimal_time - 15 and get_weekday_sleep(day) <= optimal_time + 15:
        number=func_type_get_date(get_quality(day)[-1])
        match (number):
            case 1:
                x=1
                # get_date1()
            case 2:
                x=2
                # get date2()
        cut=0

    if new_sleep.id >= 50:
        k+=1
        if x==0:
            optimal_time = optimal_time_sleep(day)
            cut=1
        elif x==1:
            func_first_event(get_weekday_sleep(day)[50*k+1:], optimal_time_sleep, number)
        elif x==2:
            func_second_event(get_weekday_sleep(day)[50*k+1], get_quality(day)[-1], optimal_time,get_quality(dat)[50*k+25],get_quality(day)[-1])

def func_first_event (time_sleep, optimal_time_sleep, average_gradue_time_sleep):

    summ_time_sleep =0


    for i in range (len(time_sleep)):

        summ_time_sleep+= time_sleep[i]
    average_time_sleep = summ_time_sleep/len(time_sleep)
    
    if average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and average_gradue_time_sleep>=8:
        return 1
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and average_gradue_time_sleep <5:
        
        return 3
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and 5<= average_gradue_time_sleep <8:
        
        return 2
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep>=8:
        answer = int(input("изменть будильник?(1/0)"))
        if answer==0:
            
            return 2
        else:
            optimal_time_sleep = average_time_sleep
            
            return 2
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep<8:
        
        return 3
    
    #функция второго случая
def func_second_event(time_sleep, gradue_optimal_time_sleep,optimal_time_sleep,average_fist_gradue_time_sleep,average_second_gradue_time_sleep):
    first_sum_sleep_time = 0
    second_sum_sleep_time = 0
    for i in range(len(time_sleep)):
        if i <= len(time_sleep)//2:
            first_sum_sleep_time +=time_sleep[i]
        else:
            second_sum_sleep_time += time_sleep[i]
    first_average_sleep_time = first_sum_sleep_time/(len(time_sleep)//2)
    second_average_sleep_time = second_sum_sleep_time / (len(time_sleep)-(len(time_sleep) // 2))
    average_time_sleep = (first_average_sleep_time+second_average_sleep_time)/2
    average_gradue_time_sleep = (average_fist_gradue_time_sleep+average_second_gradue_time_sleep)/2
    if average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and average_gradue_time_sleep>=8:
        return 1
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and gradue_optimal_time_sleep<=average_gradue_time_sleep <8:
        return 2
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and gradue_optimal_time_sleep>average_gradue_time_sleep:
        return 3
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep>=8:
        optimal_time_sleep = average_time_sleep
        
        return 1
    elif (average_time_sleep < optimal_time_sleep - 15 or average_time_sleep > optimal_time_sleep + 15) and gradue_optimal_time_sleep<=average_gradue_time_sleep <8:
        optimal_time_sleep = average_time_sleep
        
        return 2
    elif (average_time_sleep < optimal_time_sleep - 15 or average_time_sleep > optimal_time_sleep + 15) and average_gradue_time_sleep < gradue_optimal_time_sleep:
        return 3


def func_type_get_date ( gradue_optimal_time_sleep):
    if  gradue_optimal_time_sleep >= 8:
        return 1
    if  5 <=gradue_optimal_time_sleep < 8:
        return 2
    if  gradue_optimal_time_sleep <5:
        return 3


def optimal_time_sleep(weekday):
    time_sleep = get_weekday_sleep(weekday)
    request = get_quality(weekday)
    if len(request) == 0:
        return 0
    if (request.index(max(request)) == time_sleep.index(max(time_sleep)) and request.count(max(request)) == 1):
        k = max(request) / 10  # большой шаг в час
        optimal_time_sleep = time_sleep[time_sleep.index(max(time_sleep))] / k
    elif (request.index(max(request)) == time_sleep.index(min(time_sleep)) and request.count(max(request)) == 1):
        k = max(request) / 10
        optimal_time_sleep = time_sleep[time_sleep.index(min(time_sleep))] * k
    else:
        x = 0
        for i in range(len(time_sleep)):
            x += (time_sleep[i] * request[i])
        optimal_time_sleep = x / sum(request)

    return optimal_time_sleep

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

def time_sleep(result):
    if len(result) == 0:
        return 0
    return sum(result)/len(result)

def get_quality(day:int):
    result = []
    Timetable.objects.all()
    sleeps = Timetable.objects.filter(weekday = day)
    for sleep in sleeps:
        result.append(sleep.sleep_quality)
    return result


def get_user_analitic(weekday: int):
    return (int(time_sleep(get_weekday_sleep(weekday))), int(optimal_time_sleep(weekday)), int(get_alarm_id(weekday)))


def delete_alarms(alarm_timetable_id: int):
    timetable = Alarm_timetable.objects.get(id = alarm_timetable_id)
    weekday_alarms = Alarm.objects.filter(alarm_timetable = alarm_timetable_id)
    for day in weekday_alarms:
        day.delete()

def edit_alarm(alarm_id: int, alarm_time: int, alarm_days: int, reps: int):
    timetable = Alarm_timetable.objects.get(id = alarm_id)
    timetable.time = alarm_time
    delete_alarms(alarm_id)
    for day in alarm_days:
        new_alarm = Alarm(alarm_timetable = timetable, weekday = day)
        new_alarm.save()
    timetable.repeat_times = reps
    timetable.save()

def delete_alarm_timetable(alarm_id):
    timetable = Alarm_timetable.objects.get(id = alarm_id)
    delete_alarms(alarm_id)
    timetable.delete()

def get_alarm_id(weekday_: int):
    if Alarm.objects.filter(weekday = weekday_).exists():
        al = Alarm.objects.get(weekday = weekday_)
        return al.alarm_timetable.id
    else: 
        return None