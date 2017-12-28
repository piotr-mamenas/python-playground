import numpy as np;
import pandas as pd;
from datetime import datetime;

df = pd.read_csv('fin_dataset.csv',engine='python');

print(df.ix[2]);

print(df.columns);

df['Timestamp'] = df.apply(lambda df: datetime.strptime(df['Timestamp'],'%Y-%m-%d'), axis=1);

#matrix = df.as_matrix();
#print(matrix);