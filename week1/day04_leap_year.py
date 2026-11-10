'''Requirements:

- Ask for a year.
- Print whether it is a leap year.
- Use a function `is_leap(year)` that returns `True` or `False`.

Rule:

- Divisible by 4 → leap,
- except divisible by 100 → not leap,
- except divisible by 400 → leap.'''
def check_int(check):
    try:
        a=int(check)
    except ValueError:
        return
    else:
        return a

def is_leap(year):
    if year%4==0:
        if not year%100==0:
            return 'True'
        elif year%400==0:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'        
    

raw=input('input a year:')
user=check_int(raw)
if user is None:
    print('This is not an available year')
else:
    print(is_leap(user))        

   