import pandas as pd
import matplotlib.pyplot as plt
#from scipy.stats import linregress
import scipy as scp
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', ax=ax)

    # Create first line of best fit
    reg_complete = scp.stats.linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    original_years_line = np.arange(1880, 2051)
    ax.plot(original_years_line, reg_complete.intercept + reg_complete.slope*original_years_line)

    # Create second line of best fit
    recent_years = df.loc[df['Year'] >= 2000, 'Year']
    recent_values = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']
    reg_recent = scp.stats.linregress(x=recent_years, y=recent_values)
    recent_years_line = np.arange(2000, 2051)
    ax.plot(recent_years_line, reg_recent.intercept + reg_recent.slope*recent_years_line)

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_ylabel("Sea Level (inches)")
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()