import pandas as pd

df = pd.read_excel('esp.xlsx')

margin_threshold = 5000

df.style.apply(lambda x: ['background: red' if x < margin_threshold else 'background: green'\
    for x in df.cost], axis=0)

print(df)