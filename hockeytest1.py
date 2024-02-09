# Load modules
import pandas as pd
#import openpyxl
import matplotlib.pyplot as plt
import time
import timeit

# Start time
st = time.time()

# Load Excel sheet
nhl_data = pd.read_excel('Summary_NHl_Scoring.xlsx',index_col=0)


# Review first few entries
print(nhl_data.head())

# Create summary stats
print(nhl_data.describe())

# Check data types
print(nhl_data.dtypes)


print(nhl_data)

# Make scatter plot

#scatter1 = plt.scatter(nhl_data['TOI/GP'],nhl_data['P/GP'])
#plt.show()

# End time
et = time.time()

# Calculate total time
elapsed_time = et - st
print("Execution time:", elapsed_time, "seconds")

# Use timeit
n = 5
result = timeit.timeit(globals=globals(), number=n)
print(f"Execution time is {result / n} seconds")