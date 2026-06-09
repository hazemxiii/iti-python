different_numbers_example = [1,2,3,4]
duplicate_numbers_example = [1,2,3,4,3]

def check_if_numbers_different(numbers):
    occurence = {}
    for number in numbers:
        if number in occurence:
            return False
        occurence[number]=number
    return True

print("Different: ",check_if_numbers_different(different_numbers_example))
print("Duplicate: ",check_if_numbers_different(duplicate_numbers_example))