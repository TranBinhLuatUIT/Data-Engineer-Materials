try:
    try:
        # Code that may raise an exception
        result = 10 / 2
    except ZeroDivisionError:
        print("Inner catch: Division by zero.")
    else:
        print(f"Inner else: Result is {result}")
    finally:
        print("Inner finally: This will always be executed.")
except Exception as e:
    print(f"Outer catch: An error occurred: {e}")
else:
    print("Outer else: No exceptions occurred.")
finally:
    print("Outer finally: This will always be executed.")
