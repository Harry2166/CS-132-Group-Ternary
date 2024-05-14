# THIS PYTHON SCRIPT IS FOR THE CONVERTED CSVs.
# This python script is responsible for reducing the csvs to the variables needed

import pandas as pd
import os
import numpy as np

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
'PUFC38_PREVJOB', # previous job indiactor
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
    "PUFC38_PREVJOB" : "C43_LBEF",
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

grade_dict1 = {
    0 : 0,
    210 : 1,
    220 : 1,
    230 : 1,
    240 : 1,
    250 : 1,
    260 : 1,
    280 : 1,
    310 : 2,
    320 : 2,
    330 : 2,
    340 : 2,
    350 : 3,
    410 : 6,
    420 : 6,
    810 : 8,
    820 : 8,
    830 : 8,
    840 : 8,
    900 : 9,
    501 : 8,
    508 : 8,
    509 : 8,
    514 : 8,
    521 : 8,
    522 : 8,
    531 : 8,
    532 : 8,
    534 : 8,
    542 : 8,
    544 : 8,
    548 : 8,
    552 : 8,
    554 : 8,
    558 : 8,
    562 : 8,
    564 : 8,
    572 : 8,
    576 : 8,
    581 : 8,
    584 : 8,
    585 : 8,
    586 : 8,
    589 : 8,
    601 : 8,
    614 : 8,
    621 : 8,
    622 : 8,
    631 : 8,
    632 : 8,
    634 : 8,
    638 : 8,
    642 : 8,
    644 : 8,
    646 : 8,
    648 : 8,
    652 : 8,
    654 : 8,
    658 : 8,
    662 : 8,
    664 : 8,
    672 : 8,
    676 : 8,
    681 : 8,
    684 : 8,
    685 : 8,
    686 : 8,
    689 : 8,
}

grade_dict2 = {
    0 : 0,
    110 : 1,
    120 : 1,
    130 : 1,
    140 : 1,
    150 : 1,
    160 : 1,
    170 : 1,
    180 : 2,
    210 : 2,
    220 : 2,
    230 : 2,
    240 : 2,
    250 : 3,
    310 : 6,
    320 : 6,
    410 : 1,
    420 : 1,
    430 : 1,
    440 : 1,
    450 : 1,
    460 : 1,
    470 : 2,
    480 : 2,
    490 : 2,
    500 : 2,
    510 : 4,
    520 : 4,
    710 : 8,
    720 : 8,
    730 : 8,
    740 : 8,
    750 : 8,
    760 : 8,
    910 : 9,
    920 : 9,
    930 : 9,
    940 : 9,
    601 : 6,
    608 : 6,
    609 : 6,
    614 : 6,
    621 : 6,
    622 : 6,
    631 : 6,
    632 : 6,
    634 : 6,
    642 : 6,
    644 : 6,
    648 : 6,
    652 : 6,
    654 : 6,
    658 : 6,
    662 : 6,
    664 : 6,
    672 : 6,
    676 : 6,
    681 : 6,
    684 : 6,
    685 : 6,
    686 : 6,
    689 : 6,
    801 : 8,
    814 : 8,
    821 : 8,
    822 : 8,
    831 : 8,
    832 : 8,
    834 : 8,
    838 : 8,
    842 : 8,
    844 : 8,
    846 : 8,
    848 : 8,
    852 : 8,
    854 : 8,
    858 : 8,
    862 : 8,
    864 : 8,
    872 : 8,
    876 : 8,
    881 : 8,
    884 : 8,
    885 : 8,
    886 : 8,
    889 : 8,
    621 : 6,
    648 : 6,
    652 : 6,
    654 : 6,
    658 : 6,
    662 : 6,
    672 : 6,
    681 : 6,
    684 : 6,
    686 : 6
}

grade_dict3 = {
    (0,0) : 0,
    (110,180) : 1,
    (410,460) : 1,
    (210,240) : 2,
    (470,490) : 2,
    (250,250) : 3,
    (500,500) : 3,
    (510,510) : 4,
    (520,520) : 5,
    (310,320) : 6,
    (601,689) : 7,
    (710,760) : 8,
    (801,940) : 9,
}

grade_dict4 = {
    (0,0) : 0,
    (410,460) : 1,
    (470,490) : 2,
    (500,500) : 3,
    (510,510) : 4,
    (520,520) : 5,
    (310,320) : 6,
    (601,689) : 7,
    (710,760) : 8,
    (801,940) : 9
}

grade_dict5 = {
    0 : 0,
    310 : 6,
    320 : 6,
    410 : 1,
    420 : 1,
    430 : 1,
    440 : 1,
    450 : 1,
    460 : 1,
    470 : 2,
    480 : 2,
    490 : 2,
    500 : 2,
    510 : 4,
    520 : 4,
    710 : 8,
    720 : 8,
    730 : 8,
    740 : 8,
    750 : 8,
    760 : 8,
    910 : 9,
    920 : 9,
    930 : 9,
    940 : 9,
    601 : 6,
    608 : 6,
    609 : 6,
    614 : 6,
    621 : 6,
    622 : 6,
    631 : 6,
    632 : 6,
    634 : 6,
    642 : 6,
    644 : 6,
    648 : 6,
    652 : 6,
    654 : 6,
    658 : 6,
    662 : 6,
    664 : 6,
    672 : 6,
    676 : 6,
    681 : 6,
    684 : 6,
    685 : 6,
    686 : 6,
    689 : 6,
    801 : 8,
    814 : 8,
    821 : 8,
    822 : 8,
    831 : 8,
    832 : 8,
    834 : 8,
    838 : 8,
    842 : 8,
    844 : 8,
    846 : 8,
    848 : 8,
    852 : 8,
    854 : 8,
    858 : 8,
    862 : 8,
    864 : 8,
    872 : 8,
    876 : 8,
    881 : 8,
    884 : 8,
    885 : 8,
    886 : 8,
    889 : 8,
}

grade_dict6 = {
    (0, 2000) : 0,
    (10002, 10020) : 1,
    (24002, 24013) : 2,
    (24014,24020) : 3,
    (34011,34012) : 4,
    (34021,34022) : 4,
    (34031,34032) : 4,
    (35001,35002) : 4,
    (35011,35012) : 4,
    (34012,34014) : 5,
    (34022,34024) : 5,
    (34032,34034) : 5,
    (35012,35014) : 5,
    (40001,40003) : 6,
    (50001,50003) : 6,
    (40010,40010) : 6,
    (50010,50010) : 6,
    (40011,49999) : 7,
    (50011,59999) : 7,
    (60001,600010) : 8,
    (60011,89999) : 9,
    (60000,60000) : 9,
}

f = open("myfile.txt", "w")

for root, dirs, files in os.walk(r'C:\Users\Admin\Desktop\GitHub Repos\new-raw-data'): # insert directory of where raw-data is stored
    # raw-data UNEMPLOYED ONLY is a folder filled with .csv files that were created from the other python script
    reduced_root = root.split('\\')
    for file in files:
        print(file)
        df = pd.read_csv(root + "\\" + file, on_bad_lines='skip',low_memory=False)

        # we are renaming these columns for the sake of consistency, they are basically the same
        df.rename(columns = {'PUFURB2K10':'PUFURB2015'}, inplace = True)
        df.rename(columns = {'PUFC34_WYNOT':'PUFC26_WYNOT'}, inplace = True)
        # df.rename(columns = {'PUFC41_POCC':'PUFC40_POCC'}, inplace = True)
        # df.rename(columns = {'PUFC31_POCC':'PUFC40_POCC'}, inplace = True)
        # df.rename(columns = {'PUFC40_POCC':'PUFC38_PREVJOB'}, inplace = True)
        df.rename(columns = {'PUFC28_PREVJOB':'PUFC38_PREVJOB'}, inplace = True)
        for category in data:
            # this must leave only 2016-Q1
            if category not in df.columns and category != 'unemployment_rate':
                df.rename(columns = {to_be_replaced[category]:category}, inplace = True)

        grade_column = df['PUFC07_GRADE']

        def grade_changer(x):
            grade_equivalent = {
                "2016-Q1.csv" : grade_dict1,
                "2016-Q2.csv" : grade_dict1,
                "2016-Q3.csv" : grade_dict2,
                "2016-Q4.csv": grade_dict2,
                "2017-Q1.csv" : grade_dict2,
                "2017-Q2.csv" : grade_dict3,
                "2017-Q3.csv" : grade_dict3,
                "2017-Q4.csv" : grade_dict2,
                "2018-Q1.csv" : grade_dict2,
                "2018-Q2.csv" : grade_dict2,
                "2018-Q3.csv" : grade_dict4,
                "2018-Q4.csv" : grade_dict5,
                "2019-Q1.csv" : grade_dict6,
                "2019-Q2.csv" : grade_dict6,
                "2019-Q3.csv" : grade_dict6,
                "2019-Q4.csv" : grade_dict6,
                "2020-Q1.csv" : grade_dict6,
                "2020-Q2.csv" : grade_dict6,
                "2020-Q3.csv" : grade_dict6,
                "2020-Q4.csv" : grade_dict6,
                "2021-01.csv" : grade_dict6,
                "2021-02.csv" : grade_dict6,
                "2021-03.csv" : grade_dict6,
                "2021-04.csv" : grade_dict6,
                "2021-05.csv" : grade_dict6,
                "2021-06.csv" : grade_dict6,
                "2021-07.csv" : grade_dict6,
                "2021-08.csv" : grade_dict6,
                "2021-09.csv" : grade_dict6,
                "2021-10.csv" : grade_dict6,
                "2021-11.csv" : grade_dict6,
                "2021-12.csv" : grade_dict6,
                '2022-01.csv' : grade_dict6,
                '2022-02.csv' : grade_dict6,
                '2022-03.csv' : grade_dict6,
                '2022-04.csv' : grade_dict6,
                '2022-04.csv' : grade_dict6,
                '2022-05.csv' : grade_dict6,
                '2022-06.csv' : grade_dict6,
                '2022-07.csv' : grade_dict6,
                '2022-08.csv' : grade_dict6,
                '2022-09.csv' : grade_dict6,
                '2022-10.csv' : grade_dict6,
                '2022-11.csv' : grade_dict6,
                '2022-12.csv' : grade_dict6,
                '2023-01.csv' : grade_dict6,
                "2023-02.csv" : grade_dict6,
                "2023-03.csv" : grade_dict6
            }

            if type(x) is str and len(x.strip()) == 0:
                return 99
            elif type(x) is not int: 
                x.split()
                x = int(x)
            
            if grade_equivalent[file] == grade_dict6:
                for (a,b) in list(grade_equivalent[file].keys()):
                    if x in range(a,b+1):
                        return grade_equivalent[file][(a,b)]
            elif grade_equivalent[file] == grade_dict3:
                for (a,b) in list(grade_equivalent[file].keys()):
                    if x in range(a,b+1):
                        return grade_equivalent[file][(a,b)]
            elif grade_equivalent[file] == grade_dict4:
                for (a,b) in list(grade_equivalent[file].keys()):
                    if x in range(a,b+1):
                        return grade_equivalent[file][(a,b)]
            elif grade_equivalent[file] == grade_dict6:
                for (a,b) in list(grade_equivalent[file].keys()):
                    if x in range(a,b+1):
                        return grade_equivalent[file][(a,b)]
            if x not in grade_equivalent[file].keys():
                if x == 191:
                    a = 1
                print(x)
                return 99
            return grade_equivalent[file][x]

        new_grade_column = grade_column.apply(grade_changer)
        df['PUFC07_GRADE'] = new_grade_column

        (rows, cols) = df.shape
        df.insert(cols, "unemployment_rate", unemployment_rate[file[0:7]])

        df1 = df[data]
        print(df['PUFC38_PREVJOB'])
        df1.to_csv(file + ".csv")