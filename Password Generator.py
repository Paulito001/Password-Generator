# Password Generator

# A program that can create one or multiple unique passwords that match the users Criteria
# Criteria - Min length (at least 6 characters), highest length (at most 15 characters) (The password will have a length somewhere between these values)

import random 
# Function creates one password
def generate_password(length):

    # Formula - Combo of alphabetic, numeric, and punctuation characters
    #           3 min                2 min        1 min 

    # Lists, which will soon contain all choosen password chars
    selected_alpha = []
    selected_numeric = []
    selected_punct = []

    # List with all possible...

    # Alphanbetic characters
    possible_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']

    # Numberic Chars
    possible_numeric = ['0','1','2','3','4','5','6','7','8','9']

    # Punctuation Chars
    possible_punct = ['!','@','#','$','%','^','&','*','(',')']

    upper = -1 # Var to determine whether or not to uppercase
    letter = '' # Var for keeping track of the current letter in the loop

    # From the start I will ensure I include all the neccessary components
    for i in range(3): 
        letter = random.choice(possible_alpha)

        # 50 % chance of the letter being capitalized (0 -> Stay Lower, 1 -> Convert Upper)
        upper = random.choice([0,1])

        if upper == 1: letter = letter.upper()
        
        # Add letter
        selected_alpha.append(letter) 

    # Choosing numeric/punctuation characters
    for i in range(3):
        # First two itterations are numeric
        if i in [0,1]: selected_numeric.append(random.choice(possible_numeric))

        # Last is punctuation
        else: selected_punct.append(random.choice(possible_punct))
    
    # Now the password has 6 characters selected, the rest will be randomized 
    # All remaining values have a 1/3 chance of being choosen 

    # 'a' = alpha, 'n' = numeric, 'p' = punctuation

    # Only do this if the user would like more than 6 characters 
    if length > 6:
        # Continue itterating for the remaining length leftover
        for i in range(0, length - 6):
            char_type = random.choice(['a','n','p'])

            # Going to re-use the upper & letter variable
            if (char_type == 'a'): 
                letter = random.choice(possible_alpha)
                upper = random.choice([0,1])

                if upper == 1: letter = letter.upper()

                selected_alpha.append(letter)

            elif (char_type == 'n'): selected_numeric.append(random.choice(possible_numeric))
            else: selected_punct.append(random.choice(possible_punct))
    
    # Now all characters have been choosen 
    # I have to make the password to return

    password = ""

    # In the beggining, each char type will have a 1/3 of a chance to be the next letter
    # When one list becomes empty, the remaing two list will have a 1/2 of a chance
    # Then I will add the remaing values in the last list till it is empty

    char_types = ['a', 'n', 'p']
    selected_type = ''

    while ((len(selected_alpha) != 0) or (len(selected_numeric) != 0) or (len(selected_punct) != 0)):

        # Inner loop breaks once at least one loop is empty
        while ((len(selected_alpha) >= 1) and (len(selected_numeric) >= 1) and (len(selected_punct) >= 1)):
            
            # Choosing a rand type
            selected_type = random.choice(char_types)

            # Once type is selected, I will go to the beggining of the associative list, remove it, and add it to the password
            if (selected_type == 'a'):
                password += selected_alpha[0]; selected_alpha.remove(selected_alpha[0])

            elif (selected_type == 'n'):
                password += selected_numeric[0]; selected_numeric.remove(selected_numeric[0])

            else:
                password += selected_punct[0]; selected_punct.remove(selected_punct[0])
        
        # Figure out which is empty
        # Continue itterating untill the next list is empty
        if (len(selected_alpha) == 0):
            # Numeric and Punctuation Remain
            while ((len(selected_numeric) >= 1) and (len(selected_punct) >= 1)):
                
                char_types = ['n','p']
                selected_type = random.choice(char_types)

                if (selected_type == 'n'): 
                    password += selected_numeric[0]; selected_numeric.remove(selected_numeric[0])
                else:
                    password += selected_punct[0]; selected_punct.remove(selected_punct[0])

        elif (len(selected_numeric) == 0):
            # Alphabetic and Punctuation Remain
            while ((len(selected_alpha) >= 1) and (len(selected_punct) >= 1)):

                char_types = ['a','p']
                selected_type = random.choice(char_types)

                if (selected_type == 'a'): 
                    password += selected_alpha[0]; selected_alpha.remove(selected_alpha[0])
                else:
                    password += selected_punct[0]; selected_punct.remove(selected_punct[0])
        else:
            # Alphabetic and Numeric Remain
            while ((len(selected_alpha) >= 1) and (len(selected_numeric) >= 1)):
                
                char_types = ['a','n']
                selected_type = random.choice(char_types)

                if (selected_type == 'n'): 
                    password += selected_numeric[0]; selected_numeric.remove(selected_numeric[0])
                else:
                    password += selected_alpha[0]; selected_alpha.remove(selected_alpha[0])
        
        # Now there is one remaining list
        # Figure out what list that is, then I can leave the remaining elements in the leftover list
        # Since there is no need to delete and it would cost exta operations

        if (len(selected_alpha) >= 1):
            for e in selected_alpha: password += e

        if (len(selected_numeric) >= 1):
            for e in selected_alpha: password += e

        if (len(selected_punct) >= 1):
            for e in selected_alpha: password += e
        
        return password

def display_menu():
    print(" ________________________ ")
    print("|                        |")
    print("| A. One Password        |")
    print("| B. Multiple Passwords  |")
    print("|________________________|")

# Main Program 

print("Welcome, you have started the Password Generator Program.\n")
print("Select from the menu choices below...\n")
display_menu()


# Note: After the first itteration, I will notify the user that they can type q to quit 

# Variable to keep track of the password length the user would like
user_length = 0
program_runs = 0

menu_choice = ''
while (menu_choice not in ['q', 'Q']):

    if (program_runs == 0): menu_choice = input("\nMenu Choice: ")
    else: menu_choice = input("\nChoose again from the menu: ")

    # Error exception to choice to make sure it is applicable (a/A, b/B, q/Q)

    more_than_one = False # Var to check to see if choice is invalid > 1 times
    times_inccorect = 0 # Var to check the total number of times the user entered a invalid choice.
                        # I'm doing this for the spacing 

    while (menu_choice not in ['a', 'A', 'b', 'B', 'q', 'Q']):
        times_inccorect += 1

        if (not more_than_one):
            menu_choice = input("\nPlease choose a valid option.\nRefer to the menu above above\n\nChoice: ")
            more_than_one = True
        else:
            # First time inccorect, I will seperate the two prompts by a space
            if (times_inccorect == 2): print()
            
            menu_choice = input("Re-enter your choice: ")

    # Make sure the user would not like to quit before extracting the password length
    if menu_choice not in ['q','Q']:

        # Using conditions, which determine the prompt to be shown (password OR passwords)
        if (menu_choice in ['a', 'A']): user_length = int(input("\n(6 - 15) How long would you like your password to be? "))
        else: user_length = int(input("\n(6 - 15) How long would you like your passwords to be? "))

        # Error exception to ensure password length is with the valid range
        more_than_one = False
        times_inccorect = 0
        while ((user_length < 6) or (user_length > 15)):
            times_inccorect += 1

            if (not more_than_one):
                user_length = int(input("\nPlease make sure you type a length within the range from 1 - 15: "))
                more_than_one = True
            else:
                if (times_inccorect == 2): print()
                user_length = int(input("Length: "))
        
    
    # Check to see if the user would like to display ONE or Mult. Passwords

    # ONE
    if menu_choice in ['a', 'A']:
        print("\nYour generated password is", generate_password(user_length))

    elif menu_choice in ['b', 'B']:
        num_passwords = 0

        num_passwords = int(input("\n(80 max.) How many passwords would you like to create? "))

        while ((num_passwords > 80) or (num_passwords < 2)):
            if (num_passwords > 80): num_passwords = int(input("\nPlease make sure the number doesn\'t go above 80: "))
            else: num_passwords = int(input("\nPlease make sure you include at least two passwords: "))

        # Display all the passwords below (Doing this numerically)

        for i in range(1, num_passwords + 1):

            if i == 1: print() # Spacing
            print(str(i) + '. ' + generate_password(user_length))

    program_runs += 1
print("\nThank you for using my Password Generator Program!")
print("Have a Good Day!")

input()