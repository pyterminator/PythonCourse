def Average(*args):
    length = len(args)
    total = sum(args)
    avg = int(total / length)
    return avg
    # return [length, avg]

result = Average(1,2,3,4,5)
print(result)