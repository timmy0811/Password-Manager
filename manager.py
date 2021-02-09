import os, sys, time, random
from cryptography.fernet import Fernet

def newEntry():
    new_entry = input("Create new Entry: ")
    #all_entries.append(None)
    #all_entries[len(all_entries) - 1] = new_entry

    return new_entry

def newUser():
    new_user = input("Create new User: ")
    #entry_user.append(None)
    #entry_user[len(entry_user) - 1] = new_user

    return new_user

def newPassword():
    new_password = input("Create new Password: ")
    #entry_password.append(None)
    #entry_password[len(entry_password) - 1] = new_password

    return new_password

def mainMenu():
    print(" [1] Create new entry \n [2] Access existing entry \n [3] Delete existing entry \n [4] View all entries \n [5] Clear all \n [6] Generate save password \n ----Always close programm in Menu----")
    action = int(input())
    

    return action

def getlen():
    file = open("save_log.txt", "r")
    count = len(file.readlines())
    file.close()

    return count

def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loadKey():
    return open("key.key", "rb"). read()

def encryptFile(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
    
    file.close()

def decryptFile(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    file.close

def drawScreen():
    os.system("cls")
    print("Password manager by timmy0811\n-------------------------------\n")

all_entries = []
entry_user = []
entry_password = []

if(os.path.exists("key.key") == False):
    writeKey()

key = loadKey()
f = Fernet(key)

while(True):

    drawScreen()
    action = mainMenu()

    if(action == 1):

        if(os.path.exists("save_log.txt") == True):
            file = open("save_log.txt", "r")
            encr_file = file.readline()
            if(encr_file != "decrypted\n"):
                decryptFile("save_log.txt", key)
            
            file.close()

        drawScreen()

        save_exist = os.path.exists("save_log.txt")
        file = open("save_log.txt", "a")

        if(save_exist == False): file.write("decrypted\n")
        file.write(newEntry() + "&")
        file.write(newUser() + "&")
        file.write(newPassword() + "& \n")

        print("New entry has been added!")
        time.sleep(1)

        file.close()
        encryptFile("save_log.txt", key)

    elif(action == 2):
        
        if(os.path.exists("save_log.txt") == True):
            file = open("save_log.txt", "r")
            encr_file = file.readline()
            if(encr_file != "decrypted\n"):
                decryptFile("save_log.txt", key)
            
            file.close()

        drawScreen()
        entry_acc = input("Enter entry to access: ")

        file = open("save_log.txt", "r")
        line = 0
        
        do_loop = True
        while(do_loop):
            s = file.readline()
            line_content = s.split('&')
            
            if entry_acc in line_content:
                line_found = line
                do_loop = False
            line += 1

        file.close()

        file = open("save_log.txt", "r")  
        lines = file.readlines()

        entry_data = (lines[line_found]).split('&')

        print("Entry:       " + entry_data[0])
        print("User:        " + entry_data[1])
        print("Password:    " + entry_data[2])

        file.close()

        time.sleep(1)
        input("Press Enter to continue...")
        encryptFile("save_log.txt", key)

    elif(action == 3):

        if(os.path.exists("save_log.txt") == True):
            file = open("save_log.txt", "r")
            encr_file = file.readline()
            if(encr_file != "decrypted\n"):
                decryptFile("save_log.txt", key)
            
            file.close()

        drawScreen()
        entry_del = input("Enter entry to delete: ")
        file = open("save_log.txt", "r")
        line = 0
        
        do_loop = True
        while(do_loop):
            s = file.readline()
            l = s.split('&')
            
            if entry_del in l:
                line_del = line
                do_loop = False
            line += 1
        
        a_file = open("save_log.txt", "r")
        lines = a_file.readlines()
        a_file.close()

        del lines[line_del]

        del_file = open("save_log.txt", "w+")

        for line in lines:
            del_file.write(line)

        del_file.close()

        print("Entry has been deleted!")
        time.sleep(1)
        encryptFile("save_log.txt", key)

    elif(action == 4):

        if(os.path.exists("save_log.txt") == True):
            file = open("save_log.txt", "r")
            encr_file = file.readline()
            if(encr_file != "decrypted\n"):
                decryptFile("save_log.txt", key)
            
            file.close()

        drawScreen()

        line_amount = getlen()
        file = open("save_log.txt", "r")
        
        lines = file.readlines()

        for x in range(line_amount):
            line_string = lines[x]
            line_list = line_string.split('&')

            print("[ " + str(x) + " ]       " + line_list[0])

        file.close()
        time.sleep(1)
        input("Press Enter to continue...")
        encryptFile("save_log.txt", key)

    elif(action == 5):

        drawScreen()
        os.remove("save_log.txt")
        
        print("All entries has been removed")
        time.sleep(1)

    elif(action == 6):

        gen_letterCap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        gen_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        gen_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        gen_symbols = ["!", "§", "$", "%", "&", "/", "=", "+", "#", "-", "<", ">" , ".", ":", ";"]
        gen_all = []

        drawScreen()
        pw_len = input("Lenght of password: ")
        pw_cap = input("Use capital letters? (y/n): ")
        pw_let = input("Use letters? (y/n): ")
        pw_num = input("Use numbers? (y/n): ")
        pw_sym = input("Use symbols? (y/n): ")

        if(pw_cap == "y"): gen_all += gen_letterCap
        if(pw_let == "y"): gen_all += gen_letter
        if(pw_num == "y"): gen_all += gen_number
        if(pw_sym == "y"): gen_all += gen_symbols

        pw_out = ""

        for letter in range(int(pw_len)):
            pw_out += random.choice(gen_all)

        print("Your secure password:    " + pw_out)
        time.sleep(1)
        input("Press Enter to continue...")

    else: print("Wrong input! Retry")

    
    

