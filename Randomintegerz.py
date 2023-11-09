import random
from collections import Counter

def generate_random_integers(n,min_val,max_val):
    return [random.randint(min_val,max_val) for _ in range(n)]

def find_mode(numbers):
    counter = Counter(numbers)
    mode = counter.most_common(1)[0][0]
    return mode

random_integers = generate_random_integers(100, 1, 20)
number_mode = find_mode(random_integers)

print("Generated random integers:",random_integers)
print("Mode(Reapeting number)",number_mode)