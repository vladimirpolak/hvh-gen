from pyexcel_ods3 import save_data
from setgen import generate_set
from collections import defaultdict

# https://pypi.org/project/pyexcel-ods3/

data = []
for _ in range(279):
    line = []
    generated_values = generate_set()
    for value in generated_values:
        line.append(str(value))

    line.append("OK")
    data.append(line)

with open("my-data.csv", "w") as f:
    for l in data:
        f.write(",".join(l))
        f.write("\n")
# save_data("example.ods", data)
