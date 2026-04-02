while True:
    print('---SIMPLE--CALCULATOR---')
    print('1.ADD  ,  2.SUBTRACT,  3.MULTIPLE,  4.DIVISON,  5.EXIT')
    option=int(input('ENTER YOUR CHOICE = '))
    A=float(input('A = '))
    B=float(input('B = '))
    
    if(option==5):
        print('EXIT')
        break
    if(option==1):
        print('ADD =',A+B)
    elif(option==2):
        print('SUBTRACT =',A-B)
    elif(option==3):
        print('MULTIPLE =',A*B)
        if(B==0):
            print('ERROR')
        else:
            print('Divison = ',A/B)
            
    else:
        print('ERRORRRR')