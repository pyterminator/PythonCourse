from time import sleep

count = 3
while count > 0: 
    print(f"{count}\r", end="")
    sleep(1)
    count -= 1
    if count == 0: print("\rHello world!", end="")