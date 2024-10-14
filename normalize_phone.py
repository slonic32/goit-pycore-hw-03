import re

def normalize_phone(phone_number):
    number = re.sub(r'[^\d+]', '', phone_number.strip())
    if number.startswith('380'):
        number = '+' + number

    elif not number.startswith('+'):
        number = '+38' + number
    
    return number

