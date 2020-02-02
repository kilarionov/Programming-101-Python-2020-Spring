'''
    Hack Bulgaria,
    “Programming 101 with Python” започващ на 24.02.2020
    задача "Сензори за мръсен въздух"

    от Кирил Иларионов,
    k.ilarionov@gmail.com
    02/02/2020
'''
def sensors() :
    '''
    https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/tree/master/Application/1.Sensors
    '''

    try:
        file_name = input("Filename: ")
        sensors_file = open(file_name, 'r')
    except FileNotFoundError as e :
        print(f"{e.filename} - Not Found")
        return

    try:
        neighbours_distance = int(input("Neighbours distance: "))
        max_error = int(input("Max error: "))
    except ValueError as e:
        print("Integer Value Error")
        return

    sensors_list = []

    for line in sensors_file :
        if line == "" :
            continue
        sensor = x, y, value = eval(line)
        sensors_list.append(sensor)

    sensors_file.close()
    not_working_sensors_list = []

    while sensors_list :
        x, y, value = sensors_list[0]
        for sensor in sensors_list :
            x1, y1, value1 = sensor
            is_in_circle = (x - x1) ** 2 + (y - y1) ** 2 <= neighbours_distance ** 2
            is_max_error = abs(value - value1)
            is_not_working = is_in_circle and is_max_error
            if is_not_working :
                not_working_sensors_list.append((x, y))
                not_working_sensors_list.append((x1, y1))
        del sensors_list[0]

    if not not_working_sensors_list :
        print("All sensors are OK.")
    else :
        not_working_sensors_set = set(not_working_sensors_list)
        not_working_sensors_list = sorted(list(not_working_sensors_set))
        print("Please check sensors at: ", end='')
        print(*not_working_sensors_list, sep=', ')


if __name__ == '__main__' :
    # Task 1 - Sensors
    sensors()
