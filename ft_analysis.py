def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_analysis(str):
    print(str[2])
    c = ft_len(str)
    d = c
    c = c - 2
    print(str[c])
    print(str[0], str[1], str[2], str[3], str[4])
    i = 0
    while i < c:
        print(str[i], end=" ")
        i = i + 1
    i = 0
    print('')
    while i < d:
        if i % 2 == 0:
            print(str[i], end=" ")
        i = i + 1
    i = 0
    print('')
    while i < d:
        if i % 2 != 0:
            print(str[i], end=" ")
        i = i + 1
    i = 0
    k = d
    d = d - 1
    print('')
    while d >= i:
        print(str[d], end=" ")
        d = d - 1
    d = k
    i = 0
    print('')
    if d % 2 != 0:
        while d >= i:
            if d % 2 == 0:
                print(str[d], end=" ")
            d = d - 1
    if d % 2 == 0:
        while d >= i:
            if d % 2 != 0:
                print(str[d], end=" ")
            d = d - 1
    print('')
    print(k)


ft_analysis('12345678')
