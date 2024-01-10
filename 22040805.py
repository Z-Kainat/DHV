# Save this code in a file named 22040805.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter, FuncFormatter

# Load the data from a CSV file in the local folder
df = pd.read_csv('world_population.csv')

# Additional code snippet
# Filter the DataFrame for the Asia continent
asia_df = df[df['Continent'] == 'Asia']

# Sort the DataFrame by population in descending order
sorted_asia_df = asia_df.sort_values(by='2022 Population', ascending=False)

# Select the top 5 countries
top5_asia_df = sorted_asia_df.head(5)

# Create a bar chart
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(x='2022 Population', y='Country/Territory', data=top5_asia_df)

# Add population annotations
for index, value in enumerate(top5_asia_df['2022 Population']):
    bar_plot.text(value, index, f'{value:,}', va='center', fontsize=15, color='black', fontweight='bold')
# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Country', fontweight='bold')
plt.xlabel('Population', fontweight='bold')

# Remove the grid
sns.despine()

plt.show()

# Continue with the existing code

# Aggregate population values for each continent
aggregated_df = df.groupby('Continent')[['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']].sum().reset_index()

# Rename columns to remove spaces
aggregated_df.columns = ['Continent', '2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']

# Melt the DataFrame to have 'Year' and 'Population' columns
melted_df = pd.melt(aggregated_df, id_vars='Continent', var_name='Year', value_name='Population')

# Set the style for seaborn
sns.set(style="whitegrid")

# Create a line plot for population increase by continent over the years
plt.figure(figsize=(12, 8))
plot = sns.lineplot(x='Year', y='Population', hue='Continent', data=melted_df, palette='dark', linewidth=2.5)

# Reverse the x-axis
plt.gca().invert_xaxis()

# Format y-axis ticks to display values in millions
def format_millions(value, _):
    return f'{value / 1e6:.0f}M'

plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Population', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
# Remove the title
plt.title('')

# Show --- grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Move legend inside the graph without box and bold legend text
legend = plt.legend(title='Continent', loc='upper left', frameon=False)
for text in legend.get_texts():
    text.set_fontweight('bold')

# Save the plot as a PNG file
plt.savefig("22040805.png", dpi=300)
plt.show()

# Filter the DataFrame for the year 2022
population_2022 = df[['Continent', '2022 Population']].groupby('Continent').sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
wedges, _, _ = plt.pie(population_2022['2022 Population'], labels=None, autopct='', startangle=140, colors=plt.cm.tab10.colors)

# Add legend with percentages
plt.legend(wedges, [f'{label} ({percentage:.1f}%)' for label, percentage in zip(population_2022.index, 100 * population_2022['2022 Population'] / population_2022['2022 Population'].sum())], title='Continent', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Save the plot as a PNG file
plt.savefig("22040805.png", dpi=300)
plt.show()

# Sort the DataFrame by world population in descending order
sorted_world_df = df.sort_values(by='2022 Population', ascending=False)

# Select the top 5 countries
top5_world_df = sorted_world_df.head(5)

# Calculate the percentage of world population for each country using assign to avoid warning
world_population_2022 = df['2022 Population'].sum()
top5_world_df = top5_world_df.assign(Percentage_of_World_Population=top5_world_df['2022 Population'] / world_population_2022 * 100)

# Create a bar chart for the percentage of world population
plt.figure(figsize=(10, 6))
bar_plot = sns.barplot(x='Country/Territory', y='Percentage_of_World_Population', data=top5_world_df, hue='Country/Territory', palette='viridis', legend=False)  # Use hue instead of palette

# Add percentage annotations
for index, value in enumerate(top5_world_df['Percentage_of_World_Population']):
    bar_plot.text(index, value, f'{value:.2f}%', ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

# Bold the axis values and label
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Percentage of World Population', fontweight='bold')
plt.xlabel('Country', fontweight='bold')

# Save the plot as a PNG file
plt.savefig("22040805.png", dpi=300)
plt.show()
