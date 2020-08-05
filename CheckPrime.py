def prime():
    inp = int(input('Enter A number > '))
    a = []
    for x in range(2,inp):
        if inp%x == 0:
            a.append(False)
        else:
            a.append(True)
    if a.count(False) == 0:
        print(str(inp) + ' is a prime Number.')
    else:
        print(str(inp) + ' is not a prime Number.')
prime()
