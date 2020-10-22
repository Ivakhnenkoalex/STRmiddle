def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_change_place_word(str):
    i = 0
    s1 = ''
    s2 = ''
    s3 = ''
    while str[i] != ' ':
        s1 += str[i]
        i += 1
    i += 1
    while i < ft_len(str):
        s2 += str[i]
        i += 1
        s3 = s2 + ' ' + s1
    return s3
