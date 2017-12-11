import numpy as np;
import pandas as pd;

dataframe = pd.read_csv('dataset.csv',header=None);

print(dataframe.info());
print(dataframe.head());

m = dataframe.as_matrix();
print(m);
print('------');
print(dataframe[0]);
print('------');
print(dataframe[[0,2]]);
print('------');
print(dataframe.ix[0]);

print(dataframe[ dataframe[0] < 1]);