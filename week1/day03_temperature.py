'''- Ask whether to convert C→F or F→C.
- Ask for the temperature.
- Use two functions: `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`.
- Print the result with one decimal place.
- Handle a non-number input without crashing.'''

def celsius_to_fahrenheit(c):
    F=c*9/5+32
    return round(F,1)
def check_int(check):
    try:
        a=int(check)
    except ValueError:
        return
    else:
        return int(a)

def check_float(check):
    try:
        a=float(check)
    except ValueError:
        print(check,"is not a available value")  
    else:
        return float(a)

def fahrenheit_to_celsius(f):
    C=(f-32)*5/9
    return round(C,1)

def mode(u):
    if u==1:
        c=input("input a celsius that you want to convent to fahrenheit:")
        c=check_float(c)
        if c is None:
            return
        else:
            print("celsius to fahrenheit",c,"C->",celsius_to_fahrenheit(c),"F")
    elif u==2:
        f=input("input a fahrenheit that you want to convent to celsius:")
        f=check_float(f)
        if f is None:
            return
        else:
            print("fahrenheit to celsius",f,"F->",fahrenheit_to_celsius(f),"C")

user=input("what mode do you want? 1.C->F  2.F->C:")
user=check_int(user)
if user not in [1,2]:
    print(user,"is not a available mode")
else:
    mode(user)    
