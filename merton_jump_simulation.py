import numpy as np
import matplotlib.pyplot as plt


S0 = 100
time = 1
rate = 0.02
meanJump = 0
#standard deviation of jump
stdJump = 0.3
#number of jumps per annum
jumpIntensity = 5
steps = 252
#numbers of path simulated
n = 10
sigma = 0.2

def merton_jump_paths(S0, time, rate, sigma, jumpIntensity, meanJump, stdJump, steps, n):
    size = (steps, n)
    dt = time / steps
    poi_rv = np.multiply(np.random.poisson(jumpIntensity * dt, size=size), np.random.normal(meanJump, stdJump, size=size)).cumsum(axis=0)
    geo = np.cumsum(((rate - sigma ** 2 / 2 - jumpIntensity * (meanJump + stdJump ** 2 * 0.5)) * dt + sigma * np.sqrt(dt) * np.random.normal(size=size)), axis=0)

    return np.exp(geo + poi_rv) * S0


j = merton_jump_paths(S0, time, rate, sigma, jumpIntensity, meanJump, stdJump, steps, n)

plt.plot(j)
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()