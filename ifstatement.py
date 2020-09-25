Speed= int(input("What was your average speed in km/h"))

Average= int(input("What was the allowed speed on the road?"))

points= int(Speed-Average)/5


print("Points:",int(points))

if points>=12:
    print("Time to go to jail!!")

elif Speed<=Average:
    print("OK")
