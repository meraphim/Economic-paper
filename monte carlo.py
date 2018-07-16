#
# Monte Carlo valuation of European call options with pure python
# mcs pure_python.py
#
from time import time
from math import exp, sqrt, log
from random import gauss, seed
seed(20000)
t0 = time()
# Parameters
S0 = 100. # inìtial value
K = 105. # str~ke price
T = 1.0 # maturlty
r = 0.05 # riskless short rate
sigma = 0.2 #νolatility
M = 50 # number of time steps
dt = T/M # length of time interval
I = 250000 # number of paths
# Simulating 1 paths with M time steps
S = []
for i in range(I):
    path = []
    for t in range( M + 1) :
        if t == 0:
             path.append(S0)
        else :
             z = gauss(0.0, 1.0)
             St = path[t - 1] * exp(( r - 0.5 *sigma ** 2) * dt
                                     + sigma * sqrt(dt)* z)
             path.append(St)
    S.append(path)
# Calculating the Monte Carlo estimator
C0 = exp(-r * T) * sum([max(path[-1] - K, 0) for path in S]) / I
# Results output
tpy = time() - t0
print("European option Va1ue %7.3f" % C0)
print ("Duration in Seconds %7.3f" % tpy)