import itertools

def chain_example():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Chain Example:")
    for item in itertools.chain(list1, list2):
        print(item)  # Output: 1, 2, 3, 4, 5, 6

def combinations_example():
    list1 = [1, 2, 3]
    print("\nCombinations Example:")
    for combo in itertools.combinations(list1, 2):
        print(combo)  # Output: (1, 2), (1, 3), (2, 3)

    print("\nCombinations with Replacement Example:")
    for combo in itertools.combinations_with_replacement(list1, 2):
        print(combo)  # Output: (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)

def groupby_example_simple():
    data = [1, 1, 2, 2, 3, 3, 3, 4, 4]
    grouped_data = itertools.groupby(data)
    
    print("\nGroupby Example with Simple Data:")
    for key, group in grouped_data:
        print(f"Key: {key}, Group: {list(group)}")
    # Output:
    # Key: 1, Group: [1, 1]
    # Key: 2, Group: [2, 2]
    # Key: 3, Group: [3, 3, 3]
    # Key: 4, Group: [4, 4]

def groupby_example_complex():
    data = [(1, 'A'), (1, 'B'), (2, 'C'), (2, 'D'), (3, 'E')]
    grouped_data = itertools.groupby(data, key=lambda x: x[0])

    print("\nGroupby Example with Complex Data:")
    for key, group in grouped_data:
        print(f"Key: {key}, Group: {list(group)}")
    # Output:
    # Key: 1, Group: [(1, 'A'), (1, 'B')]
    # Key: 2, Group: [(2, 'C'), (2, 'D')]
    # Key: 3, Group: [(3, 'E')]

def groupby_example_dict():
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

    print("\nGroupby Example with Dictionary Data:")
    for key, group in grouped_data:
        print(f"Age: {key}, Group: {list(group)}")
    # Output:
    # Age: 25, Group: [{'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 25}]
    # Age: 30, Group: [{'name': 'Alice', 'age': 30}, {'name': 'David', 'age': 30}]
    # Age: 35, Group: [{'name': 'Eve', 'age': 35}]

def zip_example():
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c']
    print("\nZip Example:")
    print(list(zip(list1, list2)))
    # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

    print("\nZip Longest Example:")
    print(list(itertools.zip_longest(list1, list2)))
    # Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, None)]

def batched_example():
    batch_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\nBatched Example:")
    print(list(itertools.batched(batch_data, 3)))
    # Output: [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]

if __name__ == "__main__":
    chain_example()
    combinations_example()
    groupby_example_simple()
    groupby_example
