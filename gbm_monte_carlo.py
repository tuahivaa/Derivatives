import math
import numpy as np
import matplotlib.pyplot as plt

#setup parameters
S0 = 100
mu = 0.35
sigma = 0.4
paths = 10
time = 1
dt = 1/252

price_paths = []

def gbm(S0, mu, sigma, dt, time):
    prices = []
    while (time - dt > 0):
        Wt = np.random.normal(0, math.sqrt(dt))
        Xt = mu * dt + sigma * Wt
        S0 += Xt
        prices.append(S0)
        time -= dt
    return prices

for i in range (0,paths):
    price_paths.append(gbm(S0,mu,sigma,dt,time))

# Visualizing GBM
plt.figure(figsize=(20, 10))
plt.xlabel('Time')
plt.ylabel('Price')

for price_path in price_paths:
    plt.plot(price_path)
plt.show()