import math

# sum two complex numbers
def sum(c1, c2):

    number1 =  c1[0] + c2[0]
    number2 = c1[1] + c2[1]
    print_beatiful (number1, number2)
    return ( number1, number2)

# sustration two complex numbers
def sustration(c1, c2):

    number1 =  c1[0] - c2[0]
    number2 = c1[1] - c2[1]
    print_beatiful(number1, number2)
    return (number1, number2)

#multiply two complex numbers
def multiplation (c1, c2):

    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginate = c1[0] * c2[1] + c1[1] * c2[0]

    print_beatiful(real, imaginate)
    return (real, imaginate)
 

#This fuction go the definition and use conjugate and multiplication for division two complex numbers
def division(c1, c2):

    number = multiplation(c1, conjugate(c2))
    denominator = multiplation(c2, conjugate(c2))
    real = number[0] / denominator[0]
    imaginary = number[1] / denominator[0]
    print_beatiful(real, imaginary)
    return(real, imaginary)

#Find the magnitude of complex number
def module(c1):

    number1 = c1[0]**2 
    number2 = c1[1]**2
    operation = (number1 + number2)** 1/2
    print_beatiful (operation)
    return operation

# Negate the imaginary part
def conjugate(c1):

    number1 = c1[0]
    nubmer2 = c1[1]*-1
    print_beatiful(number1, nubmer2)
    return (number1, nubmer2)

#receive a cartesian coordinate  and the convert a polar coordinate 
def cartesian_to_polar(coordinate):
   
    distance1 = (coordinate[0]**2 + coordinate[1]**2) ** 1/2
    angle = (math.atan2(coordinate[1], coordinate[0]))
    print_beatiful(distance1,angle)
    return [distance1, angle]

#receive a polar coordinate and the convert a cartesian coordinate 
def polar_to_cartesian(coordinate):
    
    distance1 = coordinate[0]
    angle =  math.radians(coordinate[1])
    x = distance1 * math.cos(angle)
    y = distance1 * math.sin(angle)
    print_beatiful(x,y)
    return (x, y)

#Find the angle of the module whit the coordinates.
def fase(coordinate):
   
    inverse = math.atan2(coordinate[1],coordinate[0])
    print_beatiful(inverse)
    return (inverse)

#Only print very very beatiful :D. The teacher request it. 
def print_beatiful (a,b):
    if b == None :
        print (a)
    else:
        print ("( " , a ," , ",b ,"i)")



if __name__ == "__main__":
    sum((4,5),(3,5))
    sustration((4,5),(3,5))
    cartesian_to_polar((4,5))