import numpy as np

def double_precision():
    s,c,i,f = 0,0,0,0
    exponent = 10000000111
    fraction = "111010111001000000000000000000000000000000"

    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * (2**i)
        exponent = exponent//10
        i +=1 
    i = 1
    for k in fraction:
        f = f + int(k) * (0.5 **i)
        i += 1
    print(((-1)** s)*(2**(c-1023))*((1+f)))
    return 


def three_digit_round():
    number = 491.5625
    print(round((number/1000),3))
    return

def three_digit_chop():
    number = 491.5625
    print(((int)(str(number)[:3]))/1000)
    return

def question_four():
    number = 491.5625
    rounded_number = 492
    print(abs(number-rounded_number))
    print(abs((number-rounded_number)/number))
    return 

def question_five():
    def series(x,k:int):
        return ((-1)**k) * ((x**k)/(k**3))
    
    minimum_error = 0.0001
    current =  1
    while(abs(series(1,current)) > minimum_error):
        current += 1

    print(current - 1)

def Bisection_Root(val_a,val_b,minimum_error,f:callable):
    
    left = min(val_a,val_b)
    right = max(val_a,val_b)

    max_num = 200
    current = 0

    while(abs(left-right) > minimum_error and current < max_num):
        current += 1
        p = (left+right)/2

        l1 = f(left)
        lmid = f(p)
        if(l1 < 0 and lmid > 0):
            right = p
        else:
            left = p
    return current

def Newton_Raphson(initial,minError,function_f,function_f_p):
    max_num = 200
    current = 0

    next, previous = initial, initial
    
    while(current < max_num):
        if(function_f_p(previous) != 0):

            next = previous - function_f(previous)/function_f_p(previous)

            if(abs(previous - next) < minError):
                return current + 1
            
            previous = next
            current += 1
        else:
            return -1
    return -2

def question_six():
    def function_f(x):
        return x**3 + 4*(x**2) - 10
    def function_f_p(x):
        return 3*(x**2) + 8*x

    mininimum_error = 0.0001
    val_a = -4
    val_b = 7

    Newton = Newton_Raphson(val_a,mininimum_error,function_f,function_f_p)
    Bisection = Bisection_Root(val_a,val_b,mininimum_error,function_f)

    print(Bisection)
    print()
    print(Newton)



#question 1
double_precision()
print()
#question 2
three_digit_chop()
print()
#question 3
three_digit_round()
print()
#question 4
question_four()
print()
#question 5
question_five()
print()
#question 6
question_six()
