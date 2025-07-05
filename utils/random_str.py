# TODO -  krsnapriya
import random
import string

def get_random_string_of_length_6():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(get_random_string_of_length_6())
