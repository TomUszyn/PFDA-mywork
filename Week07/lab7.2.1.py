import seaborn as sns
import matplotlib.pyplot as plt
# load the dataset
dataset = sns.load_dataset('tips')
print(dataset.head())

sns.set_style('whitegrid')
#sns.lmplot(x='total_bill', y='tip', order=1, data=dataset)
#sns.scatterplot(x='total_bill', y='tip', data=dataset)
#sns.regplot(x='total_bill', y='tip', order=3, data=dataset)

# Create a scatter plot with a regression line for the dataset depending on time of day, sex and size of the party.
g=sns.relplot(x="total_bill", y="tip", kind="scatter", data=dataset, col="time", hue="sex", size="size")
# Apply regplot to each subplot in the FacetGrid
for ax in g.axes.flatten(): 
    sns.regplot(x="total_bill", y="tip", data=dataset, scatter=False, ax=ax, order=3)

# Set titles for each subplot 
g.set_titles(col_template="{col_name} Time", fontweight='bold')
# Set axis labels 
g.set_axis_labels("Total Bill", "Tip Amount", fontweight='bold')
# Add an overall title for the figure
plt.suptitle("Regression of Tip Amount vs. Total Bill by Time of Day, Sex, and Party Size", y=0.9, fontsize=12, fontweight='bold')
# Adjust layout to make space for the suptitle
plt.subplots_adjust(top=0.75)

# Create a scatter plot with a regression line for each day of the week in the dataset depending on sex.
#g=sns.relplot(x="total_bill", y="tip", kind="scatter", data=dataset, col="day", hue="sex")
# Apply regplot to each subplot in the FacetGrid
#for ax in g.axes.flatten(): 
#    sns.regplot(x="total_bill", y="tip", data=dataset, scatter=False, ax=ax, order=3)

plt.show()