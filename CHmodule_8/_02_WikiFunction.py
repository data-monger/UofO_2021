# %%
# process
    # dependencies
    
import pandas   as pd
import numpy    as np
import re       as regex

# %%
# regex
    # dollars (__c = currency)
reg_one__c = r'\$\s*\d+\.?\d*\s*[mb]illion'
reg_two__c = r'\$\s*\d{1,3}(?:[,\.]\d{3})+(?!\s[mb]illi?on)'

    # dates (__d = date)
reg_one__d = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s[123]?\d,\s\d{4}'
reg_two__d = r'\d{4}.[01]\d.[0123]\d'
reg_thre_d = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'
reg_four_d = r'\d{4}'

    # time (__t = time)
reg_one__t = r'(\d+)\s*ho?u?r?s?\s*(\d*)|(\d+)\s*m'

# %%
def clean_wiki_df (raw_df, ls):
    
    df = raw_df

        # keep columns
    wiki_columns_to_keep = [column for column in df.columns if df[column].isnull().sum() < len(raw_df) * 0.9]
    df = df[wiki_columns_to_keep]

    df = clean_movie(ls)

    df['index_'] = range(1, len(df) + 1)
    df.set_index('index_', inplace=True)

        # clean imdb_id
    df = clean_imdb(df)

        # box office data
    df = clean_box_office(df)

        # budget data
    df = clean_budget(df)

        # release date data
    df = clean_release_date(df)

        # run time data
    df = clean_run_time(df)

    return df


#%%
def clean_movie(ls):
    wiki_movies = [movie for movie in ls
                if ('Director' in movie or 'Directed by' in movie)
                    and 'imdb_link' in movie
                    and 'No. of episodes' not in movie]
    clean_movies= [clean_movie_ls(movie) for movie in wiki_movies]
    df = pd.DataFrame(clean_movies)
    
    return df

#%%

def clean_movie_ls(ls):

    movie = dict(ls) #create a non-desrtuctive copy

    alt_titles= {}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
            'Hangul','Hebrew','Hepburn','Japanese','Literally',
            'Mandarin','McCune–Reischauer','Original title','Polish',
            'Revised Romanization','Romanized','Russian',
            'Simplified','Traditional','Yiddish']:

        if key in movie:
            alt_titles[key] = movie[key]
            movie.pop(key)
            
    if len(alt_titles) > 0:
        movie['alt_titles'] = alt_titles
    
    def change_column_name(old_name, new_name):
        if old_name in movie:
            movie[new_name] = movie.pop(old_name)

    # consolidate column names and standardize
    change_column_name('Directed by', 'Director')
    change_column_name('Adaptation by', 'Writer(s)')
    change_column_name('Country of origin', 'Country')
    change_column_name('Directed by', 'Director')
    change_column_name('Distributed by', 'Distributor')
    change_column_name('Edited by', 'Editor(s)')
    change_column_name('Length', 'Run time')
    change_column_name('Original release', 'Release date')
    change_column_name('Music by', 'Composer(s)')
    change_column_name('Produced by', 'Producer(s)')
    change_column_name('Producer', 'Producer(s)')
    change_column_name('Productioncompanies ', 'Production company(s)')
    change_column_name('Productioncompany ', 'Production company(s)')
    change_column_name('Released', 'Release Date')
    change_column_name('Release Date', 'Release date')
    change_column_name('Running time', 'Run time')
    change_column_name('Written by', 'Writer(s)')
    change_column_name('Screen story by', 'Writer(s)')
    change_column_name('Screenplay by', 'Writer(s)')
    change_column_name('Story by', 'Writer(s)')
    change_column_name('Theme music composer', 'Composer(s)')

    return movie


# %%
def clean_dollars(column):
    # if s is not a string, return NaN
    if type(column) != str:
        return np.nan

    # if input is of the form $###.# million
    if regex.match(r'\$\s*\d+\.?\d*\s*milli?on', column, flags=regex.IGNORECASE):

        # remove dollar sign and " million"
        column = regex.sub('\$|\s|[a-zA-Z]','', column)

        # convert to float and multiply by a million
        value = float(column) * 10**6

        # return value
        return value

    # if input is of the form $###.# billion
    elif regex.match(r'\$\s*\d+\.?\d*\s*billi?on', column, flags=regex.IGNORECASE):

        # remove dollar sign and " billion"
        column = regex.sub('\$|\s|[a-zA-Z]','', column)

        # convert to float and multiply by a billion
        value = float(column) * 10**9

        # return value
        return value

    # if input is of the form $###,###,###
    elif regex.match(r'\$\s*\d{1,3}(?:[,\.]\d{3})+(?!\s[mb]illion)', column, flags=regex.IGNORECASE):

        # remove dollar sign and commas
        column = regex.sub('\$|,','', column)

        # convert to float
        value = float(column)

        # return value
        return value

    # otherwise, return NaN
    else:
        return np.nan


# %%
def clean_imdb(df):
 
    df['imdb_id'] = df['imdb_link'].str.extract(r'(tt\d{7})')
    df.drop_duplicates(subset='imdb_id', inplace=True)

    return df


# %%
def clean_box_office(df):    
  
    df['Box office'] = df['Box office'].dropna()
    df['Box office'] = df['Box office'].apply(lambda x: ' '.join(x) if type(x) == list else x)
    df['Box office'] = df['Box office'].str.replace(r'\$.*[-—–](?![a-z])', "$", regex=True)

    df['Box office'] = df['Box office'].str.extract(f'({reg_one__c}|{reg_two__c})', flags=regex.IGNORECASE)[0].apply(clean_dollars)

    return df

# %%
def clean_budget(df):
 
    df['Budget'] = df['Budget'].dropna()
    df['Budget'] = df['Budget'].map(lambda x: ' '.join(x) if type(x) == list else x)
    df['Budget'] = df['Budget'].str.replace(r'\$.*[-—–](?![a-z])', "$", regex=True)   
    df['Budget'] = df['Budget'].str.replace(r'\[\d+\]\s*', '')

    df['Budget'] = df['Budget'].str.extract(f'({reg_one__c}|{reg_two__c})', flags=regex.IGNORECASE)[0].apply(clean_dollars)

    return df

# %%
def clean_release_date(df):

    df['Release date'] = df['Release date'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)
    df['Release date'] = pd.to_datetime(df['Release date'].str.extract(f'({reg_one__d}|{reg_two__d}|{reg_thre_d}|{reg_four_d})')[0], infer_datetime_format=True)   
    
    return df

# %%
def clean_run_time(df):

    df['Run time'].dropna().apply(lambda x: ' '.join(x) if type(x) == list else x)
    column_extract = df['Run time'].str.extract(f'({reg_one__t})', flags=regex.IGNORECASE)
    column_extract = column_extract.apply(lambda col: pd.to_numeric(col, errors='coerce')).fillna(0)
    
    df['Run time'] = column_extract.apply(
                        lambda row: row[3] 
                            if row[0]==0 and row[1]==0 and row[2] == 0 else row[0]*60 + row[1] 
                            if row[0]==0 and row[1]==0 else row[2], axis=1) 

    return df




