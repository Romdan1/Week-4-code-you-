def max_num(numbers):
    largest_number = numbers[0]
    for num in numbers:
        if num >= largest_number:
            largest_number = num
    return largest_number  


# Test it
print(max_num([1, 3, 4, 5, 6, 6, 7]))  # 7