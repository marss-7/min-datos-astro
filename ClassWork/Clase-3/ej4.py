import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

sns.kdeplot(data=df, x='bill_length_mm', y='bill_depth_mm', fill=True, hue='species')

plt.title('penguins uwu')
plt.show()
