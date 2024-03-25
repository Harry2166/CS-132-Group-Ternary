# THIS PYTHON SCRIPT IS FOR THE OVERALL CSVs.
# This python script is for reducing the raw data to only the unemployed data

import pandas as pd
import os

for root, dirs, files in os.walk(r'C:\Users\Admin\Desktop\GitHub Repos\second-year-second-sem-notes\cs132\raw-data'): # insert directory of where raw-data is stored
    # raw-data is a folder filled with other folders that contain the microdata and other related files from the LFS results
    reduced_root = root.split('\\')
    if len(reduced_root) == 9:
        # first gets the year and survey number and puts it into a tuple
        # the tuple is then joined together into one string
        # this format is guaranteed, some of the .csv files were not named appropriately and were renamed manually
        specifier = (reduced_root[-1].split("-")[3],reduced_root[-1].split("-")[4]) # from C:\Users\....\PHL-PSA-LFS-2016-Q1-PUF -> PHL-PSA-LFS-2016-Q1-PUF
        specifier = "-".join(specifier)
        # specifier is basically just telling you from which year and what no. of survey it is
    for file in files:
        # the folder will contain other files, but the raw data is stored in .csv or .CSV hence the if statement
        if file.endswith(".csv") or file.endswith(".CSV"):
            df = pd.read_csv(root + "\\" + file, on_bad_lines='skip',low_memory=False)
            (rows, cols) = df.shape
            df.insert(cols, "year-surveynum", specifier)

            # this is to rename the column of NEWEMPST to PUFNEWEMPSTAT so that we can have consistency
            df.rename(columns = {'NEWEMPST':'PUFNEWEMPSTAT'}, inplace = True) 

            # we will be basing unemployment based on this metric
            unemployed = df[(df["PUFNEWEMPSTAT"] == '2')]
            unemployed.to_csv(specifier + ".csv")
            print(specifier)