'''- Ask for a score from 0 to 100.
- Print `A` for 90+, `B` for 80–89, `C` for 70–79, `D` for 60–69, `F` below 60.
- Reject scores below 0 or above 100 with a clear message.
- Use a function `grade(score)` that returns the letter.

Test these inputs: `95`, `80`, `69`, `0`, `101`, `-5`.
'''

def grade(score):
    if score<0 or score>100:
        return f"{score} is not valid score (between 0~100)" 
    elif score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif  score>=70:
        return 'C'
    elif score>=60:
         return 'D'
    else:
         return 'F'
a=input("how many score do you got?")
try:
    score=int(a)
except:
    print(a,'is not a valid score')
else:

    print(grade(int(a)))




