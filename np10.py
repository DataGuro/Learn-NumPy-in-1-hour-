'''
Filtering = Refers to the process of sleceting elements
            from an array that match a given condition
'''

import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]

evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

where = np.where(ages >= 18, ages, 0)


print("TEENAGERS:")
print(teenagers)

print(60*"=")

print("\nADULTS:")
print(adults)

print(60*"=")

print("\nSENIORS:")
print(seniors)

print(60*"=")

print(evens)
print(odds)

print(60*"=")

print(where)