from random import randint, seed

def d6(times = 1):
    seed()
    return randint(1 * times, 6 * times)

def d10(times = 1):
    seed()
    return randint(1 * times, 10 * times)

def d100(time = 1):
    seed()
    return randint(1 * times, 100 * times)

def dOpenEnded():
    seed()
    value = 0
    if value <= 2:
        value -= d100()
    elif value >= 99:
        value += d100()
    else:
        value += d100()
    return value
            
    