def b_armijo(fA,x0_):
    fA = sp.sympify(fA)
    s = 1.1
    beta = 1/2
    sigma = 1/2
    m=0
    x0_=np.array(x0_)
    grad = [sp.diff(fA, var) for var in (x1, x2, x3)]
    grad_func = sp.lambdify((x1,x2,x3), grad)
    grad_eval = grad_func(*x0_)
    d=-1*np.array(grad_eval)
    res1 = fA.subs({x1:x0_[0],x2:x0_[1],x3:x0_[2]})
    mod=np.dot(np.array(grad_eval).T,d)
    total_armijo = 0
    while True:
        eval={x1:x0_[0]+(s*beta**m)*d[0],x2:x0_[1]+(s*beta**m)*d[1],x3:x0_[2]+(s*beta**m)*d[2]}
        res2 = fA.subs(eval)
        res3=(-sigma*s*beta**m)*mod
        if(res1-res2 >= res3):
            return s*beta**m,m
        else:

            m=m+1
