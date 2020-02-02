'''
    Hack Bulgaria,
    “Programming 101 with Python” започващ на 24.02.2020
    задача "Правилни скоби"

    от Кирил Иларионов,
    k.ilarionov@gmail.com
    02/02/2020
'''

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


if __name__ == '__main__' :
    # Task 2 - Correct Brackets
    print(correct_brackets())
