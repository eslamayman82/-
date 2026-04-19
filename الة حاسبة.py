name1=float(input("enter farist namber : "))
oper=input("choosean operation  (+,-,*,/,%) :  ")
name2=float(input("enter scand namber : "))

if oper== "+": 
    rasult=name1+name2
    print(name1,"+", name2, "=", rasult) 

elif oper== "-": 
    rasult=name1-name2
    print(name1,"-", name2, "=", rasult)   
    
elif oper== "*": 
    rasult=name1*name2
    print(name1,"*", name2, "=", rasult)  

elif oper== "/": 
    rasult=name1/name2
    print(name1,"/", name2, "=", rasult)  

elif oper== "%":
    rasult=name1%name2
    print(name1,"%", name2, "=", rasult)  
