import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[
(df['value'] >= df['value'].quantile(0.025)) &
(df['value']<= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    def draw_line_plot():
    plt.plot('date', 'value')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = 16, fontweight = 'bold', color = 'red')
    plt.xlabel('Date', fonsize = 12, color = 'green')
    plt.ylabel('Page Views', fontsize = 12, color = 'orange')
    plt.show()
   

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df = df.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().reset_index()
    df_pivot = df_bar.pivot(index = 'year', columns = 'month', values = 'value')
    import calendar
    month_names = {i: calendar.month_name[i] for i in range (1,13)}

    # Draw bar plot
    fig, ax = plt.sublots(figsize=(12,8))
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views per Month', fontsize=16, fontweight='bold')
    ax.set_xlabel('Years', fontsize = 12, color = 'red')
    ax.set_ylabel('Average Page Views', fontsize = 12, color = 'blue')
    legend = ax.legend(
    labels=[month_names[i] for i in df_pivot.columns],  
    title='Months', 
    title_fontsize=14, 
    fontsize=10)
    legend.get_title().set_color('purple')
    legend.get_title().set_fontweight('bold')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
