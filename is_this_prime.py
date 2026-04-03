def is_prime(number):

    if number < 2:
        return False  
    
    prime_status = True
    
    for i in range(2, number):
        if number % i == 0:
            prime_status = False  
            break 
    
    if prime_status:
        return True
    else:
        return False

print(is_prime(6))  
print(is_prime(7))   
print(is_prime(2))   
print(is_prime(1))   
print(is_prime(13))  