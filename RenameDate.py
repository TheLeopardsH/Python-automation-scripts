import re,os,shutil
# convert date format from American (MM-DD-YYYY) to European (DD-MM-YYYY) in all file names
DatePattern = re.compile(r"""^(.*?)
                        ((0|1)?\d)- # one or two digits for month
                        ((0|1|2|3)?\d)- #one or two digits for day
                        ((19|20)?\d\d) # four digits from 1900 to 2099 years
                        (.*?)$
                         """, re.VERBOSE)
for Afilename in os.listdir('.'):
    dp = DatePattern.search(Afilename)
    if dp == None:
        continue
    #different parts of filename
    beforepart = dp.group(1)
    monthpart  = dp.group(2)
    daypart    = dp.group(4)
    yearpart   = dp.group(6)
    afterpart  = dp.group(8)
    Efilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart
    AbsolutePathCurrentDir = os.path.abspath('.')
    AmericanDateFilename = os.path.join(AbsolutePathCurrentDir, Afilename)
    EuropeanDateFilename = os.path.join(AbsolutePathCurrentDir, Efilename)
    print(f'Renaming "{Afilename}" to "{Efilename}"...')
    shutil.move(AmericanDateFilename,EuropeanDateFilename)


