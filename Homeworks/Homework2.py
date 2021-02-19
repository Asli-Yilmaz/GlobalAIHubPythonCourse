names=list()
grades=list()
info={}
for i in range(5):
    stdName=input("Enter your name:")
    names.append(stdName)
    stdSname=input("Enter your surname:")
    names.append(stdSname)
    while True:
        midterm=int(input("Enter your midterm grade: "))
        if(midterm<0 or midterm>100):
            print("\tPlease enter a value between 0-100.")            
        else:
            grades.append(midterm)
            break
    while True:
        final=int(input("Enter your final grade: "))
        if(final<0 or final>100):
            print("\tPlease enter a value between 0-100.")            
        else:
            grades.append(final)
            break
    while True:
        hmwrk=int(input("Enter your homework grade: "))
        if(hmwrk<0 or hmwrk>100):
            print("\tPlease enter a value between 0-100.")            
        else:
            grades.append(hmwrk)
            break

    avrg=(midterm+final+hmwrk)/3
    info[names[2*i]+" "+names[2*i+1]]=[avrg,midterm,final,hmwrk]
  

orderedInfo={k: v for k, v in sorted(info.items(), key=lambda item: item[1],reverse=True)}
print("\n")
for k,v in orderedInfo.items():
    print(k,v)
    
for k in orderedInfo:
    print("\n %s has the highest grades. Congrats!" %k)
    break
