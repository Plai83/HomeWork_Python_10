import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

for name_col in set(lst):
    att_temp = [1 if z == name_col else 0 for z in data['whoAmI'].tolist()]
    data[name_col] = att_temp

new_df = data[list(set(lst))]
print(new_df)
