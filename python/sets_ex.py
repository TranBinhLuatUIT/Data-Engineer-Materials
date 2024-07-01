# Define two sets
set_a = set([5, 4, 3, 2, 2])
set_b = set([1, 2, 3, 8])

# Print initial sets
print("Initial Set A:", set_a)
print("Initial Set B:", set_b)

# Adding a value to Set A (no effect because 5 is already in the set)
set_a.add(5)
print("After adding 5 to Set A:", set_a)
# Set stores distinct values, so it remains {5, 4, 3, 2}

# Adding a new value to Set A
set_a.add(6)
print("After adding 6 to Set A:", set_a)
# Now Set A becomes {2, 3, 4, 5, 6}

# Trying to add multiple values at once (this will raise an error)
try:
    set_a.add(1, 7)
except TypeError:
    print("Add only accepts one value at a time")

# Updating Set A with multiple values
set_a.update([1, 7])
print("After updating Set A with [1, 7]:", set_a)
# Update works with iterables, adding multiple values. Now Set A is {1, 2, 3, 4, 5, 6, 7}

# Discarding a value from Set A
set_a.discard(7)
print("After discarding 7 from Set A:", set_a)
# Now Set A becomes {1, 2, 3, 4, 5, 6}

# Difference between Set A and Set B
difference_ab = set_a.difference(set_b)
print("Difference between Set A and Set B:", difference_ab)
# Elements in Set A but not in Set B. Result: {4, 5, 6}

# Union of Set A and Set B
union_ab = set_a.union(set_b)
print("Union of Set A and Set B:", union_ab)
# All unique elements from both sets. Result: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of Set A and Set B
intersection_ab = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_ab)
# Elements common to both sets. Result: {1, 2, 3}

# Symmetric Difference between Set A and Set B
sym_diff_ab = set_a.symmetric_difference(set_b)
print("Symmetric Difference between Set A and Set B:", sym_diff_ab)
# Elements in either Set A or Set B but not in both. Result: {4, 5, 6, 8}

# Check if set A is a subset of set B: https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
set_c = set([1 , 2 ,3 ,4])
set_d = set([1, 2, 3 , 5])
set_e = set([1, 2 ,3, 4, 6, 7])

diff_ce = set_c.difference(set_e)
diff_de = set_d.difference(set_e)
if (diff_ce == set()):
    print("C is subset of E")

if (diff_de != set()):
    print("D is not subset of E")