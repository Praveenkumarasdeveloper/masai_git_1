### secreat_number = 72 
print("Welcome to the number guessing game !!!")
print("Guess the number between 1 to 100")

secreat_number = 72 

for i in range(0,5):
    
    user_input = int(input("Enter the number :"))
    if user_input < 1 or user_input > 100:
        print("Invaild number! Please enter the Number between 1 TO 100 ")
        
    elif user_input > secreat_number:
        print("Your number is higher")
        
    elif user_input < secreat_number:
        print("Your number is lesser")
        
    else:
        print("Your Guessing number is correct!!!")
        break

if secreat_number == user_input:
    print(f"Congratulation, you guessed the number {secreat_number} in {i} attempts") 
else:
    print("Sorry!! Your all trials are excisesed")

    