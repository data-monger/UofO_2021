import json as js
import pandas as pd

# process
    # files
file_dir = 'Resources'

def load_csv (csv):
    csv = pd.read_csv(f'{file_dir}/{csv}', low_memory=False)
    return csv
        
def load_jsn(jsn):
    with open(f'{file_dir}/{jsn}') as file:
        jsn = js.load(file)
    jsn_raw = [movie for movie in jsn]
    jsn = pd.DataFrame(jsn)

    return jsn, jsn_raw