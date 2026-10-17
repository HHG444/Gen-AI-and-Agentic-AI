#repeating code
user_command = "" #empty string
while user_command.lower() != "quit":
    user_command = input(">")
    if user_command.lower() == "start":
        print("car started...")
    elif user_command.lower() == "stop":
        print("car stopped...")
    elif user_command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif user_command == "quit":
        break
    else:
        print("sorry, I don't understand you")

print('*' * 25)
#dry code

user_command = "" #empty string
while True:
    user_command = input(">").lower()
    if user_command == "start":
        print("car started...")
    elif user_command == "stop":
        print("car stopped...")
    elif user_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif user_command == "quit":
        break
    else:
        print("sorry, I don't understand you")

print('*'* 25)
#scenario 3
user_command = "" #empty string
started = False
while True:
    user_command = input(">").lower()
    if user_command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started...")
    elif user_command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped...")
    elif user_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif user_command == "quit":
        break
    else:
        print("sorry, I don't understand you")