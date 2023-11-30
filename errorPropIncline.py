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
g, a, D, d, theta, Delta= symbols("g, a, D, d, theta, Delta")
dg, da, dD, dd, dtheta, dDelta = symbols("sigma_g, sigma_a, sigma_D, sigma_d, sigma_theta, sigma_Delta")

# Perimeter:
# Define relation, and print:
g = a / sin(theta + Delta) * (1 + 2/5 * D**2 / (D**2 - d**2))
lprint(latex(Eq(symbols('g'),g)))

# Calculate uncertainty and print:
dg = sqrt(g.diff(a)**2 * da**2 + g.diff(D)**2 * dD**2 + g.diff(d)**2 * dd**2 + g.diff(theta)**2 * dtheta**2 + g.diff(Delta)**2 * dDelta**2)
lprint(latex(Eq(symbols('sigma_g'), dg)))
