def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
print(large_power(10, 4))   # True (10000 > 5000)
print(large_power(2, 10))   # True (1024 < 5000 → False)
print(large_power(5, 5))    # True (3125 < 5000 → False)
print(large_power(8, 5))    # True (32768 > 5000)
print(large_power(3, 6))    # True (729 < 5000 → False)
print(large_power(7, 4))    # True (2401 < 5000 → False)