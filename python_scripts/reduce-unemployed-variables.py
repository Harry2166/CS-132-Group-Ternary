# THIS PYTHON SCRIPT IS FOR THE UNEMPLOYED ONLY CSVs.
# This python script is responsible for reducing the csvs to the variables needed

import pandas as pd
import os

# these are the data that we are going to need
data = [
"PUFREG", # region
'PUFURB2015', # urban or rural
'PUFC03_REL', # relationship to head of house
'PUFC04_SEX', # sex
'PUFC05_AGE', # age
'PUFC06_MSTAT', # marital status
'PUFC07_GRADE', # highest grade completed
'PUFC26_WYNOT', # why no work
'PUFC41_POCC', # previous occupation
'PUFNEWEMPSTAT', # unemployed stat
'year-surveynum', # year and what number of survey it is
"unemployment_rate", # unemployment rate for the year and survey number
]

# this is for 2016-Q1 because it has the most number of variable names that differ from others
to_be_replaced = {
    "PUFREG" : "REG",
    "PUFURB2015" : "URB2K70",
    "PUFC03_REL" : "C05_REL",
    "PUFC04_SEX" : "C06_SEX",
    "PUFC05_AGE" : "C07_AGE",
    "PUFC06_MSTAT" : "C08_MS",
    "PUFC07_GRADE" : "J12C09_GRADE",
    "PUFC26_WYNOT" : "C42_WYNT",
    "PUFC41_POCC" : "C45_POCC",
    "PUFNEWEMPSTAT" : "NEWEMPST"
}

# collected manually
unemployment_rate = {
    "2016-Q1" : 5.8,
    "2016-Q2" : 6.1,
    "2016-Q3" : 5.4,
    "2016-Q4" : 4.7,
    "2017-Q1" : 6.6,
    "2017-Q2" : 5.7,
    "2017-Q3" : 5.6,
    "2017-Q4" : 5,
    "2018-Q1" : 5.3,
    "2018-Q2" : 5.5,
    "2018-Q3" : 5.4,
    "2018-Q4" : 5.1,
    "2019-Q1" : 5.2,
    "2019-Q2" : 5.1,
    "2019-Q3" : 5.4,
    "2019-Q4" : 4.5,
    "2020-Q1" : 5.3,
    "2020-Q2" : 17.6,
    "2020-Q3" : 10,
    "2020-Q4" : 8.7,
    "2021-01" : 8.7,
    "2021-02" : 8.8,
    "2021-03" : 7.1,
    "2021-04" : 8.7,
    "2021-05" : 7.7,
    "2021-06" : 7.7,
    "2021-07" : 6.9,
    "2021-08" : 8.1,
    "2021-09" : 8.9,
    "2021-10" : 7.4,
    "2021-11" : 6.5,
    "2021-12" : 6.6,
    "2022-01" : 6.4,
    "2022-02" : 6.4,
    "2022-03" : 5.8,
    "2022-04" : 5.7,
    "2022-05" : 6.0,
    "2022-06" : 6.0,
    "2022-07" : 5.2,
    "2022-08" : 5.3,
    "2022-09" : 5.0,
    "2022-10" : 4.5,
    "2022-11" : 4.2,
    "2022-12" : 4.3,
    "2023-01" : 4.8,
    "2023-02" : 4.8,
    "2023-03" : 4.7
}

f = open("myfile.txt", "w")

for root, dirs, files in os.walk(r'C:\Users\Admin\Desktop\GitHub Repos\raw-data UNEMPLOYED ONLY'): # insert directory of where raw-data is stored
    # raw-data UNEMPLOYED ONLY is a folder filled with .csv files that were created from the other python script
    reduced_root = root.split('\\')
    for file in files:
        print(file)
        df = pd.read_csv(root + "\\" + file, on_bad_lines='skip',low_memory=False)

        # we are renaming these columns for the sake of consistency, they are basically the same
        df.rename(columns = {'PUFURB2K10':'PUFURB2015'}, inplace = True)
        df.rename(columns = {'PUFC34_WYNOT':'PUFC26_WYNOT'}, inplace = True)
        df.rename(columns = {'PUFC40_POCC':'PUFC41_POCC'}, inplace = True)
        df.rename(columns = {'PUFC31_POCC':'PUFC41_POCC'}, inplace = True)
        for category in data:
            # this must leave only 2016-Q1
            if category not in df.columns and category != 'unemployment_rate':
                df.rename(columns = {to_be_replaced[category]:category}, inplace = True)

        (rows, cols) = df.shape
        df.insert(cols, "unemployment_rate", unemployment_rate[file[0:7]])

        df1 = df[data]
        df1.to_csv(file + ".csv")