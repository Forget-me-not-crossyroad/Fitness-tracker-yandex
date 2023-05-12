import datetime as dt
import randomtimestamp

endDate_1 = dt.time(6, 00, 00)
endDate_2 = dt.time(12, 00, 00)
endDate_3 = dt.time(18, 00, 00)
endDate_4 = dt.time(23, 00, 00)

a = randomtimestamp.random_time()
# print(a)

HEIGHT = 175
WEIGHT = 75
FORMAT = '%H:%M:%S'
STEP_M = 0.65
TRANSFER_COEFF = 1000
K_1 = 0.035
K_2 = 0.029
storage_data = {}


def accept_package(package):
    storage_data_internal = {}
    if check_correct_data(package[1]) and check_correct_time(package[0]):
        storage_data_internal[package[0]] = package[1]
    else:
        return 'Получен поврежденный пакет данных'
    print(storage_data_internal)
    storage_data.update(storage_data_internal)
    steps = get_step_day(storage_data)
    dist = get_distance(steps)
    current_time = package[0]
    current_steps = package[1]
    print(f'Время: {current_time}/nКоличество шагов за сегодня: {steps}./nДистанция составила {dist} км./nВы сожгли {get_spent_calories(current_steps, current_time)} ккал./n{get_achievement(dist)}')


def get_achievement(dist):
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def check_correct_data(data):
    print(data)
    return True


def check_correct_time(time):
    print(time)
    return True


def get_step_day(dict_steps):
    return sum(step for step in dict_steps.values())


def get_distance(steps):
    return int((steps * STEP_M) / TRANSFER_COEFF)


def get_spent_calories(current_steps, current_time):
    time_list = list(storage_data.keys())
    steps_list = list(storage_data.values())
    if len(storage_data) != 1:
        time_1 = dt.datetime.strptime(current_time, FORMAT)
        time_2 = dt.datetime.strptime(time_list[len(storage_data) - 2], FORMAT)
        dist_delta = current_steps - steps_list[len(storage_data) - 2]
        hour_1 = time_1.hour + time_1.minute / 60 + time_1.second / 3600
        hour_2 = time_2.hour + time_2.minute / 60 + time_2.second / 3600
        time_delta = hour_1 - hour_2
        V = get_distance(dist_delta) / round(time_delta)
    else:
        time_1 = dt.datetime.strptime(current_time, FORMAT)
        time_2 = dt.datetime.strptime('0:00:00', FORMAT)
        hour_1 = time_1.hour + time_1.minute / 60 + time_1.second / 3600
        hour_2 = time_2.hour + time_2.minute / 60 + time_2.second / 3600
        time_delta = hour_1 - hour_2
        V = get_distance(current_steps) / round(time_delta)
    print(V)
    return round(K_1 * WEIGHT + (V**2 / HEIGHT) * K_1 * WEIGHT)


def time_interval_calculation():
    print('Nothing')

def Convert(tup, di):
    di = dict(tup)
    return di


def show_message(time, steps, dist, calories, achievement):
    print(f'Время: {time}/nКоличество шагов за сегодня: {steps}./nДистанция составила {dist} км./nВы сожгли {calories} ккал./n{achievement}')


package2 = ('9:36:02', 15000)


package3 = ('11:00:02', 15000)


accept_package(package2)


accept_package(package3)