import random

num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['!','@','#',"$",'%','^',"&",'*','(',")",'~','`',',','.','/']
letter = ['a','b',"c",'d','e',"f",'g','h',"i",'j','k',"l",'m','n',"o",'p','q',"r",'s','t',"u",'v','w',"x",'y','z']

output = []
#something that can mix up this list and put it in a new list
random.shuffle(num)
random.shuffle(sym)
random.shuffle(letter)
new_list = num + sym + letter 
new_list = new_list * 9999

#length of the password
times = int(input("The length of your password: "))
while times > 0:
    random.shuffle(new_list)
    for i in range(times):
        output.append(new_list[i])
        times -= 1
        
if times == 0:
    output = ''.join(output)
    print(output)

    



