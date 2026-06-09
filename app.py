def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(5, 5)
    print(f"The result is: {result}")
    
    # A simple safety check (assertion) to make sure our code works
    assert result == 8, "Math is broken!"
    print("All checks passed successfully!")