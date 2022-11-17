import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display_html


##pd.options.display.max_rows = 9999
##pd.options.display.max_info_columns = 9999
df = pd.read_csv('drug_deaths.csv')

sns.displot(x=df["Age"], height=10, aspect=1, color='purple')
