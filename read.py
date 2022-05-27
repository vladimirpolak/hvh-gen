# from pyexcel_ods3 import get_data, save_data
import pyexcel_ods3 as p
from collections import OrderedDict
from setgen import generate_set
import openpyxl
# import pyexcel as p

output = OrderedDict()

data = p.get_data("05-2022.ods")

for title, sheet in data.items():

    output[title] = []
    output[title].append(sheet[0])

    day = ""
    for row in sheet[1:]:
        if row[0]:
            day = row[0]

        generated_values = generate_set()
        for v in generated_values:
            row.append(v)

        row.append("OK")
        output[title].append(row)

# p.save_data("05-2022.ods", output)
p.write_data("05-2022.ods", output)

# sheet = p.get_sheet(file_name="05-2022.ods")
# sheet.save_as("example.ods")
