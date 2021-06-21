import sys
print("""
 _____________________
|  _________________  |
| | GK           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
        """)


def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div
        }
def operator_select(a, b):
    num1, num2 = a, b
    print("+, -, *, /")
    op = input(("Pick an operator: "))
    function = operations[op]
    res = function(num1, num2)
    return res, op

def continue_cal(prev_result):
    next_num = int(input("Enter new number: "))
    result, ope = operator_select(prev_result, next_num)
    print(f"{prev_result} {ope} {next_num} = {result}")
    flag = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'e' to exit: ")
    if flag == 'y':
        continue_cal(result)
    elif flag == 'n':
        new_cal()
    else: 
        sys.exit()

def new_cal():
        
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    res, op = operator_select(num1, num2)
    print(f"{num1} {op} {num2} = {res}")

    flag = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation, 'e' to exit: ")
    if flag == 'y':
        continue_cal(res)
    elif flag == 'n':
        new_cal()
    else:
        sys.exit()

new_cal()
