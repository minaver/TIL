#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np

xl_file = "../Hw3/db_score.xlsx"
df = pd.read_excel(xl_file)

X = df.midterm
Y = df['final']

X_mean = X.mean()
Y_mean = Y.mean()

cov = np.mean((X - X_mean)*(Y - Y_mean)) # covariance (indicates the direation of linear relationship)
print(f"covariance : {cov}")

cor = cov / (X.std() * Y.std()) # correlation (indicates both the strength and direction of linear relationship)
print(f"correlation : {cor}")


# In[ ]:





# In[ ]:




