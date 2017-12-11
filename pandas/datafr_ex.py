import numpy as np;
import pandas as pd;

df = pd.read_csv('fin_dataset.csv',engine='python');

print(df.ix[2]);

print(df.columns);