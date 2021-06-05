#Minion Game

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score, steven_score=0,0
    for i in range(len(string)):
        score = len(string)-i
        if string[i] in vowels:
            kevin_score += score
        else:
            steven_score += score
    if kevin_score > steven_score:
        print("Kevin", kevin_score)
    elif kevin_score < steven_score:
        print("Steven", steven_score)
    else:
        print("Draw")
        
string =input(" ")
minion_game(string)
    
    
