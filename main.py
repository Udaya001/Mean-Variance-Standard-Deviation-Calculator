from mean_var_std import calculate

if __name__ == "__main__":
    
    print("Please enter 9 numbers separated by spaces:")
    user_input = input()
    
    # Convert the input string into a list of integers
    try:
        lst = list(map(int, user_input.split()))
    except ValueError:
        raise ValueError("Input must contain valid integers.")
    
    # Ensure there are exactly 9 numbers
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
        
    # Call the calculate function with the user input list
    result = calculate(lst)
    print(result)
