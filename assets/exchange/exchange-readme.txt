The following document will explain the steps to publish the data submitted vai NIMExchange form.

0. clone the nime-website repository
1. download the form responses as .csv file and move it to the exchange folder (do not change the filename)
2. ensure that the images submitted with the Google form in Gdrive have permission set to “general access” permissions to “anyone with the link”
2. run the python script 'python process-table.py' (requires python 3.9 or higher and pandas)
3. if 2. succeeds the downloaded .csv will be deleted and two new .csv files will appear in the same folder: exchange-table-small.csv and exchange-table.csv
4. preview changes running the command 'bundle exec jekyll serve' and commit the changes

optional:
* to change the contents of the associated pages on the nime website edit: exchange.md and exchange-full.md (files in the website root)
* to change the font size of the table, create a “<style>” tag, and for the div of the table add the line “font-size: <x>px;”, with <x> being the selected font size.
* to make a column wider, edit process-table.py and add underscores '_____' (as many as the target width) to the column name (edit the column_renamed_id list and eventually also columns_small_id)
* to make a column narrower, break too add a new line character (‘\n’) to all entries in a column or a space using custom formatting or python process-table.py