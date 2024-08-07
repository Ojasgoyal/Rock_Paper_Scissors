from random import choice

score = {'win' : 0 , 'loss' : 0 , 'draw' : 0}
try:
    while(True):
        list1 = ["r","p","s"]
        user = input("Rock , Paper , Scissor ! : ").lower()
        comp = choice(list1)
        mydict = {'r':'rock','p':'paper','s':'scissor'}
        if(user == 'r' and comp == 'p') or (user == 'p' and comp == 's') or (user == 's' and comp == 'r'):
            score['loss'] += 1
            print(mydict[comp])
            print("You Lose !")
        elif user == comp:
            score['draw'] += 1
            print(mydict[comp])
            print("Draw !")
        elif(user == 'p' and comp == 'r') or (user == 's' and comp == 'p') or (user == 'r' and comp == 's'):
            score['win'] += 1
            print(mydict[comp])
            print("You Win !")
        elif(user == "score"):
            print(f"Win : {score['win']}\nLoss : {score['loss']}\nDraw : {score['draw']}")
        elif(user == 'exit'):
            raise EOFError
        else:
            pass
except EOFError:
    exit("BYE BYE !")

