import string    
import random 
str_len = 15 


def generate_strings(num):
    res = []
    for _ in range(num):
        ran = ''.join(random.choices(string.ascii_lowercase, k = str_len))    
        res.append(ran)
    
    return res
    