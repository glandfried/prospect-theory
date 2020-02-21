"""
   :copyright: (c) 2020 by Gustavo Landfried
   :license: BSD, see LICENSE for more details.   
"""

import os
name = os.path.basename(__file__).split(".py")[0]
##########

import numpy as np
from numpy.random import normal as rnorm
from matplotlib import pyplot as plt 


"""
When economists define expected-utility theory, they say it optimizes 
$E[u(t+\delta t)]$ (expected terminal utility).
That’s true, but $E[u(t+\delta t)]$ here is really short-hand for $E(\delta u)$, where

$$\delta u=u[x(t+\deltat)] - u[x(t)]$$

$t$ is the time now, and $t+\delta t$ is the time after the gamble. See Barberis 2013.
2/ Of course $\delta u \neq u(t+\delta t)$, but the idea is that we know our current wealth $x(t)$ and its utility $u[x(t)]$, and that's independent of any gamble on offer.

So we add the known constant $u[x(t)]$ to $\delta u$, and that indeed leaves us with $u[x(t+\delta t)]$.

But why are we allowed to do that?

3/ Well, adding a (deterministic) constant to $u$ makes no difference to decision theory. Why? Because decision theory is about ranking scalars, viz about whether

$$ E(\delta u) > E(\delta u\prime) $$

for utilities $u$ for one gamble and utilities $u\prime$ for another gamble.

4/ This inequality doesn't change if we add the constant $u[x(t)]$ on both sides (or any other constant), and therefore the corresponding decision theory predicts the same preferences as before.

5/ But this short-hand confuses people into thinking that $u[x(t)]$ and $x(t)$ are irrelevant, and that one can write $E(\delta u)$ as $E[u(\delta x)]$
But u(δx) is ill-defined without specifying x.

Descriptions of prospect theory often wrongly say that EUT has no reference-level dependence.
"""

x_t_dt = np.arange(1,101)/100
x_t = 0.1
def du(x_t_dt, x_t, u=np.log):
    return u(x_t_dt)-u(x_t)
u = np.log
#plt.plot(du(x_t_dt,x_t)-u(x_t_dt))
#plt.title("du \propto u_t_dt")

"""
But u(t+dt) is no proportional to u(dx)
"""
def dx(x_t_dt, x_t):
    return x_t_dt - x_t

line1 = plt.plot(x_t_dt,u(x_t_dt), label="    u(x[t+dt])",linestyle='--')
line2 = plt.plot(x_t_dt,u(dx(x_t_dt,x_t)), label="    u(x[t+dt]-x[t])",linestyle='-.')
line3 = plt.plot(x_t_dt,u(x_t_dt)-u(dx(x_t_dt,x_t)), label="    u([t+dt]) - u(x[t+dt]-x[t])" )
plt.title("u(t+dt) is not proportional to u(dx)")
# Create a legend for the first line.
plt.legend()

plt.savefig(name+".pdf",pad_inches =0,transparent =True,frameon=True)
plt.savefig(name+".png",pad_inches =0,transparent =True,frameon=True,dpi=90)
bash_cmd = "pdfcrop --margins '0 0 0 0' {0}.pdf {0}.pdf".format(name)
os.system(bash_cmd)

