'''Requirements:

- Ask for two dates in `YYYY-MM-DD` format.
- Print the number of days between them.
- Print which date is earlier.
- Use the `datetime` module.
- Handle invalid date text without crashing.'''

from datetime import datetime
def time_check(check):
    try:
        return datetime.fromisoformat(check)
    except ValueError:
        print(check,'is not YYYY-MM-DD format')
        return
    

def main(a):
    timelist=[]
    while a<2:
        time=input('input a time in YYYY-MM-DD format:')
        parsed= time_check(time)
        if parsed is None:
            return
        else:
            timelist.insert(a,parsed)
            a=a+1
    timebetween=timelist[1]-timelist[0]
    if timelist[1]>timelist[0]:
        print(timelist[0],'is earlier')
    elif timelist[1]<timelist[0]:
        print(timelist[1],'is earlier')
    else:
        print('they are same date')
    print(abs(timebetween.days),'is the numbers of days between them')     
            
    

main(0)


