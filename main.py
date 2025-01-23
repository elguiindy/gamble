import time
import random

money = 100
results1 = ["jake won", "mike won"]
results2 = ["canelo won", "floyd won"]
results3 = ["logan", "conor"]

print("Hello, Which fight do you want to gamble on?")

fight = input("1.Jake Paul VS Mike Tyson \n2.Canelo VS Mayweather \n3.Logan paul VS Conor Mcgregor, \n4.exit the code : ")
if fight == "1":
    while True:
        whotobeton1 = input("ok who do you wanna bet on (jake/mike)").strip().lower()
        if whotobeton1 == "jake":
            howmuch1 = int(input("how much do you wanna bet?: "))
            if howmuch1 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch1 <= money:
                print(f"you have betted {howmuch1} dollars on jake")
                whowon1 = random.choice(results1)
                print(f"the results is {whowon1}")
                if "jake" in whowon1:
                    print("you won the bet")
                    money += howmuch1
                else:
                    print("you lost the bet")
                    money -= howmuch1
                print(f"your remaining money is {money}")
            elif howmuch1 > money:
                print("sorry you're too poor for that, bet lower")
            else:
                print("please enter amount of money you want to bet")
        elif whotobeton1 == "mike":
            howmuch1 = int(input("how much do you wanna bet?:"))
            if howmuch1 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch1 <= money:
                print(f"you have betted {howmuch1} dollars on mike")
                whowon1 = random.choice(results1)
                print(f"the results is {whowon1}")
                if "mike" in whowon1:
                    print("you won the bet")
                    money += howmuch1
                else:
                    print("you lost the bet")
                    money -= howmuch1
                print(f"your remaining money is {money}")
            elif howmuch1 > money:
                print("sorry you're too poor for that, bet lower")
            else:
                print("please enter amount of money that you would like to bet")
        else:
            print("please enter either 'jake' or 'mike' nigga.")
        break

elif fight == "2":
    while True:
        whotobeton2 = input("ok who do you wanna bet on (canelo/floyd)?").strip().lower()
        if whotobeton2 == "canelo":
            howmuch2 = int(input("How much do you wanna bet?: "))
            if howmuch2 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch2 <= money:
                print(f"you better {howmuch2} on canelo")
                whowon2 = random.choice(results2)
                print(f"the winner is {whowon2}")
                if "canelo" in whowon2:
                    print("you won the bet")
                    money += howmuch2
                else:
                    print("you lost the bet")
                    money -= howmuch2
                print(f"your remaining money is {money}")
            elif howmuch2 > money:
                print("sorry you're too poor for that, bet lower")
            else:
                print("please enter amount of money you want to bet")
        elif whotobeton2 == "floyd":
            howmuch2 = int(input("how much do you want to bet?: "))
            if howmuch2 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch2 <= money:
                print(f"you bet {howmuch2} on floyd")
                whowon2 = random.choice(results2)
                print(f"the result is {whowon2}")
                if "floyd" in whowon2:
                    print("you won the bet")
                    money += howmuch2
                else:
                    print("you lost the bet")
                    money -= howmuch2
                print(f"your remaining money is {money}")
            elif howmuch2 > money:
                print("sorry you cant your too poor, bet lower")
            else:
                print("please enter amount of money you'd like to bet")
        else:
            print("please enter either canelo or floyd nigga.")
        break

elif fight == "3":
    while True:
        whotobeton3 = input("ok who do u wanna bet on (logan/conor): ").strip().lower()
        if whotobeton3 == "logan":
            howmuch3 = int(input("how much do you wanna bet?: "))
            if howmuch3 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch3 <= money:
                print(f"you have betted {howmuch3} on logan")
                whowon3 = random.choice(results3)
                print(f"the result is {whowon3}")
                if "logan" in whowon3:
                    print("you won the bet")
                    money += howmuch3
                else:
                    print("you lost the bet")
                    money -= howmuch3
                print(f"your remaining money is {money}")
            elif howmuch3 > money:
                print("sorry your too poor for that, bet lower")
            else:
                print("please enter amount of dollars you want to bet.")
            break
        elif whotobeton3 == "conor":
            howmuch3 = int(input("how much do you wanna bet?: "))
            if howmuch3 <= 0:
                print("Please enter a valid positive amount.")
            elif howmuch3 <= money:
                print(f"you have betted {howmuch3} on conor")
                whowon3 = random.choice(results3)
                print(f"the result is {whowon3}")
                if "conor" in whowon3:
                    print("you won the bet")
                    money += howmuch3
                else:
                    print("you lost the bet")
                    money -= howmuch3
                print(f"your remaining money is {money}")
            elif howmuch3 > money:
                print("sorry your too poor for that, bet lower")
            else:
                print("please enter amount of dollars you want to bet.")
            break
        else:
            print("please enter either 'logan' or 'conor' nigga.")

elif fight == "4":
    exit()
else:
    print("please enter either 1 , 2 , 3, or 4")
