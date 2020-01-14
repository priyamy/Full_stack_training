import random
import time
print ('The Game starts!!!')
print()
ply_list = [1,2]
first_m =  (random.choice(ply_list)) 

print('Tossing the coin...')
print()
time.sleep(2)
if first_m == 1:
    print ('Player 1 wins the toss!')
    seq1 = 1
    seq2 = 2
    print()
else:
    print('Player 2 wins the toss!')
    seq1 = 2
    seq2 = 1
    print()

list_win = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9], 
    [1,5,9], 
    [3,5,7], 
    [2,5,8],
    [4,5,6] 
    ]

seq_1 = []
seq_2 = []
num_list = [1,2,3,4,5,6,7,8,9]
sum1 = 0
sum2 = 0
flag_2 = 0
ply1=0
ply2=0
ply1_list = []
ply2_list = []
win = 0
while len(num_list)!=0 :
    
    print('Player', seq1, ': choose number between', ",".join(map(str,num_list)))
    num2 = int(input('Enter input: '))

    if num2 in num_list:
        sum1+=num2
        num_list.remove(num2)
        ply1_list.append(num2);
        ply1+=1
##        if ply1>=3:
##            if sum1==6 or sum1 == 15 or sum1==24:
##                print('Player ', seq1, 'wins!')
##                break
        for i in list_win:
##            print(i)
            if(len(set(i) & set(ply1_list)) == 3):
                print('Player ', seq1, 'wins!')
                win = 1 
##                exit()
                break
        if win == 1:
            break                
        print('Player', seq2, ': choose number between', ",".join(map(str,num_list)))
        num2 = int(input('Enter input: '))
        while (num2 not in num_list):
            print('Enter a valid number!')
            print('Player', seq2, ': choose number between', ",".join(map(str,num_list)))
            num2 = int(input('Enter input: '))
        else:
            sum2+=num2
            ply2+=1
            num_list.remove(num2)
            ply2_list.append(num2);
##            if ply2>=3:
##                if sum2==6 or sum2 == 15 or sum2==24:
##                    print('Player', seq2, 'wins!')
##                    break
            for i in list_win:
                if(len(set(i) & set(ply2_list)) == 3):
                    print('Player ', seq2, 'wins!')
                    win=1
##                    exit()
                    break
            if win == 1:
                break
    else:
        if num2 not in num_list:
            print('Enter a valid number!')
            continue

    




