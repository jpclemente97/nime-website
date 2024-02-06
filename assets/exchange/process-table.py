#requirements
#python 3.9 or higher
#pandas
#os

import os
import pandas as pd

#filenames
raw_table_filename = 'NIMExchange Form.csv'
exported_table_filename = 'exchange-table.csv'
exported_table_small_filename = 'exchange-table-small.csv'

#columns
columns_to_drop = ['Timestamp','Username']

columns_original_id = ['Name of the NIME',	'Description', 'Paper', 'Webpage', 'Picture', 'Video', 
                            'Name of owner', 'Email of owner', 'Geographical location', 'Borrowing terms',
                            'Allowed borrowers', 'Interest in collaborating with borrower', 'How to borrow',
                            'Documentation', 'Working condition', 'Technical Support',
                            'Hardware integrity', 'Year of manufacturing or last update',
                            'Software dependencies', 'Operating system dependency',
                            'Dimension and weight',	'Other information']

column_renamed_id = ['NIME', 'Description', 'Paper', 'Webpage', 'Picture', 'Video', 
                            'Owner', 'Email', 'Location', 'Borrowing terms',
                            'Allowed borrowers', 'Collaborating with borrower', 'How to borrow',
                            'Documentation', 'Working condition', 'Technical Support',
                            'Hardware integrity', 'Last update',
                            'Software dependencies', 'OS dependency',
                            'Dimension and weight',	'Other information']

columns_small_id = ['NIME', 'Description', 'Picture', 'Owner', 'Email'] 

columns_renaming_dict = {}
for key,value in zip(columns_original_id,column_renamed_id):
    columns_renaming_dict[key] = value

columns_to_drop_small = list(set(column_renamed_id) - set(columns_small_id))

#dropping sensitive columns and renaming columns
table_full = pd.read_csv(raw_table_filename)
table_full = table_full.drop(columns=columns_to_drop)
table_full = table_full.rename(columns=columns_renaming_dict)

#masking emails
for index, row in table_full.iterrows():
    email = row['Email']
    email = email.replace("@", " _at_ ")
    email = email.replace(".", " _dot_ ")
    table_full.at[index,'Email'] = email

#generating partial table
table_small = table_full.drop(columns=columns_to_drop_small)

table_full.to_csv(exported_table_filename, index=False)
table_small.to_csv(exported_table_small_filename, index=False)

if os.path.exists(raw_table_filename):
    os.remove(raw_table_filename)
