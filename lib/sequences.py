def print_fibonacci(length):
    """
    Prints the Fibonacci sequence as a list up to the given length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate.
                      Includes 0 as the first element when length > 0.
    
    Example:
        print_fibonacci(9) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]
        print_fibonacci(0) -> []
        print_fibonacci(1) -> [0]
        print_fibonacci(2) -> [0, 1]
    """
    # Handle edge cases
    if length <= 0:
        print([])
        return
    if length == 1:
        print([0])
        return
    
    # Initialize the fibonacci sequence list
    fibonacci = [0, 1]
    
    # Generate remaining numbers until we reach the desired length
    while len(fibonacci) < length:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    
    # If length is exactly 2, we already have [0, 1]
    # Otherwise trim if we generated one extra (shouldn't happen with while loop)
    print(fibonacci[:length])