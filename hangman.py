print("WELCOME TO HANGMAN")
import random
lives=6
placeholder=""
word_list=["camel","apple","orange"]
choice=random.choice(word_list)
x=len(choice)
for i in range(x):
    placeholder += "_"
print(placeholder)

correct_order=[]
game_over=False

while not game_over:
    guess=input("guess a letter: ").lower()
    display = " "
    for i in choice:
        if i == guess:
           display += guess
           correct_order.append(guess)
        elif i in correct_order:
           display += i   
        else: 
           display += "_"

    print(display)

    if guess not in choice:
        lives -=1
        if lives == 0:
            game_over=True
            print("you loose")
    print(lives)         
    if '_'not in display:
        game_over=True
        print("you win")