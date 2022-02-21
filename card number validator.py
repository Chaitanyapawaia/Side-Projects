cardno= int(input("Enter your card number:"))
cardno=str(cardno)
odd=0
even=0
for i in range(0,len(cardno)):
    if i%2 == 0 :
        a=(int(cardno[i])*2)
        
        if len(str(a))== 1:
            odd=odd+a
           
        else:
            odd=odd+(a-9)
    else:
        even=even+int(cardno[i])
        

t=odd+ even

if t%10== 0:
    print("Your card number", cardno[0:4],cardno[4:8],cardno[8:12],cardno[12:16],"is valid")
else:
    print("Your card number", cardno[0:4],cardno[4:8],cardno[8:12],cardno[12:16],"is invalid")


