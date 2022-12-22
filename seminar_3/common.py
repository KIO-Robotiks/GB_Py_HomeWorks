def get_random_list(size, max, value):
    
    my_list = []
    
    if value == 'int':
        from random import randrange
        for _ in range(size):
            x = randrange(0, max)
            my_list.append(x)
    if value == 'real':
        from random import uniform
        for _ in range(size):
            x = round(uniform(0, max), 3)
            my_list.append(x)
    
    return my_list