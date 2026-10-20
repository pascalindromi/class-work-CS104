import os
os.system("cls" if os.name == "nt" else "clear") # for less cluttered output

input1 = float(input("Enter the first angle: "))
input2 = float(input("Enter the second angle: "))
print(f"the third angle is: {180 - (input1 + input2)}")