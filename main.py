import math
r = math.sqrt(3)
h = math.log(14, 3)

v = math.pi * pow(r, 2) * h
print(r)
print(h)
print(f"The volume of the cylinder with the radius {r} and height {h} is: {round(v, 4)}")

if v > 10:
    print("It is a big cylinder")
else:
    print("It is a small cylinder")


