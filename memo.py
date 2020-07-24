def fib(n):

    d = {}

    # seperate a dict and n
    if "{" in str(n):
        d = eval(n[n.index("{"):])
        n = int(n[:n.index("{")])

    # if in dict
    if n in d:
        return str(d[n]) + str(d)

    # 1 or 0
    if n == 1 or n == 0:
        d = {n:1}
        return str(1)+str(d)


    if n not in d:
        # get return value from n-1
        x = fib(str(n-1)+str(d))
        xd = eval(x[x.index("{"):])
        d = xd

        # get return value from n-2
        y = fib(str(n-2)+str(d))

        #if there are any values that are in x d and y d that you dont have in your d, steal their d's

        xd = eval(x[x.index("{"):])
        yd = eval(y[y.index("{"):])

        for key in xd:
            if key not in d:
                d[key] = xd[key]

        for key in yd:
            if key not in d:
                d[key] = yd[key]

        d[n] = int(x[:x.index("{")]) + int(y[:y.index("{")])
        return str(d[n])+str(d)
