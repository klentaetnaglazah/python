def get_sum(num1: int, num2: int) -> int:
    return num1 + num2

def count_capital_letters(string: str) -> int:
    count = 0
    for letter in string:
        if letter.isupper() == True:
            count += 1
    return count

def decode_string(string: str) -> str:
    lower_string = string.lower()
    result = ''
    for char in lower_string:
        if lower_string.count(char.lower()) > 1:
            result += ')'
        else:
            result += '('
    return result

def get_odd_count(string: str) -> int:
    count = 0
    for num in string:
        if int(num) % 2 == 0 and int(num) != 0:
            count += 1
    return count

def check_access(has_keycard: bool, has_fingerprint: bool, is_alarm: bool, is_daylight: bool) -> bool:
    if ((has_keycard == True and is_daylight == True) or has_fingerprint == True) and is_alarm == False:
        return True
    return False
