date1 = input ('Enter a date in DD-MM-YYYY format')
date2 = date1.split('-')

print(date2)
list_31 = [1,3,5,7,9,11]
list_30 = [4,6,8,10,12]
check1 = 0

if len(date2[0]) != 2 or not date2[0].isdigit():
    print('Invalid format DD')
    check1 = 1
if len(date2[1]) != 2 or not date2[1].isdigit():
    print('Invalid format MM')
    check1 = 1
if len(date2[2]) != 4 or not date2[2].isdigit():
    print('Invalid format YYYY')
    check1 = 1

if check1 == 0:      
    if (int(date2[1]) in range(1,13)):
            if (int(date2[1]) in list_31):
                m = 31
            elif int(date2[1]) == 2:
                a = int(date2[2])
                if (a%4) == 0:
                    if (a % 100) == 0:
                        if (a % 400) == 0:
                           m = 29
                        else:
                           m = 28
                    else:
                       m = 29
                else:
                   m = 28
            else:
                m = 30
            m+=1;
            if (int(date2[0]) in range(1,m)):
                if (int(date2[2]) in range(1,2020)):
                    print('Valid date!')
                else:
                    print('Invalid Year!')
            else:
                print('Invalid date')
    else:
        print('Invalid Month!')





