"""Script to create Pivot table"""
import os
import sys

import pandas as pd
import win32com.client as win32
from pandas import ExcelWriter

win32c = win32.constants


def create_pivot_table(wb, ws1, pt_ws, ws_name, pt_name, pt_rows, pt_cols, pt_filters, pt_fields):
    """
    wb = workbook1 object
    ws1 = worksheet1
    pt_ws = pivot table worksheet number
    ws_name = pivot table worksheet name
    pt_name = name given to pivot table
    pt_rows, pt_cols, pt_filters, pt_fields: values selected for filling the pivot tables
    """

    # pivot table location
    pt_loc = len(pt_filters) + 2
    pc = wb.PivotCaches().Create(SourceType=win32c.xlDatabase, SourceData=ws1.UsedRange)

    # create the pivot table object
    pc.CreatePivotTable(TableDestination='{}!R{}C1'.format(ws_name, pt_loc), TableName=pt_name)

    # select the pivot table work sheet and location to create the pivot table
    pt_ws.Select()
    pt_ws.Cells(pt_loc, 1).Select()

    # Sets the rows, columns and filters of the pivot table
    for field_list, field_r in (
            (pt_filters, win32c.xlPageField), (pt_rows, win32c.xlRowField), (pt_cols, win32c.xlColumnField)):
        for i, value in enumerate(field_list):
            pt_ws.PivotTables(pt_name).PivotFields(value).Orientation = field_r
            pt_ws.PivotTables(pt_name).PivotFields(value).Position = i + 1

    # Sets the Values of the pivot table
    for field in pt_fields:
        pt_ws.PivotTables(pt_name).AddDataField(pt_ws.PivotTables(pt_name).PivotFields(field[0]), field[1],
                                                field[2]).NumberFormat = field[3]

    # Visibility True or False
    pt_ws.PivotTables(pt_name).ShowValuesRow = True
    pt_ws.PivotTables(pt_name).ColumnGrand = True


# Dummy data
name_list = ['Aman', 'Palak', 'Somya', 'Sama', 'Alex', 'Fazz', 'Malik', 'Mahi', 'Diyan', 'Naomi', 'Frank', 'Sachin',
             'Deep', 'Soham', 'Kavya', 'Aman1', 'Palak1', 'Somya1', 'Sama1', 'Alex1', 'Fazz1', 'Malik1', 'Mahi1',
             'Diyan1', 'Naomi1', 'Frank1', 'Sachin1', 'Deep1', 'Soham1', 'Kavya1']
level_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'A1', 'A2',
              'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4']
tech_list = ['Python', 'Selenium', 'Appium', 'QA', 'MS Office', 'Python', 'Selenium', 'Appium', 'QA', 'MS Office',
             'Python', 'Selenium', 'Appium', 'QA', 'MS Office', 'Python', 'Selenium', 'Appium', 'QA', 'MS Office',
             'Python', 'Selenium', 'Appium', 'QA', 'MS Office', 'Python', 'Selenium', 'Appium', 'QA', 'MS Office']
year_of_experience_list = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4,
                           3, 2, 1]

df = pd.DataFrame(
    {'Name': name_list, 'Level': level_list, "Experti": tech_list, 'Year of experience': year_of_experience_list})

filename = os.getcwd() + '/DataSheet.xlsx'
writer = ExcelWriter(filename)
df.to_excel(writer, 'Data_Source', index=False)
writer.save()

# create excel application object
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True  # False

try:
    wb = excel.Workbooks.Open(filename)
except Exception as e:
    sys.exit(1)

ws1 = wb.Sheets('Data_Source')

# Setup and call pivot_table
ws2_name = 'pivot_table'
wb.Sheets.Add().Name = ws2_name
ws2 = wb.Sheets(ws2_name)
pt_name = 'By_Experti'
pt_rows = ['Experti']
pt_cols = ['Year of experience']
pt_filters = ['Level']
pt_fields = [['Name', 'Name: count', win32c.xlCount, '0']]

create_pivot_table(wb, ws1, ws2, ws2_name, pt_name, pt_rows, pt_cols, pt_filters, pt_fields)
