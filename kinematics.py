import math

print("enter the variable letter (enter) then the number, if its unknown, enter x")
print("a = accleration, t = time, v = final velocity, u = initial velocity, s = displacement")
print("enter nothing to exit the program")

def noTime(a, s, u, v):
    if a == "x":
        return "acceleration: " + str((v+u)/2*(v-u)/s)
    if s == "x":
        return "displacement: " + str((v+u)/2*(v-u)/a)
    if u == "x":
        return "initial Velocity: ±" + str(math.sqrt(v*v-2*a*s))
    if v == "x":
        return "final velocity ±: " + str(math.sqrt(u*u+2*a*s))

def noAcceleration(s, u, v, t):
    if s == "x":
        return "displacement: " + str(0.5*t*(u+v))
    if u == "x":
        return "initial velocity: " + str(2*s/t-v)
    if v == "x":
        return "final velocity: " + str(2*s/t-u)
    if t == "x":
        return "time: " + str(2*s/(u+v))

def noDisplacement(u, v, a, t):
    if v == "x":
        return "final velocity: " + str(u+a*t)
    if u == "x":
        return "initial velocity: " + str(v-a*t)
    if a == "x":
        return "acceleration: " + str((v-u)/t)
    if t == "x":
        return "time: " + str((v-u)/a)
        
def noInitialVelocity(s, v, t, a):
    if s == "x":
        return "displacement: " + str(v*t-0.5*a*t*t)
    if v == "x":
        return "final velocity: " + str(s/t + a*t/2)
    if t == "x":
        return "time: " + str((v+math.sqrt((v*v-2*a*s)))/a) + " or " + str((v-math.sqrt((v*v-2*a*s)))/a)
    if a == "x":
        return "acceleration: " + str((2*(v-s/t))/t)

def noFinalVelocity (s,u,t,a):
    if s == "x":
        return "displacement: " + str(u*t+0.5*a*t*t)
    if u == "x":
        return "initial velocity: " + str(s/t-0.5*a*t)
    if a == "x":
        return "acceleration: " + str((2*(s/t-u))/t)
    if t == "x":
        return "time: " + str((-u+math.sqrt(u*u+2*a*s))/a) + " or " + str((-u-math.sqrt(u*u+2*a*s))/a)

while True:
    acceleration = time = initialVelocity = finalVelocity = displacement = "n/a"
    for i in range(4):
        result = input()
        if result == "a":
            acceleration = input()
            if acceleration != "x":
                acceleration = float (acceleration)
        if result == "t":
            time = input()
            if time != "x":
                time = float (time)
        if result == "u":
            initialVelocity = input()
            if initialVelocity != "x":
                initialVelocity = float (initialVelocity)
        if result == "v":
            finalVelocity = input()
            if finalVelocity != "x":
                finalVelocity = float (finalVelocity)
        if result == "s":
            displacement = input()
            if displacement != "x":
                displacement = float (displacement)
        if result == "":
            exit()

    if time == "n/a":
        print(noTime(acceleration, displacement, initialVelocity, finalVelocity))
    if acceleration == "n/a":
        print(noAcceleration(displacement, initialVelocity, finalVelocity, time))
    if displacement == "n/a":
        print(noDisplacement(initialVelocity, finalVelocity, acceleration, time))
    if initialVelocity == "n/a":
       print(noInitialVelocity(displacement, finalVelocity, time, acceleration))
    if finalVelocity == "n/a":
        print(noFinalVelocity(displacement, initialVelocity, time, acceleration))
