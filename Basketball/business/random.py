import random
def generate_random_integer(a,b):
    return random.randint(a,b)


def generate_random_string():
    
    posturi = ['Extrema','Pivot','Fundas']
    
    return ''.join(random.choice(posturi))


