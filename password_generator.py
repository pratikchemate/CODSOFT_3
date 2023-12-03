import random
import string
b = 0
while(True):
    print("\n\tPASSWORD GENERATOR\n")
    print("\tSelect complexity of password")
    print("\n\t1) High complexity")
    print("\n\t2) Medium complexity")
    print("\n\t3) Low complexity")
    print("\n\t4) Exit")
    ch = int(input("\n\t Choose an option:"))
    

    chl = ''
    a = 1
    if (ch==1):
        chl += string.ascii_letters+string.punctuation+string.digits

    elif (ch==2):
        chl += string.ascii_letters+string.digits 

    elif (ch==3):
        chl += string.ascii_letters 

    elif (ch==4):
        a = 0
        break

    else:
        print("Select correct option!")
        a = 0
    
    len = int(input("\n\tEnter desired length of password:"))
    password = ''.join(random.choice(chl) for i in range(len))

    if(a==1):
        print("\n\tPassword is: "+password+"\n")
