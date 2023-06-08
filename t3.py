import os
if not os.path.exists("cats"):
    os.makedirs("cats")

with open("cats/eample.txt", "w") as file:
    file.write("hi bitch ;)")
print(os.listdir("cats"))