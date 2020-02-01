"==============================================================================================="
'                                                                                               '  
'                                            VINEbot                                            '
'                                     code by Ikram Kohil                                       '
'                                   based on sentdex tutorial                                   '
'                                      Started 31/01/20                                         '
'                                                                                               '
"==============================================================================================="

import sqlite3 # C library that implements SQL database engine (file based). Mostly used in Android Dev.
import json # The dataset is in the form of json ojects
from datetime import datetime #Used to output where we are when going through all the files

# Chose month you want the data from
timeframe = '' 

# To avoid transactions (units or sequences of work accomplished in a logical order, 
# whether in a manual fashion by a user or automatically by some sort of a database program) 
# line by line; instead of inserting rows one by one, we'll be building a big transaction to do it all at once.
sql_transaction = [] 

connection = sqlite3.connect('{}.db'.format(timeframe))
