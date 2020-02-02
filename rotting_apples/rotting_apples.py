'''
    Hack Bulgaria,
    “Programming 101 with Python” започващ на 24.02.2020
    задачи за Кандидатстване

    от Кирил Иларионов,
    359 878 719 304, k.ilarionov@gmail.com
    02/02/2020
'''

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
    # Task 3 - Rotting Apples
    rotting_apples()
