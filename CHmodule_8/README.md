# Module 8 | Assignment - Extract, Transform, and Load (ETL)

Perform ETL on several movie datasets to predict popular films for a streaming service.

## Deliverable 1
Three data files are passed into function:

code file: 00_DataProcessing.ipynb (this runs the load_file function)
code png : 01 load_file FUNCTION.png (this is the function)

### read in files and convert to data frames
wiki_movies_raw_df, wiki_movies_raw_ls = read.load_jsn('/wikipedia_movies.json')
kagl_movies_raw_df = read.load_csv('/movies_metadata.csv')
rate_movies_raw_df = read.load_csv('/ratings.csv')

code file: 01_ReadDataFunction.ipynb (this is the function)
code png : 01 load_file FUNCTION.png (this is the png of the code)

## Deliverable 2
Tv shows are filtered
try-except block to catch errors
tasks for extract on wiki-files is completed
wiki data-frame is created (see Deliverable 1)
wiki data-frame is displayed (see cleaned_wiki_df DISPLAYED.png)

### tv shows are filtered / all tasks ran
00_DataProcessing.ipynb (this runs the wiki_clean function)
code file: _02_WikiFunction.py (this is the function)
code png : 02 All tasks FUNCTION

## Deliverable 3
meta data cleaned / all four tasks completed
data frames are merged
new merged dataframe
display kaggle dataframe
display ratings dataframe

### meta data cleaned - four tasks
code file: 00_DataProcessing.ipynb (this runs the clean kagl function)
code file: _03_Kagl_Function.py (this is the function)

### data frames are merged
code file: 00_DataProcessing.ipynb (this creates new dataframe from the merged cleaned wiki and kagl data frames)

### display kagl, ratings, and new merged dataframe
code png : 03 cleaned_kagl_df DISPLAYED.png
code png : 03 cleaned_rate_df DISPLAYED.png
code png : 03 merged_df DISPLAYED.png

## Deliverable 4
the data in the movies db is replaced
ratings table is dropped and rating file added
elapsed time displayed

code png : 04 Elapsed_Time.png
code png : 04 public_movies.png
code png : 04 public_ratings count.png

code png : 04 Movies_table_PROOF OF LIFE.png
code png : 04 Ratings_table_PROOF OF LIFE.png

## Overview
To produce an ETL product that is modular, easy to modify and maintain, scales, and provides opportunities to modify in the future for other ETL projects.

## File Summary
The code base consists of 4 files:

### 00_DataProcessing.ipynb
This runs the entire process from start to finish. It probably would have made sense to include a 5th file, for the dB connection and push commands; for the sake of simplicity and 'proof of concept', we've demonstrated we can run functions within a script, or call them from outside a script. Perhaps there will be instances where we want to call a function from within a script; This provides us the framework to do that.

### _01_ReadDataFunction.py
This reads csv and jason files. Should we require to read other files, we can expand upon this to read excel files for instance- or even xml files if necessary.

### _02_WikiFunction.py
This cleans the wiki data. There is a main function that calls each clean-process; this way we can add, remove, or change existing sub functions to suit our needs. In addition, we can create a new function for each data-source we wish to cleanse. The advantage is we won't be required to change the existing code base. we can simply call the new data-source funtion from our DataProcessing script.

And if we require this wiki-function for another process or load, we can re-use this.

### _03_KaglFunction.py
This cleans the kaggle data. A great example of changing data types. The above potential also exists for this, as we can add if necessary, or simply copy and rename and use for other data-sources.


## Summary
There are still additional aspects of this we could auto-mate in the future- namely data retrieval and storage, generating a file structure to accomodate files with the same name (automated exports from external systems) that arrive on different days. Using RegEx, we can parse month, day and year, to automate storage process for a given client or data-provider.

The above code lends itself to this aforementioned scalability.