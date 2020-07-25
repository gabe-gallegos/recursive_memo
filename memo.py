def fib(n):
    
    # creates empty dict
    d = {}
    
    # seperate a dict and n if there's already a dict
    if "{" in str(n):
        d = eval(n[n.index("{"):])
        n = int(n[:n.index("{")])
        
    # memoization
    if n in d:
        return str(d[n]) + str(d)
    
    # 0 or 1
    if n == 0 or n == 1:
        return str(1)+"{0:1,1:1}"
    
    
    if n not in d:
        # get return value from n-1 (leftmost branch)
        x = fib(str(n-1)+str(d))
        
        # change d to x's d
        d = eval(x[x.index("{"):])
        
        # update then return
        d[n] = d[n-1] + d[n-2]
        return str(d[n])+str(d)
