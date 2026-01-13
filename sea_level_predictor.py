import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
               color='blue', s=50, alpha=0.6, edgecolors='black', linewidth=0.5, label='Original Data')
    
    # Create first line of best fit (all data from 1880)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate years from 1880 to 2050
    years_all = np.arange(1880, 2051)
    sea_level_all = slope * years_all + intercept
    
    ax.plot(years_all, sea_level_all, 'r-', linewidth=3, label=f'Fit: 1880-2013 (slope={slope:.4f})')
    
    # Create second line of best fit (from 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    
    if len(df_recent) > 1:  # Ensure we have enough data points
        slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
            df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
        )
        
        # Generate years from 2000 to 2050
        years_recent = np.arange(2000, 2051)
        sea_level_recent = slope_recent * years_recent + intercept_recent
        
        ax.plot(years_recent, sea_level_recent, 'g-', linewidth=3, 
                label=f'Fit: 2000-2013 (slope={slope_recent:.4f})')
    
    # Add labels and title
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Sea Level (inches)', fontsize=14)
    ax.set_title('Rise in Sea Level', fontsize=16, fontweight='bold')
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Add prediction values for 2050
    ax.axvline(x=2050, color='gray', linestyle=':', alpha=0.5)
    
    # Annotate predictions
    prediction_2050_all = slope * 2050 + intercept
    prediction_2050_recent = slope_recent * 2050 + intercept_recent
    
    ax.text(2050, prediction_2050_all, f' {prediction_2050_all:.1f}"', 
            verticalalignment='bottom', fontsize=10, color='red')
    ax.text(2050, prediction_2050_recent, f' {prediction_2050_recent:.1f}"', 
            verticalalignment='top', fontsize=10, color='green')
    
    plt.tight_layout()
    
    # Save plot and return data for testing (DO NOT MODIFIED)
    plt.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
    return plt.gca()