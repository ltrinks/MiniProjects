# Lauren Trinks March 30

# Data from FiveThirtyEight's repository found here https://github.com/fivethirtyeight/data
# their citations are in the readme for this section of the repository

# This data seems very important especially with the rise of reported hate crimes against Asian Americans.
# it should be noted this data set was last updated on Jan 24, 2017. So this dataset does not give a full picture
# about what is happening in 2021.

# I am exploring this data to see if I can find any trends in the data myself.

import pandas as pd
import matplotlib.pyplot as plt

# read in the data and sort it by chosen data
crimes = pd.read_csv("hate_crimes.csv")

# by hate crimes
statesByCrimes = crimes.sort_values(by = "avg_hatecrimes_per_100k_fbi")
statesByCrimes = statesByCrimes.reset_index()

# by gini https://en.wikipedia.org/wiki/Gini_coefficient
statesByGini = crimes.sort_values(by = "gini_index")
statesByGini = statesByGini.reset_index()

# by high school education
statesByEd = crimes.sort_values(by = "share_population_with_high_school_degree")
statesByEd = statesByEd.reset_index()

# get the 10 states with the most hate crimes
mostCrimes = []
for i in range(10):
    mostCrimes.append(statesByCrimes['state'][i])

# get the 10 states with the most income inequality
mostInequality = []
for i in range(10):
    mostInequality.append(statesByGini['state'][i])

# get the 10 states with the least education
leastEducation = []
for i in range(10):
    leastEducation.append(statesByEd['state'][statesByEd.shape[0] - 1 - i])

# find the states that are in all of three of these lists
sharedTraits = []
for state in mostCrimes:
    if (state in mostInequality) or (state in leastEducation):
        sharedTraits.append(state)

print("The states that are in the top 10 for multiply categories are: " + str(sharedTraits))
print("Wyoming was number 1 for hate crimes and least high school education, and it was number 3 in income inequality.")
print("Education and wealth inequality seem to be factors for some of the states, but other factors must dictate" \
      " the rate of hate crimes more directly.")


