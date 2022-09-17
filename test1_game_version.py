import time

print()
print('Bugged Code')
time.sleep(1)
print('-----------')
print()
print('1.   a = 33')
print('2.   b ='+'"'+'33'+'"')
print('3.   if b > a :')
print('4.      print('+'b is greater than a'+')')
print('5.   elif b == a :')
print('6.      print('+'a and b are equal'+')')
print()
time.sleep(3)
print('-----------')
print()



view_error = input('WHICH LINE HAS AN ERROR(enter line no.) ?  >>  ')
print()


if(view_error == '2'):
    print('Correct')
else: print('Incorrect')
print()


time.sleep(2)
print('----------')
print()
print('The error was -- ')
print(' line 2   ...  b is a string(str) not an integer(int) ... '+'>'+' or'+ '=='+'are not supported between str and int')
print()
print('----------')
print()


view = input('View debugged code (y/n) ?  >>  ')
if(view == 'y'):
    print()
    print('-----------')
    print()
    print('1.   a = 33')
    print('2.   b ='+'int('+'"'+'33'+'"'+')')
    print('3.   if b > a :')
    print('4.      print('+'b is greater than a'+')')
    print('5.   elif b == a :')
    print('6.      print('+'a and b are equal'+')')
    print()  
    time.sleep(1)
    print('-----------')
    print()
    print('Output')
    print()
    a = 33
    b = int(33)
    if b > a :
        print('b is greater than a')
    elif b == a :
        print('a and b are equal')



time.sleep(1)
print()
print('----------')
print()  
print('Thank you for playing')
print()
