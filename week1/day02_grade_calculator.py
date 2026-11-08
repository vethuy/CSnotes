'''- Ask for a score from 0 to 100.
- Print `A` for 90+, `B` for 80–89, `C` for 70–79, `D` for 60–69, `F` below 60.
- Reject scores below 0 or above 100 with a clear message.
- Use a function `grade(score)` that returns the letter.

Test these inputs: `95`, `80`, `69`, `0`, `101`, `-5`.
'''

def grade(score):
    if score<0 or score>100:
        return 'reject'    
    elif score>=90:
        return 'A'
    elif score<90 and score>=80:
        return 'B'
    elif score<80 and score>=70:
        return 'C'
    elif score<70 and score>=60:
         return 'D'
    else:
         return 'F'
a=int(input("how many score do you got?"))
print(grade(a)) 

'''i  can print a function value'''  

'''stronger version'''
def stronggrade(score):
    if not 0<=score<=100:
        return f"{score} is not an acceptable score"
    elif score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'

def user() :
    try :
        score=int(input("Enter your score:")) 
    except ValueError:
        print( score,"is not an acceptable score")
    print(stronggrade(score))

user()
