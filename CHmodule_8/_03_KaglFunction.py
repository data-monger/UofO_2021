# %%
# process
    # dependencies
import pandas as pd

# %%
def clean_kagl_df(df):
    df[df['adult'] == 'False'].drop('adult', axis='columns')

    # clean data types    
    df['budget']       = df['budget'].astype(int)
    df['id']           = pd.to_numeric(df['id'] , errors = 'raise')
    df['popularity']   = pd.to_numeric(df['popularity'], errors = 'raise')
    df['release date'] = pd.to_datetime(df['release_date'])

    return df


