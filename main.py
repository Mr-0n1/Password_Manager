# -- Password Administrator V.1
# Initial version, with 3 basic functions

from gen_password import pass_gen

MENU = """
Password Administrator V.1
Made by a  Very H0rny 0n1.
/------------------------/

1 - Generate Password.
2 - Save New Credentials.
3 - Check Credentials.

Select Option: 
"""

def run():
    
    option = int(input(MENU))
    if option == 1:
        # call func
        pass_len = int(input("Insert password length: "))
        print(f"Your new password is: {pass_gen(pass_len)}")
    elif option == 2:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        website = input("Enter the name of the domain (or URL if you want): ")
        
        file = open("file.txt", "a")
        file.write(f"{username}||{password}||{website}\n")
        file.close()
    elif option == 3:
        file = open("file.txt", "r")
        print("\n| Username | Password | Domain |\n")
        for i in file:
            row = i.split("||")
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
    else:
        print("Insert Valid Option. \n")
        run()
        

if __name__ == '__main__':
    run()