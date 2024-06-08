import random

def generate_rand_num():
    # Generate a random permutation of digits 0 to 9
    digits = random.sample(range(10), 4)
    
    # Ensure the first digit is not 0
    if digits[0] == 0:
        digits = digits[::-1]
    
    # Convert the list of digits into an integer
    number = 0
    for digit in digits:
        number = (number * 10) + digit
        
    return str(number)

def check_num(input_num, actual_num):
    if not (input_num and actual_num):  # Check if input_num and actual_num are not empty
        return 0, 0  # Return 0 for both bull count and cow count if either input is empty
    
    bull_count = 0
    cow_count = 0
    
    for i in range(4):  # Assuming both input_num and actual_num are strings
        if input_num[i] == actual_num[i]:
            bull_count += 1
        elif input_num[i] in actual_num:
            cow_count += 1
            
    return bull_count, cow_count
