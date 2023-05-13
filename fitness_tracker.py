import datetime as dt

HEIGHT = 175
WEIGHT = 75
FORMAT = '%H:%M:%S'
STEP_M = 0.65
TRANSFER_COEFF = 1000
K_1 = 0.035
K_2 = 0.029
storage_data = {}
calories_list = []

def accept_package(package):
    storage_data_internal = {}
    if check_correct_data(package[1]) and check_correct_time(package[0]):
        storage_data_internal[package[0]] = package[1]
    else:
        return 'Получен поврежденный пакет данных'
    storage_data.update(storage_data_internal)
    steps = get_step_day(storage_data)
    dist = get_distance(steps)
    calories_list.append(get_spent_calories(package[1], package[0]))
    show_message(package[0], steps, dist, get_calories_day(calories_list), get_achievement(dist))

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
    return True


def check_correct_time(time):
    return True


def get_step_day(dict_steps):
    return sum(step for step in dict_steps.values())


def get_calories_day(calories_list):
    return sum(step for step in calories_list)


def get_distance(steps):
    return int((steps * STEP_M) / TRANSFER_COEFF)


def get_spent_calories(dist, current_time):
    if len(storage_data) != 1:
        time_list = list(storage_data.keys())
        previous_time = time_list[len(storage_data) - 2]
        T = time_interval_calculation(current_time, previous_time)
        V = get_distance(dist) / round(T)
    else:
        T = time_interval_calculation(current_time, '0:00:00')
        V = get_distance(dist) / round(T)
    return round(K_1 * WEIGHT + (V**2 / HEIGHT) * K_2 * WEIGHT * T * 60)


def time_interval_calculation(current_time, previous_time):
    time_1 = dt.datetime.strptime(current_time, FORMAT)
    time_2 = dt.datetime.strptime(previous_time, FORMAT)
    hour_1 = time_1.hour + time_1.minute / 60 + time_1.second / 3600
    hour_2 = time_2.hour + time_2.minute / 60 + time_2.second / 3600
    return hour_1 - hour_2


def convert(tup, di):
    di = dict(tup)
    return di


def show_message(time, steps, dist, calories, achievement):
    print(f'Время: {time}'
          f'\nКоличество шагов за сегодня: {steps}.'
          f'\nДистанция составила {dist} км.'
          f'\nВы сожгли {calories} ккал.'
          f'\n{achievement}')


package2 = ('9:36:02', 15000)


package3 = ('11:00:02', 15000)


package4 = ('13:13:13', 15000)


accept_package(package2)


accept_package(package3)


accept_package(package4)
