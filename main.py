import pandas as pd
import numpy as np

df = pd.DataFrame({
    'col1': np.random.randint(10,20,20),
    'col2': np.random.randint(10,20,20),
    'col3': np.random.randint(10,20,20),
})
print(df)