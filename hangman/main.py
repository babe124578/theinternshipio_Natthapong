import random

category = ["food&drink.txt","place.txt","people&character.txt"]
wordList = []
use = []
score = 0
attemp = 6
n = 99999999
wrong = " "
playWord = ""
wrongList = []

print("Welcome to HANGMAN.")
print("Please select category from the list")
print(" 1 - food&drink")
print(" 2 - place")
print(" 3 - people&character")

def fileToList(k):
    file = open(category[k-1])
    for i in file:
        wordList.append(i.strip(' ').replace('\n',''))
def swapRandom(lst):
    idx = range(len(lst))
    idx1, idx2 = random.sample(idx, 2)
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
            
try:
    n = int(input("Insert integer between 1 to " \
                  +str(len(category))+" here - "))
except ValueError:
    print("Invalid input, please enter an integer")
while n > len(category) or n <= 0:
    try:
        n = int(input("Invalid input, please insert integer between 1 to " \
                      +str(len(category))+" - "))
    except ValueError:
        pass
    
fileToList(n)
for i in range(100):
    swapRandom(wordList)
for i in range(len(wordList[0])):
    if wordList[0][i].islower():
        use.append(wordList[0][0:i-1]+' ')
        use.append(wordList[0][i:])
        break

for i in use[0]:
    if i.isalpha()==True:
        playWord += '-'
    else:
        playWord += i

print("")
print("Hint: "+use[1])
print(playWord + "   score "+str(score)+" , "+str(attemp)+" wrong attemp left , wrong guessed ")

while attemp>=0:
    checker='NotPass'
    while checker=='NotPass':
        char = input("Guess the character here : ")
        if len(char)!=1:
            print("Please guess only 1 character")
        elif char.isalpha()==False:
            print("Please guess an alphabet")
        else:
            checker='Pass'
    tru = 0
    for i in range(len(use[0])):
        if use[0][i]==char.upper() and playWord[i]=='-':
            temp = playWord
            playWord = temp[0:i]+char.upper()+temp[i+1:]
            tru += 1
        elif (use[0][i]==char.upper() and playWord[i]!='-') or char.upper() in wrongList:
            print("You already type this alphabet")
            break;
    if use[0][i]==char.upper() and playWord[i]!='-' or char.upper() in wrongList:
        continue
            
    if tru == 0:
        attemp -= 1
        wrong += char.upper() + ' '
        wrongList.append(char.upper())
    else:
        score += attemp
    if attemp<0:
        print("You lose")
        print("The word is "+use[0])
        print("Your score is "+str(score)+" points")
        break
    if playWord == use[0]:
        print("You win")
        print("Your score is "+str(score)+" points")
        break
    else:
        print(playWord)
        print(playWord+ "   score "+str(score)+" , "+str(attemp)+" wrong attemp left , wrong guessed "+wrong)

print()
input("Press ENTER to exit ... ")
