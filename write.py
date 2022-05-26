from pyexcel_ods3 import save_data
from setgen import generate_set
from collections import defaultdict

# https://pypi.org/project/pyexcel-ods3/

data = defaultdict(list)
for _ in range(1000):
    data["Sheet 1"].append(generate_set())

save_data("example.ods", data)
