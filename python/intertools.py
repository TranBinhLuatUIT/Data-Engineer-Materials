# Functions creating iterators for efficient looping, algebra

import itertools


list1 = [1, 2, 3]
list2 = [4, 5, 6]
for _ in itertools.chain(list1, list2):
    print(_)  # Output: 1, 2, 3, 4, 5, 6

for _ in itertools.combinations(list1, 2):
    print(_) # (1, 2), (1, 3), (2, 3), Order matter
    
for _ in itertools.combinations_with_replacement(list1, 2):
    print(_) # Allow, not order


data = [1, 1, 2, 2, 3, 3, 3, 4, 4]
grouped_data = itertools.groupby(data)

for key, group in grouped_data:
    print(f"Key: {key}, Group: {list(group)}")

# Output:
# Key: 1, Group: [1, 1]
# Key: 2, Group: [2, 2]
# Key: 3, Group: [3, 3, 3]
# Key: 4, Group: [4, 4]


data = [(1, 'A'), (1, 'B'), (2, 'C'), (2, 'D'), (3, 'E')]
grouped_data = itertools.groupby(data, key=lambda x: x[0])

for key, group in grouped_data:
    print(f"Key: {key}, Group: {list(group)}")

# Output:
# Key: 1, Group: [(1, 'A'), (1, 'B')]
# Key: 2, Group: [(2, 'C'), (2, 'D')]
# Key: 3, Group: [(3, 'E')]


data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 25},
    {'name': 'David', 'age': 30},
    {'name': 'Eve', 'age': 35}
]

# Sorting by age first
data.sort(key=lambda x: x['age'])

grouped_data = itertools.groupby(data, key=lambda x: x['age'])

for key, group in grouped_data:
    print(f"Age: {key}, Group: {list(group)}")

# Output:
# Age: 25, Group: [{'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 25}]
# Age: 30, Group: [{'name': 'Alice', 'age': 30}, {'name': 'David', 'age': 30}]
# Age: 35, Group: [{'name': 'Eve', 'age': 35}]


# Zip
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

print(list(itertools.zip_longest(list1, list2)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, None)]

batch_data = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 , 10]
print(list(itertools.batched(batch_data, 3)))
#Ouput: [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]