import time
car = 0
speed = 0
print("\nhello im a car 'help' for more info")
while car != -1:
    choice = input(">").lower().strip()
    if choice == 'start':
        if car == 1:
            print("car is already ON 'go' to speed up")
        else:
            print('car is ready to vroom "go" to speed up ,ctrl+c to slow down') 
            car = 1
    elif choice == 'go':    
        if car == 1:
            try:
                while speed < 50:
                    speed += 1
                    print(f"{'.' * speed}o=o" ,end="\r")
                    time.sleep(.4)
            except KeyboardInterrupt:
                if speed != 0:
                    print("Slowing Down ,the speed goes ,ctrl+c to maintain current speed")
                    try:
                        for i in range(int(speed), -1 , -1):
                            print(i ,end="->")
                            time.sleep(.3)
                        print("")
                    except KeyboardInterrupt:
                        print(i)
                    if i == 0:
                        print("car stops")
                    speed = i
                    print("'go' to accelerate")
                else:
                    print('the car is at rest')
            if speed !=0:
                print(f"car is moving at {speed} kmph")
        else:
            print("first 'start' the car")
        if speed == 50:
            print("max. speed reached")
    elif choice == 'stop':
        if car == 1:
            for i in range(int(speed), 0 , -1):
                print(i ,end="->")
            print("0")
            print("car is stopped")
            car = 0
            speed = 0
        else:
            print('car is already at rest')
    elif choice == 'status':
        if car == 1 and speed != 0:
            print(f"car is moving at a speed of {speed} kmph")
        elif speed == 0:
                print("car is ready to go")
        elif car == 0 :
            print('car is at rest "start" to move')
    elif choice == 'help':
        print(''' 
'start' to start the car
'go' to accelarate the car
'ctrl+c' on keyborad to slow down after car goes vroom
'break' to apply breaks
'horn' to honk
'status' to know the speed and state of car
'stop'  to stop the car
'exit' to stop the process
        ''')
    elif choice =='break':
            if speed != 0:
                print("BREAK!!, the speed goes")
                try:
                    for i in range(int(speed), -1 , -1):
                        print(i ,end="->")
                        time.sleep(.4)
                    print("")
                except KeyboardInterrupt:
                    print(i)
                speed = i
                if i == 0:
                    print("car stops")
                print("car is slowed 'go' to accelerate")
            else:
                print('the car is at rest')

    elif choice =='horn':
        print("honk honk")        
    elif choice =='exit':
        if car == 1:
            print('car is stopped and exiting')
        print("bye")
        car = -1 
    else:
        print("invalid action 'help' for more info")
import time
car = 0
speed = 0
print("\nhello im a car 'help' for more info")
while car != -1:
    choice = input(">").lower().strip()
    if choice == 'start':
        if car == 1:
            print("car is already ON 'go' to speed up")
        else:
            print('car is ready to vroom "go" to speed up ,ctrl+c to slow down') 
            car = 1
    elif choice == 'go':    
        if car == 1:
            try:
                while speed < 50:
                    speed += 1
                    print(f"{'.' * speed}o=o" ,end="\r")
                    time.sleep(.4)
            except KeyboardInterrupt:
                if speed != 0:
                    print("Slowing Down ,the speed goes ,ctrl+c to maintain current speed")
                    try:
                        for i in range(int(speed), -1 , -1):
                            print(i ,end="->")
                            time.sleep(.3)
                        print("")
                    except KeyboardInterrupt:
                        print(i)
                    if i == 0:
                        print("car stops")
                    speed = i
                    print("'go' to accelerate")
                else:
                    print('the car is at rest')
            if speed !=0:
                print(f"car is moving at {speed} kmph")
        else:
            print("first 'start' the car")
        if speed == 50:
            print("max. speed reached")
    elif choice == 'stop':
        if car == 1:
            for i in range(int(speed), 0 , -1):
                print(i ,end="->")
            print("0")
            print("car is stopped")
            car = 0
            speed = 0
        else:
            print('car is already at rest')
    elif choice == 'status':
        if car == 1 and speed != 0:
            print(f"car is moving at a speed of {speed} kmph")
        elif speed == 0:
                print("car is ready to go")
        elif car == 0 :
            print('car is at rest "start" to move')
    elif choice == 'help':
        print(''' 
'start' to start the car
'go' to accelarate the car
'ctrl+c' on keyborad to slow down after car goes vroom
'break' to apply breaks
'horn' to honk
'status' to know the speed and state of car
'stop'  to stop the car
'exit' to stop the process
        ''')
    elif choice =='break':
            if speed != 0:
                print("BREAK!!, the speed goes")
                try:
                    for i in range(int(speed), -1 , -1):
                        print(i ,end="->")
                        time.sleep(.4)
                    print("")
                except KeyboardInterrupt:
                    print(i)
                speed = i
                if i == 0:
                    print("car stops")
                print("car is slowed 'go' to accelerate")
            else:
                print('the car is at rest')
                
    elif choice =='horn':
        print("honk honk")        
    elif choice =='exit':
        if car == 1:
            print('car is stopped and exiting')
        print("bye")
        car = -1 
    else:
        print("invalid action 'help' for more info")
