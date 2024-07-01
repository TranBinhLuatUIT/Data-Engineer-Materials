from collections import Counter, deque

# Demonstrating the usage of Counter
def counter_example():
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

if __name__ == "__main__":
    print("Counter Example:")
    counter_example()
    print("\nDeque Example:")
    deque_example()
