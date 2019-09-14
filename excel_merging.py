import pandas as pd
import glob

all_data1 = pd.DataFrame()
all_data2 =pd.DataFrame()
all_data3 =pd.DataFrame()
# 'all_data' could be more/less regarding how many sheets is going to be appended


print('1.Accessing the excel files...')
for f in glob.glob('excel files\\*.xlsx'):
    print('<<Reading data of:-', f + '>>')
    print('\tReading Sheet1 Data...')
    df1 = pd.read_excel(f, sheet_name=0)

    print('\tReading Sheet2 data...')
    df2 = pd.read_excel(f, sheet_name=1)

    print('\tReading Sheet3 data...')
    df3 = pd.read_excel(f, sheet_name=2)

    print('\t\tAppending Sheet1 data...')
    all_data1 = all_data1.append(df1, ignore_index=True, sort=False)

    print('\t\tAppending Sheet2 data..')
    all_data2 = all_data2.append(df2, ignore_index=True, sort=False)

    print('\t\tAppending Sheet3 data..')
    all_data3 = all_data3.append(df3, ignore_index=True, sort=False)
    #increase or decrease the block of read_excel & append section regarding the number of sheets.


print('2.writing appended data...')
writer = pd.ExcelWriter('excel files\\merged_data.xlsx', engine='openpyxl')

print('\tWriting Sheet1 data....')
all_data1.to_excel(writer, sheet_name= 'CDD')

print('\tWriting Sheet2 data....')
all_data2.to_excel(writer, sheet_name= 'L2U')

print('\tWriting Sheet3 data....')
all_data3.to_excel(writer, sheet_name= 'L2G')



print('3.Saving Final excel file......')
writer.save()

