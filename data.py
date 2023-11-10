import pandas as pd
import numpy as np

df = pd.read_csv('RUUUUI.csv')
a = df.to_numpy()

a = np.array(df).reshape(5,2)
print(a)