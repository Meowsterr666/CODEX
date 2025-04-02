import random
    
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

newRange = int(random.random() * 5)

chosen = friends[newRange]
print(f"Random friend pick: {chosen}, Number picked: {newRange}")

"""
The code above is basically how I solved this,
Angela gives 2 other options in her solution; heres all those permutations   
"""

# 1st other option
print(random.choice(friends))

# 2nd other option
random_index = random.randint(0, 4)
print(friends[random_index])