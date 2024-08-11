def b_unidimensional(u,gU):
    gU = sp.sympify(gU)
    ec = gU.subs({x1: u[0], x2: u[1], x3:u[2]})
    derivada_ec = sp.diff(ec, l)
    sol = sp.solve(derivada_ec, l)
    sol_reales = [s.evalf() for s in sol if sp.im(s) == 0]
    if not sol_reales:
        return 'N'
    else:        
        min_valores = [ec.subs({l: i}).evalf() for i in sol_reales]
        l_min = sol_reales[min_valores.index(min(min_valores))]
    return l_min
