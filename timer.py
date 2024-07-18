from time import sleep
count = 5
while count > 0:
    text = f"{count}\r"
    print(text, end="")
    sleep(1)
    count -= 1

    if count == 0:
        print("\rHello world!", end="")