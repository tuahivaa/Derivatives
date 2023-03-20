import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

#df = yf.download("AAPL")
#test = np.log(1+df['Adj Close'].pct_change())
#testmu, testsigma = test.mean(), test.std()
#SP = np.random.normal(testmu,testsigma,252)
#i = df['Adj Close'].iloc[-1]
#si = i*(SP+1).cumprod()

#stock price a T0
S0 = 100
#drfit, expected daily return
mu = 0.0004
#volatility
sigma = 0.02
#legnth in days
n = 252

for i in range(1000):
    # simulate daily returns
    returns = np.random.normal(mu, sigma, n)
    prices = S0 * (returns + 1).cumprod()
    plt.plot(prices)
plt.axhline(S0,0)
plt.savefig("monte_carlo_simulation.png")
plt.show()