import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   # Read data from file
   df = pd.read_csv("epa-sea-level.csv")

   y_to_2050 = pd.Series(range(df.Year.max() + 1, 2050 + 1))

   # Create scatter plot
   fig, ax = plt.subplots()
   ax.scatter(df.Year, df["CSIRO Adjusted Sea Level"])

   # Create first line of best fit
   lr1 = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
   Years = pd.concat([df.Year, y_to_2050], axis=0)
   ax.plot(Years, Years*lr1.slope + lr1.intercept)

   # Create second line of best fit
   df_2000s = df[df.Year >= 2000]
   lr2 = linregress(df_2000s.Year, df_2000s["CSIRO Adjusted Sea Level"])
   Years_2000s = pd.concat([df_2000s.Year, y_to_2050], axis=0)
   ax.plot(Years_2000s, Years_2000s*lr2.slope + lr2.intercept)

   # Add labels and title
   ax.set_xlabel("Year")
   ax.set_ylabel("Sea Level (inches)")
   ax.set_title("Rise in Sea Level")
   
   # Save plot and return data for testing
   plt.savefig('sea_level_plot.png')
   return plt.gca()