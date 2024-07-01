from collections import Counter, deque, ChainMap

# Demonstrating the usage of Counter
def counter_example():
    """A Counter is a dict subclass for counting hashable objects.
    
    """
    my_list = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
    
    # Creating a Counter object
    count = Counter(my_list)
    print("Counter:", count)  # Output: Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    
    # Displaying items and their counts
    print("Items and counts:", count.items())  # Output: dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])
    
    # Displaying the most common element
    print("Most common element:", count.most_common(1))  # Output: [(2, 4)]
    
    # Displaying the total count of all elements
    print("Total count of elements:", sum(count.values()))  # Output: 14

# Demonstrating the usage of deque
def deque_example():
    """Deques are a generalization of stacks and queues
    Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
    """
    # Creating a deque
    dq = deque()

    # Appending items to the right end
    dq.append('a')
    dq.append('b')
    dq.append('c')

    # Appending items to the left end
    dq.appendleft('x')
    dq.appendleft('y')

    print("Deque after appends:", dq)  # Output: deque(['y', 'x', 'a', 'b', 'c'])

    # Popping items from the right end
    print("Popped from right:", dq.pop())  # Output: 'c'
    print("Deque after popping from right:", dq)  # Output: deque(['y', 'x', 'a', 'b'])

    # Popping items from the left end
    print("Popped from left:", dq.popleft())  # Output: 'y'
    print("Deque after popping from left:", dq)  # Output: deque(['x', 'a', 'b'])

    # Rotating the deque to the right
    dq.rotate(1)
    print("Deque after rotating right:", dq)  # Output: deque(['b', 'x', 'a'])

    # Rotating the deque to the left
    dq.rotate(-1)
    print("Deque after rotating left:", dq)  # Output: deque(['x', 'a', 'b'])

def defaultdict_example():
    """
    Demonstrates the use of collections.defaultdict to automatically handle missing keys with a default value.
    
    Example:
    >>> defaultdict_example()
    defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})
    """
    # Create a defaultdict with list as the default factory
    dd = defaultdict(list)
    
    # Adding values
    dd['fruits'].append('apple')
    dd['fruits'].append('banana')
    dd['vegetables'].append('carrot')
    
    # Printing defaultdict
    print("Defaultdict:", dd)
    
    # Trying to access a missing key
    print("Accessing missing key:", dd['grains'])  # Output: []
    
    # Adding a value to the newly accessed key
    dd['grains'].append('rice')
    print("After adding to new key:", dd)

def normal_dict_example():
    """
    Demonstrates the use of a normal dict and handling missing keys manually.
    
    Example:
    >>> normal_dict_example()
    {'fruits': ['apple', 'banana'], 'vegetables': ['carrot'], 'grains': ['rice']}
    """
    # Create a normal dict
    normal_dict = {}
    
    # Adding values with manual checks
    if 'fruits' not in normal_dict:
        normal_dict['fruits'] = []
    normal_dict['fruits'].append('apple')
    
    if 'fruits' not in normal_dict:
        normal_dict['fruits'] = []
    normal_dict['fruits'].append('banana')
    
    if 'vegetables' not in normal_dict:
        normal_dict['vegetables'] = []
    normal_dict['vegetables'].append('carrot')
    
    # Trying to access a missing key
    try:
        normal_dict['grains']
    except KeyError:
        print("KeyError: 'grains'")
    
    # Adding a value to the newly accessed key
    if 'grains' not in normal_dict:
        normal_dict['grains'] = []
    normal_dict['grains'].append('rice')
    
    # Printing normal dict
    print("Normal dict:", normal_dict)

def chainmap_example():
    """Demonstrates the use of collections.ChainMap to combine multiple dictionaries.
        - Memory Efficiency: ChainMap does not combine the dictionaries into a new dictionary; it maintains references to the original dictionaries.
        - Order of Precedence: The order in which the dictionaries are passed to ChainMap determines which dictionary's values are used when keys overlap.
    """
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    
    combined = ChainMap(dict1, dict2)
    print(combined)
    
    """Allows you to overlay settings in a way that respects the hierarchy and precedence of configurations python
    
    """
    defaults = {'theme': 'light', 'language': 'English'}
    user_settings = {'theme': 'dark'}
    runtime_settings = {'language': 'Spanish'}

    config = ChainMap(runtime_settings, user_settings, defaults)
    print(config['theme'])  # Output: 'dark'
    print(config['language'])  # Output: 'Spanish'
    
    

if __name__ == "__main__":
    print("Counter Example:")
    counter_example()
    print("\nDeque Example:")
    deque_example()
    print("Defaultdict Example:")
    defaultdict_example()