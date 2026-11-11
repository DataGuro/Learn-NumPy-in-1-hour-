#RANDOM
import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1, high=101))

print(60*"=")

print(rng.integers(low=1, high=101, size=3))

print(60*"=")

print(rng.integers(low=1, high=101, size=(3, 2)))

print(60*"=")

rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=101, size=(3, 2)))

print(60*"=")

print(np.random.uniform())

print(60*"=")

rng = np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3,2)))

print(60*"=")

rng = np.random.default_rng()

fruits = np.array(["🍎","🍊","🍌","🥥","🍍"])

fruits = rng.choice(fruits, size=(3,3))
print(fruits)