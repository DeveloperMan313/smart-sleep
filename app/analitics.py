from app.database import *

def optimal_time_sleep(weekday):
    time_sleep = get_weekday_sleep(weekday)
    request = get_quality(weekday)
    if (request.index(max(request)) == time_sleep.index(max(time_sleep)) and request.count(max(request)) == 1):
        k = max(request) / 10  # большой шаг в час
        optimal_time_sleep = time_sleep[time_sleep.index(max(time_sleep))] / k
    elif (request.index(max(request)) == time_sleep.index(min(time_sleep)) and request.count(max(request)) == 1):
        k = max(request) / 10
        optimal_time_sleep = time_sleep[time_sleep.index(min(time_sleep))] * k
    else:
        x = 0
        for i in range(0, len(time_sleep)):
            x += (time_sleep[i] * request[i])
        optimal_time_sleep = x / sum(request)

    return optimal_time_sleep

def func_first_event (time_sleep, optimal_time_sleep, average_gradue_time_sleep):

    summ_time_sleep =0


    for i in range (len(time_sleep)):

        summ_time_sleep+= time_sleep[i]
    average_time_sleep = summ_time_sleep/len(time_sleep)
    print(average_time_sleep)
    if average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and average_gradue_time_sleep>=8:
        print("good")
        return 1
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and average_gradue_time_sleep <5:
        print("bad")
        return 3
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and 5<= average_gradue_time_sleep <8:
        print("nbad")
        return 2
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep>=8:
        answer = int(input("изменть будильник?(1/0)"))
        if answer==0:
            print('gbj')
            return 2
        else:
            optimal_time_sleep = average_time_sleep
            print(optimal_time_sleep)
            return 2
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep<8:
        print("Еблан?")
        return 3





    #функция второго случая
def func_second_event(time_sleep, gradue_optimal_time_sleep,average_fist_gradue_time_sleep, average_second_gradue_time_sleep,optimal_time_sleep):
    get_date2()
    first_sum_sleep_time =0
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
        print("good")
        return 1
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and gradue_optimal_time_sleep<=average_gradue_time_sleep <8:
        print("nbad")
        return 2
    elif average_time_sleep>=optimal_time_sleep-15 and average_time_sleep<=optimal_time_sleep+15 and gradue_optimal_time_sleep>average_gradue_time_sleep:
        print("bad")
        return 3
    elif (average_time_sleep<optimal_time_sleep-15 or average_time_sleep>optimal_time_sleep+15) and average_gradue_time_sleep>=8:
        optimal_time_sleep = average_time_sleep
        print(optimal_time_sleep)
        return 1
    elif (average_time_sleep < optimal_time_sleep - 15 or average_time_sleep > optimal_time_sleep + 15) and gradue_optimal_time_sleep<=average_gradue_time_sleep <8:
        optimal_time_sleep = average_time_sleep
        print(optimal_time_sleep)
        print('mbad')
        return 2
    elif (average_time_sleep < optimal_time_sleep - 15 or average_time_sleep > optimal_time_sleep + 15) and average_gradue_time_sleep < gradue_optimal_time_sleep:
        print('vbad')
        return 3




#функция первого определения случаев
def func_type_get_date ( gradue_optimal_time_sleep):
    if  gradue_optimal_time_sleep >= 8:
        return 1
    if  5 <=gradue_optimal_time_sleep < 8:
        return 2
    if  gradue_optimal_time_sleep <5:
        return 3
gradue_optimal_time_sleep =10










for i in range (len(time_start)):
    time_sleep = time_finish[i]- time_start[i]
    if time_sleep <= 0:
        time_sleep+=24*60
while time_sleep<optimal_time_sleep-15 and time_sleep>optimal_time_sleep+15:
        #get_date3()
        exit()
if time_sleep>=optimal_time_sleep-15 and time_sleep<=optimal_time_sleep+15:
    x = func_type_get_date(gradue_optimal_time_sleep)
    match (x):
        case 1:
            # get_date1()
            func_first_event(time_sleep, optimal_time_sleep, average_gradue_time_sleep)
        case 2:
            # get date2()
            func_second_event(time_sleep, gradue_optimal_time_sleep, average_fist_gradue_time_sleep,
                              average_second_gradue_time_sleep, optimal_time_sleep)
        case 3:
            #get_date3()

        # gradue_optimal_time_sleep = int(input("как спалось?\n"))
        # if gradue_optimal_time_sleep>=8:
        #     average_gradue_time_sleep = int(input("как вы спали этот месяц?\n"))
        #     time_finish_first_event = [optimal_time_sleep-20 , optimal_time_sleep-20 , optimal_time_sleep-20, optimal_time_sleep-20]
        #     time_start_first_event = [0, 0, 0,0]
        #     func_first_event(time_start_first_event, time_finish_first_event, gradue_optimal_time_sleep, optimal_time_sleep)
        # if 5 <= gradue_optimal_time_sleep < 8:
        #
        #     time_sleep_massiv = [optimal_time_sleep, optimal_time_sleep, optimal_time_sleep, optimal_time_sleep]
        #     average_fist_gradue_time_sleep = int(input('как спалось первую половину месяца\n'))
        #     average_second_gradue_time_sleep = int(input('как спалось вторую половину месяца\n'))
        #     func_second_event(time_sleep_massiv, gradue_optimal_time_sleep,average_fist_gradue_time_sleep, average_second_gradue_time_sleep,optimal_time_sleep)



