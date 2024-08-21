import pandas as pd

df = pd.read_csv('test.csv')


subsequent_years = ['INDEX2014', 'INDEX2015', 'INDEX2016', 'INDEX2017', 
                    'INDEX2018', 'INDEX2019', 'INDEX2020', 'INDEX2021', 
                    'INDEX2022','INDEX20132014', 'INDEX20142015', 'INDEX20152016', 'INDEX20162017', 
                    'INDEX20172018', 'INDEX20182019', 'INDEX20192020', 
                    'INDEX20202021', 'INDEX20212022', 'INDEX20222023']


df['mean_subsequent_years'] = df[subsequent_years].mean(axis=1).round(2)


df['INDEX2011'] = df['INDEX2011'].fillna(df['mean_subsequent_years'])
df['INDEX2012'] = df['INDEX2012'].fillna(df['mean_subsequent_years'])
df['INDEX2013'] = df['INDEX2013'].fillna(df['mean_subsequent_years'])
df['INDEX20112012'] = df['INDEX20112012'].fillna(df['mean_subsequent_years'])


df = df.drop(columns=['mean_subsequent_years'])


df.to_csv('cleaned_dataset.csv', index=False)
