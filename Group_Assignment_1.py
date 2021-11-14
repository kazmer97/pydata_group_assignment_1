# Question 1

import sys
import os
from typing import List

## a
boeing_data = "BA.csv"

with open(boeing_data, 'r') as f:
    data = f.readlines()


print(data)

header = data[0]
allData = data[1:]

N = len(allData)

prices = []
dates = []

for line in allData:
    prices.append(float(line.split(',')[1]))
    dates.append(line.split(',')[0])

## b

def moving_average(data: list[float], n: int) -> list[float]:
    """
    Calculates the moving average of a list of numbers
    :param data: list of numbers
    :param n: number of days
    :return: list of moving averages
    """
    moving_average = [None]*(n-1)
    for i in range(n, len(data)+1):
            moving_average.append(sum(data[i-n:i])/len(data[i-n:i]))
    return moving_average


## c
prices_dummy = [2,3,4,5,8,5,4,3,2,1]
moving_average(prices_dummy, 3)

## d

ma_252 = moving_average(prices, 252)

## e

ma_252[251:253]
### First moving average is 119.15963196031755

## f

ma_60 = moving_average(prices, 60)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plt.plot(prices,'-go', label='Prices')
plt.plot(ma_252, 'b-', label = "ma_252")
plt.plot(ma_60, 'm-', label = "ma_60")
plt.title('Boeing 252-day Moving Average', fontsize = 20) plt.xlabel('Time Step', fontsize = 15)
plt.ylabel('Adjusted Closing Price', fontsize = 15) plt.autoscale(enable = True, tight = True) # or for specific axis axis='x'
plt.legend(loc = "upper left", fontsize = 15)
plt.show()


# Q2

## a

busDays = 252
rf = 0.011555

## b
import math
R = []
for i in range(1,len(prices)):
    R.append(math.log(prices[i]/prices[i-1]))

## c
muR = 0
for i in range(len(R)):
    muR += R[i]

muR = muR/len(R)

muR_annual = muR*busDays

## d

sigmaR = 0
varR = []
sigmaR_annual = []

for i in range(len(prices)-1):
    varR.append(R[i]-muR)

for i in range(len(prices)-1):
    sigmaR += varR[i]**2

sigmaR = math.sqrt(sigmaR/(len(prices)-1))

sigmaR_annual = sigmaR*math.sqrt(busDays)

## e

lowPt = prices[0]
highPt = prices[0]

for i in prices:
    if i > highPt:
        highPt = i
    if i < lowPt:
        lowPt = i


## f

SR = (muR_annual - rf)/sigmaR_annual

## g

print("The annualized return is:", muR_annual)
print("The annualized standard deviation is:", sigmaR_annual)
print("The daily standard deviation is", sigmaR)
print("The sharpe ratio is:", SR)
print("Daily mean log Return is:",muR)
### Sharpe ratio is around 0.12, which is smaller than 1, 
### so consider as sub-optimal and not a good investment

## h

"""
muR: 0.0002608959797437571
muR_annual: 0.0657457868954268
sigmaR: 0.0.02843688980272897
sigmaR_annual: 0.0657457868954268
SR = 0.12004472800983401
"""
