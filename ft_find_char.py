def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)
def ft_find_char(char,str):
    d = ft_len(str)
    k = 0
    i = 0
    b = char
    while d > i:
        if str[i] == b:
            k = k + 1
        i = i + 1
    if k == 1:
        i = 0
        while d > i:
            if str[i] == b:
                return(i)
            i = i + 1
    elif k >= 2:
        i = 0
        max = k
        k = 0
        while d > i:
            if str[i] == b:
                k = k + 1
                if k == 1:
                    i1 = i
                if k == max:
                    i2 = i
            i = i + 1
        return i1,i2
    else:
        return False

print(ft_find_char( "a" ,'asdafdsfs'))