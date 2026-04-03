
choose=int(input('1.enter_data , 2.read_data ,  3.max_marks ='))
if(choose<1 or choose>5):
   print('NOT_FOUND')
elif(choose==1):
 with open('chaube.txt','a') as f:
   name=str(input('enter name = '))
   marks=int(input('enter marks = '))
   f.write(name + "," + str(marks) + '\n')
elif(choose==2):
   with open('chaube.txt','r') as f:
    print(f.read())
elif(choose==3):
    max_marks = 0
    topper = ''
    with open('chaube.txt','r')  as f:
     for line in f:
        name, marks = line.strip().split(',')
        marks = int(marks)

        if marks > max_marks:
            max_marks = marks
            topper = name

    print('Topper =', topper)
    print('Marks =', max_marks)
