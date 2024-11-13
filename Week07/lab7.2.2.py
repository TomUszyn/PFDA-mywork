import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# load the dataset
dataset = sns.load_dataset('tips')
print(dataset.head())

# Create a figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot the first regplot
sns.regplot(x="size", y="tip", data=dataset, ax=axes[0])
axes[0].set_title('Simple regplot')

# Plot the second regplot with x_jitter
sns.regplot(x="size", y="tip", data=dataset, x_jitter=.05, ax=axes[1])
axes[1].set_title('regplot with x_jitter')

# Plot the third regplot with x_estimator
sns.regplot(x="size", y="tip", data=dataset, x_estimator=np.mean, ax=axes[2])
axes[2].set_title('regplot with x_estimator')

# Adjust layout
plt.tight_layout()
plt.show()
