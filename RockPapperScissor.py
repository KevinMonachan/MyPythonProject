import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images=[rock,papper,scissor]

while True:
 print("Enter your choice \n0- rock \n1-paper \n2-scissor")
 user_choice=int(input("Enter your choice: "))
 if user_choice >=0 and user_choice <= 2:
    print("User chose:")
    print(game_images[user_choice])

 computer_choice=random.randint(0,2)
 print("Computer chose:")
 print(game_images[computer_choice])


 if user_choice == computer_choice:
    print("It's a draw!")
 elif user_choice >= 3 or user_choice < 0:
    print("You typed invalid number. you loose!")    
 elif user_choice == 0 and computer_choice == 2:
    print("You win!")
 elif user_choice == 2 and computer_choice == 0:
    print("You loose!")         
 elif user_choice > computer_choice:
    print("You win!")
 elif computer_choice > user_choice:
    print("you loose!")
         
 ans=input("Do you want to play again!(y/n):").lower()
 if ans == "n":
    break

print("Thanks for playing!")