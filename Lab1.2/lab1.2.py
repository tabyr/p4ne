from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

def getvalue(x):
    return x.value

sheet = wb['Data']

years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
sun = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temperature, label="Temp")
pyplot.plot(years, sun, label="Sun Active")

pyplot.show()
