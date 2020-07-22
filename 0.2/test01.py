import pandas as pd

tables = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/")

print(tables[0])