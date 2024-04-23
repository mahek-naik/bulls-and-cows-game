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
        
    return number

print(generate_rand_num())