'''
    Hack Bulgaria,
    “Programming 101 with Python” започващ на 24.02.2020
    задачи за Кандидатстване

    от Кирил Иларионов,
    359 878 719 304, k.ilarionov@gmail.com
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

def correct_brackets() :
    '''
    https://github.com/HackBulgaria/Programming-101-Python-2020-Spring/tree/master/Application/2.CorrectBrackets
    '''
    try :
        checked_string = input()
        tpl = checked_string.replace(")(", "),(")
        tpl = eval(tpl)
        for t in tpl:
            if t != eval('()'):
                return False
        return True
    except SyntaxError as e :
        return False

def rotting_apples() :
    GOOD_APPLE = 'O'
    BAD_APPLE = 'X'
    DAYS_TO_BE_BAD = 3
    nxm = input("Enter the size of the box: ")
    xy = input("Еnter the coordinates of the rotten apples: ")
    days = int(input("After how many days will you come back: "))
    n, m = nxm.split('x')
    n = int(n)  # qty rows
    m = int(m)  # qty cols

    n,m = m,n # Repair Note: Input Format is: colsXrows

    mtrx = {}
    for i in range(n+2) :
        # incl. Border Set Up
        for k in range(m+2) :
            t = f"({i},{k})"
            mtrx[t] = GOOD_APPLE
    xy_list = xy.split() # Initial List Of Bad Apples

    for t in xy_list :
        # Initial Bad Apples Placing
        x, y = eval(t)
        x = int(x)
        y = int(y)
        s = f"({y},{x})" # Repair Note:
        mtrx[s] = BAD_APPLE

    qtyDays = [] # List After a Period (index) Of days
    # 3D Array simulation
    qtyDays.append(mtrx.copy()) # Initial State After 0 Days

    for d in range(1, days, DAYS_TO_BE_BAD) :
        qtyDays.append(qtyDays[-1].copy()) # Previous Status As a Today Starting Point
        if len(qtyDays) > 3:
            del qtyDays[-3]

        for row in range(1, n+1) :
            for col in range(1, m+1) :
                if n == 1 and m == 1 :
                    continue

                # Rotting Process
                is_good_apple = GOOD_APPLE == qtyDays[-2][f"({row},{col})"]
                if is_good_apple :
                    continue

                # To Set Up Bad Apples For Day d
                qtyDays[-1][f"({row},{col})"] = BAD_APPLE
                qtyDays[-1][f"({row-1},{col-1})"] = BAD_APPLE
                qtyDays[-1][f"({row-1},{col})"] = BAD_APPLE
                qtyDays[-1][f"({row-1},{col+1})"] = BAD_APPLE
                qtyDays[-1][f"({row},{col-1})"] = BAD_APPLE
                qtyDays[-1][f"({row},{col+1})"] = BAD_APPLE
                qtyDays[-1][f"({row+1},{col-1})"] = BAD_APPLE
                qtyDays[-1][f"({row+1},{col})"] = BAD_APPLE
                qtyDays[-1][f"({row+1},{col+1})"] = BAD_APPLE

    # Final Result Printing
    for row in range(1, n+1):
        for col in range (1, m+1):
            print(qtyDays[-1][f"({row},{col})"], end='')
        print()

if __name__ == '__main__' :
    # Task 1 - Sensors
    print('\tЗадача "Сензори за мръсен въздух"')
    sensors()

    # Task 2 - Correct Brackets
    print('\tЗадача "Правилни скоби"')
    print(correct_brackets())

    # Task 3 - Rotting Apples
    print('\tЗадача "Гниещи ябълки"')
    rotting_apples()
