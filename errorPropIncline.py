from IPython.core.display import Latex
from sympy import * 
def lprint(*args,**kwargs):
    """Pretty print arguments as LaTeX using IPython display system 
    
    Parameters
    ----------
    args : tuple 
        What to print (in LaTeX math mode)
    kwargs : dict 
        optional keywords to pass to `display` 
    """
    display(Latex('$$'+' '.join(args)+'$$'),**kwargs)

g, a, D, d, theta, Delta= symbols("g, a, D, d, theta, Delta")
dg, da, dD, dd, dtheta, dDelta = symbols("sigma_g, sigma_a, sigma_D, sigma_d, sigma_theta, sigma_Delta")


# Perimeter:
# Define relation, and print:
gexpr = a / sin(theta + Delta) * (1 + 2/5 * D**2 / (D**2 - d**2))

lprint(latex(Eq(symbols('g'),gexpr)))


dga = gexpr.diff(a) * da
dgD = gexpr.diff(D) * dD
dgd = gexpr.diff(d) * dd
dgtheta = gexpr.diff(theta) * dtheta
dgDelta = gexpr.diff(Delta) * dDelta
# Calculate uncertainty and print:
dg = sqrt(dga**2 + dgD**2 + dgd**2 + dgtheta**2 + dgDelta**2)
lprint(latex(Eq(symbols('sigma_g'), dg)))

eval_g = lambdify(args=(a, D, d, theta, Delta), expr=gexpr)
eval_eg = lambdify(args=(g, a, D, d, theta, Delta, da, dD, dd, dtheta, dDelta), expr=dg)
eval_egD = lambdify(args=(g, a, D, d, theta, Delta, da, dD, dd, dtheta, dDelta), expr=dgD) 
eval_egd = lambdify(args=(g, a, D, d, theta, Delta, da, dD, dd, dtheta, dDelta), expr=dgd) 
eval_egtheta = lambdify(args=(g, a, D, d, theta, Delta, da, dD, dd, dtheta, dDelta), expr=dgtheta) 
eval_egDelta = lambdify(args=(g, a, D, d, theta, Delta, da, dD, dd, dtheta, dDelta), expr=dgDelta) 

# Finding angle trigonometrically
h,l, dh,dl = symbols('h,l,sigma_h,sigma_l')
thetaexpr = atan(h/l)
lprint(latex(Eq(symbols('theta'),thetaexpr)))

dgh = thetaexpr.diff(h) * dh
dgl = thetaexpr.diff(l) * dl
dthetaexpr = sqrt(dgh**2 + dgl**2)
lprint(latex(Eq(symbols('sigma_theta'),dthetaexpr)))


eval_theta = lambdify(args=(h, l), expr=thetaexpr)
eval_etheta = lambdify(args=(h,l,dh,dl), expr=dthetaexpr)
eval_ethetah = lambdify(args=(h,l,dh,dl), expr=dgh)
eval_ethetal = lambdify(args=(h,l,dh,dl), expr=dgl)