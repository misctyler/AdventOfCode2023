import re

def get_first_digit(s):
    for char in s:
        if char.isnumeric():
            return char
    return None

def get_last_digit(s):
    for char in reversed(s):
        if char.isnumeric():
            return char
    return None

def replace_text_numbers(s):
    replacements = {  
                    "one": "o1e"
                    ,"two": "t2o"
                    ,"three": "t3e"
                    ,"four": "f4r"
                    ,"five": "f5e"
                    ,"six": "s6x"
                    ,"seven": "s7n"
                    ,"eight": "e8t"
                    ,"nine": "n9e"
                    }  
    
    for key, value in replacements.items():
        s = s.replace(key, value)
    return s

def calculate_calibration(file_path, second_run):
    calibration_total = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if second_run == True: line = replace_text_numbers(line)

            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)

            if first_digit is not None and last_digit is not None:
                calibration_value = int(first_digit) * 10 + int(last_digit)
                calibration_total += calibration_value

    return calibration_total

file_path = '~/day1input.txt'  
total_calibration = calculate_calibration(file_path, False)
print('Calibration Value: {total_calibration}')
total_calibration = calculate_calibration(file_path, True)
print('Calibration Value: {total_calibration}')
