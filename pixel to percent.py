n = float(input("Enter the number of pixels for width or height: "))
m = input("what have you entered width or height: ")
if m.lower() == "w":
    Percentage = (n / 2560) * 100
    print(Percentage)
elif m.lower() == "h":
    Percentage = (n / 1600) * 100
    print(Percentage)
else:
    print("not present")
