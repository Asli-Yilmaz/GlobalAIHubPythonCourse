#A program that press the prime numbers between 0-500 on the screen with the prime_first function,
#and press the prime numbers between 500-1000 on the screen with the prime_second function.
def prime_first(i):

    if(i<2):return

    elif(i==2 or i==3 or i==5 or i==7 or
       i==11 or i==13 or i==17 or i==19 or
       i==23 or i==29 or i==31):
        print(i,end=",")
        
    elif(i%2==0 or i%3==0 or i%5==0 or i%7==0 or
       i%11==0 or i%13==0 or i%17==0 or i%19==0):return
    else:
        print(i,end=",")
def prime_second(i):
    
    if(i%2==0 or i%3==0 or i%5==0 or i%7==0 or
       i%11==0 or i%13==0 or i%17==0 or i%19==0 or
       i%23==0 or i%29==0 or i%31==0):return
    else:
        print(i,end=",")

for i in range(0,1000):
    if(i<500):
        prime_first(i)
    if(i>=500 and i<1000):
        prime_second(i)
