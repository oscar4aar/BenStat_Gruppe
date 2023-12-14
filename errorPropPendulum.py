import numpy as np                                     # Matlab like syntax for linear algebra and functions
import matplotlib.pyplot as plt                        # Plots and figures like you know them from Matlab
import seaborn as sns                                  # Make the plots nicer to look at
from iminuit import Minuit                             # The actual fitting tool, better than scipy's
import sys                                             # Modules to see files and folders in directories

from IPython.core.display import Latex

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


# Import SymPy: 
from sympy import * 
    
# Define variables:
g, L, T= symbols("g, L, T")
dg,dL,dT = symbols("sigma_g, sigma_L, sigma_T")

# Perimeter:
# Define relation, and print:
g = L * ((2 * pi)/T)**2
lprint(latex(Eq(symbols('g'),g)))

# contribution of L and T
delta_T = g.diff(T) * dT
delta_L = g.diff(L) * dL

# Calculate uncertainty and print:
dg = sqrt(g.diff(L)**2 * dL**2 + g.diff(T)**2 * dT**2)
lprint(latex(Eq(symbols('sigma_g'), dg)))

eval_g = lambdify(args=(T, L), expr=g)
eval_eg = lambdify(args=(T, L, dT, dL), expr=dg)
eval_dT = lambdify(args=( T, L, dT, dL), expr=delta_T)
eval_dL = lambdify(args=( T, L, dT, dL), expr=delta_L)
