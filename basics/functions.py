def getname():
    return "John Doe"

def calculate_sum(a, b):
    return a + b

def calculate_product(a, b, c=1):
    return a * b * c

def calculate_average(numbers):
    return (sum(numbers)/len(numbers)),(len(numbers))


(avg, count) = calculate_average([1, 2, 3, 4, 5])
print(f"Average: {avg}, Count: {count}")  # Average: 3.0, Count: 5