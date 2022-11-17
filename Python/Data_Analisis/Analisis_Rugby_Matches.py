import pandas as pd
import numpy as np
from IPython.display import display_html


#pd.options.display.max_rows = 9999
#pd.options.display.max_info_columns = 9999
df = pd.read_csv('Resultados_internacionales_rugby.csv')
##df.dtypes
df['ganador']=np.where(df['home_score'] > df['away_score'] , 'home', np.nan)
display_html(df)
