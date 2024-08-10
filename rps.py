from random import choice

score = {'win' : 0 , 'loss' : 0 , 'draw' : 0}


while(True):
    list1 = ["r","p","s"]
    user = input("Rock , Paper , Scissor ! : ").lower()
    if(user == 'q'):
        break
    if user not in list1:
        continue
    comp = choice(list1)
    mydict = {'r':'rock','p':'paper','s':'scissor'}

    print(f"Computer picked {mydict[comp]}" )

    if(user == 'p' and comp == 'r') or (user == 's' and comp == 'p') or (user == 'r' and comp == 's'):
        score['win'] += 1
        print("You Win !")
    elif user == comp:
        score['draw'] += 1
        print("Draw !")       
    else:
        score['loss'] += 1
        print("You Lose !")   
        

print(f"Win : {score['win']}\nLoss : {score['loss']}\nDraw : {score['draw']}")

