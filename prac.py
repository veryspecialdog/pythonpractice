def fibs(n):
    numbers=[0,1]
    for i in range(n-2):
        numbers.append(numbers[-1]+numbers[-2])
    return numbers

print(fibs(8))