#!/usr/bin/python3
def magic_string(n=1):
    result = []
    for i in range(n):
        if i == 0:
            result.append('BestSchool')
        else:
            result.append(f', BestSchool')
    return ''.join(result)
