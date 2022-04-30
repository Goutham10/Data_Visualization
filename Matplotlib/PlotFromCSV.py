import matplotlib.pyplot as plt
import numpy as np
import xlrd
# impo/rt codecs


plt.style.use("fivethirtyeight")

# csvReader = csv.reader(codecs.open('/home/vy/Data_Visualization/Matplotlib/sample.xls', 'rU', 'utf-8'))

with open("/home/vy/sample.xls", 'r') as csv_file:
    print("entered with ")
    print([row for row in xlrd.open_workbook_xls(csv_file)])
    # csv_reader = csv.reader(csv_file)


