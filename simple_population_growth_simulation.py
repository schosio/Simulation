# the script is created in April 7, 2023
# the source of script is 
# https://towardsdatascience.com/building-simulations-in-python-a-complete-walkthrough-3965b2d3ede0

# define basic variables

# total population
totalPopulation = 50

# rate of growth in population 
growthFactor = 1.00005

# Day count to simulate growth on day scale
dayCount = 0 #Every 2 months the population is reported

# Loop to run till max population reach 1 million
while totalPopulation < 1000000:
    totalPopulation *= growthFactor
    #Every 56th day, population is reported
    dayCount += 1
    if dayCount == 56: 
        dayCount = 0
        print(totalPopulation)
