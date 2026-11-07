'''要求輸出從 1 到 n 的整數序列，並根據整數的整除特性進行字串替換。

遊戲與題目規則

• 3 的倍數：替換為 "Fizz"
• 5 的倍數：替換為 "Buzz"
• 同時是 3 與 5 的倍數（即 15 的倍數）：替換為 "FizzBuzz"
• 其他數字：維持數字本身的字串格式
'''

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%15==0:
            print("FizzBizz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz") 
        else:
            print(i)
        
user=int(input("how many number you want to print?"))    
if user<=0:
    print("error")
fizzbuzz(user)
 
