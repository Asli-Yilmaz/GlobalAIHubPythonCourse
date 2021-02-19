import random as rnd
matrix=[]
for i in range(3):
    number=0
    row=[]
    while number!=3:
        n=rnd.randint(0,100)
        if(n<2):continue
        elif(n==2 or n==3 or n==5 or n==7):
            row.append(n)
            number+=1
        elif(n%2==0 or n%3==0 or n%5==0 or n%7==0):continue       
        else:
            row.append(n)
            number+=1
    matrix.append(row)
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()