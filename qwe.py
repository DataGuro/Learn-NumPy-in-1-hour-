import random

numbers = []
for i in range(1000000):
    numbers.append(random.randint(1, 100))



import time

start = time.time()
mean = calculate_mean(numbers)
end = time.time()

print("Manual Mean:", mean)
print("Time:", end - start)




import time
import numpy as np
import numbers

array = np.array(numbers)
start = time.time()
mean = np.mean(array)
end = time.time()

print("NumPy Mean:", mean)
print("Time:", end - start)
