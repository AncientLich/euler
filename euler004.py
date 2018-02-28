def is_palindrome(num):
    xstr = str(num)
    while len(xstr) >=2:
        if xstr[0] == xstr[-1]:
            xstr = xstr[1:-1]
        else:
            return False
    return True


escape = False
result = 0
for val1 in range(999, 99, -1):
    for val2 in range(999, 99, -1):
        value = val1 * val2
        if is_palindrome(value):
            if value > result:
                result = value

print("result is", result)
