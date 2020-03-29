import openpyxl,pprint
print('Opening Excel workbook')
excelfile = openpyxl.load_workbook('censuspopdata.xlsx')
sheetofP = excelfile['Population by Census Tract']
CountryData ={}
print('Moving toward reading of data')
for row in range(2,sheetofP.max_row+1):
    state = sheetofP['B'+str(row)].value
    country = sheetofP['C'+str(row)].value
    population = sheetofP['D'+str(row)].value
    CountryData.setdefault(state, {})
    CountryData[state].setdefault(country,{'tracts':0,'population':0})
    CountryData[state][country]['tracts']+=1
    CountryData[state][country]['population']+=int(population)
print("Writing Results")
OutputFile = open('populationtract.py','w')
OutputFile.write('allData= '+pprint.pformat((CountryData)))
OutputFile.close()
print('Done')


