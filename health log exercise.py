# Exercise given by Harry from Code with Harry Youtube Channel (HarisAK)
# Coder - Praveen Singh Chauhan (Technology Video Network - Youtube Channel ,
# GAMP Aaryawarti Films - Film Production & Youtube Channel)
# Link of Youtube - https://www.youtube.com/TechnologyVideoNetwork ,
# https://www.youtube.com/gampaaryawartifilms
# Facebook - https://www.facebook.com/praveen13c
# Twitter - https://twitter.com/praveen13c , https://twitter.com/tvnutube
# Linkedin -  https://www.linkedin.com/in/impraveenchauhan

# Programe Starts

# variables assignment

food_health_mem = 0
log_mem_qs = 0
log_ret_qs = 0


def getdate():  # define a function for date
    import datetime
    return datetime.datetime.now()


while True:  # run the program untill user exit

    print("=" * 80)
    print("What do you want to do ")
    log_ret_qs1 = input("[ 0 = Add New Member | 1 = Log | 2 = Retrieve | 3 = Exit or Enter 'exit' ]  > ")

# conditions start from here
    if log_ret_qs1.lower() == "exit":
        print("*" * 160)
        print("  < Exit >  " * 18)
        print("*" * 160)
        break

    if log_ret_qs1 != str(log_ret_qs1).isnumeric():
        try:
            log_ret_qs1 == int(log_ret_qs1)
        except Exception as err_log_ret_qs1:
            print("You have options to enter ")
            print(f"Error = ' {err_log_ret_qs1} '")
            print("*" * 170, "\n")
            print("Application Restart")
            continue

    log_ret_qs = int(log_ret_qs1)
    print("=" * 80)

    if log_ret_qs == 0:
        add_new_mem = input("Enter Name of New Member > ")

        a_n_m = len(add_new_mem)
        if add_new_mem == "" or a_n_m <4:
            print(f"Please add Full name [You entered > '{add_new_mem}' not allowed ] ")
            continue
        else:
            with open("member_list.txt", "a") as mem_list:
                pointer_position = mem_list.tell()
                mem_list.seek(pointer_position)
                mem_status = "Active"
                mem_list.write(f"[ {getdate()} ]  {add_new_mem.capitalize()}, {mem_status}\n")
                print(f"New Member '{add_new_mem.capitalize()}' added Successfylly ... ")

    elif log_ret_qs == 1:
        print(f"You chose [ log ] ")
        print("Which member's Log ")
        log_mem_qs1 = input("[ 1 = Rohan | 2 = Praveen | 3 = Harry  > ")

        print("-" * 55)

        if log_mem_qs1 != str(log_mem_qs1).isnumeric():
            try:
                log_mem_qs1 == int(log_mem_qs1)
            except Exception as err_log_mem_qs1:
                print("You have options to enter ")
                print(f"Error = ' {err_log_mem_qs1} '")
                print("*" * 170, "\n")
                print("Application Restart")
                continue
        log_mem_qs = int(log_mem_qs1)

        if log_mem_qs == 1:
            print(f"You chose [ Rohan ] ")
            print("hoose log type ")
            food_health_mem1 = input("C[ 1 = Food log | 2 = Health Log ]  > ")
            print("-" * 55)

            if food_health_mem1 != str(food_health_mem1).isnumeric():
                try:
                    food_health_mem1 == int(food_health_mem1)
                except Exception as err_fo_he_me:
                    print("You have options to enter ")
                    print(f"Error = ' {err_fo_he_me} '")
                    print("*" * 170, "\n")
                    print("Application Restart")
                    continue
            food_health_mem = int(food_health_mem1)

            if food_health_mem == 1:
                print(f"You chose [ Food Log of Rohan ] ")
                food_item = input("Enter food item he ate > ")
                with open("food_rohan.txt", "a") as foodrohan:
                    pointer_position = foodrohan.tell()
                    foodrohan.seek(pointer_position)
                    foodrohan.write(f"[ {getdate()} ]  {food_item} \n")
                    print("Food Item added successfully ")
            elif food_health_mem == 2:
                print(f"You chose [ Health Log  of Rohan  ] ")
                health_item = input("Enter how many Exercise 'Rohan' did > ")
                with open("health_rohan.txt", "a") as healthrohan:
                    pointer_position = healthrohan.tell()
                    healthrohan.seek(pointer_position)
                    healthrohan.write(f"[ {getdate()} ]  {health_item} \n")
                    print("Health Item added successfully ")
        elif log_mem_qs == 2:
            print(f"You chose [ Praveen ] ")
            print("Choose log type")
            food_health_mem = int(input(" [ 1 = Food log | 2 = Health Log ]  > "))
            print("=" * 55)

            if food_health_mem == 1:
                print(f"You chose [ Food Log of Praveen ] ")
                food_item = input("Enter food item 'Praveen'  ate > ")
                with open("food_praveen.txt", "a") as foodpraveen:
                    pointer_position = foodpraveen.tell()
                    foodpraveen.seek(pointer_position)
                    foodpraveen.write(f"[ {getdate()} ]  {food_item} \n")
                    print("Food Item added successfully ")
            elif food_health_mem == 2:
                print(f"You chose [ Health Log of Praveen ] ")
                health_item = input("Enter how many Exercise 'Praveen' did > ")
                with open("health_praveen.txt", "a") as healthpraveen:
                    pointer_position = healthpraveen.tell()
                    healthpraveen.seek(pointer_position)
                    healthpraveen.write(f"[ {getdate()} ]   {health_item} \n")
                    print("Health Item added successfully ")
            else:
                print(" No More Options ")

        elif log_mem_qs == 3:
            print(f"You chose [ Harry ] ")
            print("Choose log type")
            food_health_mem = int(input(" [ 1 = Food log | 2 = Health Log ]  > "))
            print("=" * 55)

            if food_health_mem == 1:
                print(f"You chose [ Food Log of Harry ] ")
                food_item = input("Enter food item 'Harry' ate > ")
                with open("food_harry.txt", "a") as foodharry:
                    pointer_position = foodharry.tell()
                    foodharry.seek(pointer_position)
                    foodharry.write(f"[ {getdate()} ]  {food_item} \n")
                    print("Food Item added successfully ")
            elif food_health_mem == 2:
                print(f"You chose [ Health Log of Harry ] ")
                health_item = input("Enter how many Exercise 'Harry' did > ")
                with open("health_harry.txt", "a") as healthharry:
                    pointer_position = healthharry.tell()
                    healthharry.seek(pointer_position)
                    healthharry.write(f" [ {getdate()} ]  {health_item} \n")
                    print("Health Item added successfully ")
            else:
                print(" No More Options ")

        else:
            print(" No More Option is there ")

    elif log_ret_qs == 2:
        print(f"You chose [ Retrieve ] ")
        print("Which member's ? ")
        log_mem_qs = int(input("[ 1 = Rohan | 2 = Praveen | 3 = Harry  | 0 = Member's List  > "))
        print("-" * 80)

        if log_mem_qs == 1:
            print(f"You chose [ Rohan ] ")
            print("Choose log type")
            food_health_mem = int(input(" [ 1 = Food log | 2 = Health Log ]  > "))
            print("=" * 80)

            if food_health_mem == 1:
                with open("food_rohan.txt") as foodrohan:
                    print("-" * 80)
                    print("              Food Log of Rohan ")
                    print("S.No. Date & Time                    Food Item  ")
                    print("-" * 80)
                    count = 1
                    for line in foodrohan:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80)
            elif food_health_mem == 2:
                with open("health_rohan.txt") as healthrohan:
                    print("-" * 80)
                    print("              Health Log of Rohan ")
                    print("S.No. Date & Time                    Exercises   ")
                    print("-" * 80)
                    count = 1
                    for line in healthrohan:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80)

        elif log_mem_qs == 2:
            print(f"You chose [ Praveen ] ")
            print("Choose log type ")
            food_health_mem = int(input("[ 1 = Food log | 2 = Health Log ]  > "))
            print("=" * 80)

            if food_health_mem == 1:
                with open("food_praveen.txt") as foodpraveen:
                    print("-" * 80)
                    print("              Food Log of Praveen ")
                    print("S.No. Date & Time                    Food Item  ")
                    print("-" * 80)
                    count = 1
                    for line in foodpraveen:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80)
            elif food_health_mem == 2:
                with open("health_praveen.txt") as healthpraveen:
                    print("-" * 80)
                    print("              Health log of Praveen  ")
                    print("S.No. Date & Time                    Exercises   ")
                    print("-" * 80)
                    count = 1
                    for line in healthpraveen:
                        print(f"[ {count} ]", line, end="")
                        count += 1

        elif log_mem_qs == 3:
            print(f"You chose [ Harry ] ")
            print("Choose log type ")
            food_health_mem = int(input("[ 1 = Food log | 2 = Health Log ]  > "))
            print("=" * 80)

            if food_health_mem == 1:
                with open("food_harry.txt") as foodharry:
                    print("-" * 80)
                    print("              Food Log of Harry  ")
                    print("S.No. Date & Time                    Food Item  ")
                    print("-" * 80)
                    count = 1
                    for line in foodharry:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80)
            elif food_health_mem == 2:
                with open("health_harry.txt") as healthharry:
                    print("-" * 80)
                    print("              Heath Log of Harry  ")
                    print("S.No. Date & Time                    Exercises   ")
                    print("-" * 80)
                    count = 1
                    for line in healthharry:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80)
        elif log_mem_qs == 0:
                with open("member_list.txt") as mem_list:
                    print("                           Member's List  ")
                    print("S.No. Date & Time                     | Member's Name         | Status   ")
                    print("-" * 80)
                    count = 1
                    for line in mem_list:
                        print(f"[ {count} ]", line, end="")
                        count += 1
                print("-" * 80, "\n")
    elif log_ret_qs == 3:
        print("*" * 160)
        print("  < Exit >  " * 18)
        print("*" * 160)
        break
    else:
        print("other option not allowed ")

# Program Ends
