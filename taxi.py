distance = float(input("Enter your distance: "))
time = int(input("Enter your time(0-23): "))
price = 2 + distance * 0.8

if time <= 6 or time == 23:
    price = 2 + distance * 0.96

if price < 3:
    price = 3


print(f"Your fare is {price}")