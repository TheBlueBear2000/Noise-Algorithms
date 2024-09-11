from math import sqrt
from random import randint

def getRand(x, max, min):
    
    x = abs((x*(55+x) * 22.5) / (x/2) * (x*5))/(56*x)+41267.3269874/583*x
    
    x = (x - int(x)) * (max-min) + min
    
    return int(x)

# digits = {}
# length = 2
# maxN = 142
# minN = 24

# for i in range(minN, maxN+1):
#     digits[str(i)] = 0

# for i in range(100000):
#     digits[str(getRand(randint(0,9999999999), maxN, minN))] += 1
    
# maxLen = 0
# for digit in digits:
#     maxLen = max(maxLen, len(str(digits[digit])))
    
    
# for digit in digits:
#     print(f"{digit:<{length}} -> {digits[digit]:>{maxLen}}")
    
print(getRand(15, 348, 76))