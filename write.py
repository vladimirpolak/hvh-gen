from pyexcel_ods3 import save_data
from setgen import generate_set
from collections import defaultdict

data = defaultdict(list)
for _ in range(100):
    data["Sheet 1"].append(generate_set())

save_data("your_file.ods", data)
