def motor_speed():
    while True:
        try:
            speed = int(input("Enter Motor Speed 0-100: "))
        except ValueError:
            print("speed is not an integer")
        
        else:
            break 
        return speed 
    print("The motor speed is",{speed})
    
motor_speed()

def get_function():
    while True:
        try:
            x_coordinate = int(input("Enter x coordinate: "))
        except ValueError:
            print("Try again")
        if x_coordinate > 100:
            print("Coordinate out of range")
        elif x_coordinate < -100:
            print("Coordinate out of range")

        else: 
            break
    print ("The x coordinate is",{x_coordinate})
    return x_coordinate
    
get_function()
