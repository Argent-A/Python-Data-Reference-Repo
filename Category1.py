import pandas as pd 

# Putting together a small dataframe as an easy example

census_sample = [
    ["Bob J.",      55, "M"     ,"NYC"          ,"United States",  "Economist"],
    ["Gus F.",      48, "M"     ,"Santiago"     ,"Chile",          "Distributor"],
    ["Walter W.",   52, "M"     ,"Albaquerque"  ,"United States",   "Teacher"],
    ["James M.",    56, "M"     ,"Albaquerque"  ,"United States",   "Lawyer"],
    ["Jimmy M.",    45, "M"     ,"Cicero"       ,"United States",   "Lawyer"]
]

census_sample = pd.DataFrame(census_sample, columns=["Name", "Age", "Gender", "City", "Country", "Profession"])

# filtering this dataframe 

print(census_sample)
# filtering and selecting a dataframe
