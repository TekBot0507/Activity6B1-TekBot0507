print("Hello world!")

newList = []

for i in range(20):
    newList.append(i)

def fibonacci_series(i):
    if i == 0:
        return 0
    if i <= 2:
        return 1
    
    return fibonacci_series(i - 1) + fibonacci_series(i - 2)

fib_list = []

for i in range(20):
    fib_list.append(fibonacci_series(i))

print(newList)
print(fib_list)