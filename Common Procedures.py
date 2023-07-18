import pandas as pd 


#This is a representation of manually putting together a dataframe, in practice you are more often reading from files or pulling from a database

# Putting together a small dataframe as an easy example
'''you can create a list of lists and then use the dataframe method to assembly the lists into 
an array (you must provide the column name arguement)'''
census_sample = [
    ["Bob J.",      55, "M"     ,"NYC"          ,"United States",   "Economist"],
    ["Gus F.",      48, "M"     ,"Santiago"     ,"Chile",           "Distributor"],
    ["Walter W.",   52, "M"     ,"Albaquerque"  ,"United States",   "Teacher"],
    ["Charles M.",  59, "M"     ,"Albaquerque"  ,"United States",   "Lawyer"],
    ["Jimmy M.",    45, "M"     ,"Cicero"       ,"United States",   "Lawyer"],
    ["Kim W.",      44, "F"     ,"Albaquerque"  ,"United States",   "Lawyer"],
    ["Howard H.",   50, "M"     ,"Albaquerque"  ,"United States",   "Lawyer"],
]

census_sample = pd.DataFrame(census_sample, columns=["Name", "Age", "Gender", "City", "Country", "Profession"])


'''or you can use a dictionary'''
census_sample = {
    "Name" :        ["Bob J", "Gus F.", "Walter W.",  "Charles M.", "Jimmy M", "Kim W.", "Howard H."],
    "Age"  :        [55,48,52,56,45,44,50],
    "Gender":       ["M" ,"M", "M", "M", "M", "F", "M"],
    "City":         ["NYC", "Santiago", "Albaquerque", "Albaquerque", "Cicero", "Albaquerque", "Albaquerque"],
    "Country":      ["United States", "Chile", "United States", "United States", "United States", "United States", "United States"],
    "Profession":   ["Economist", "Distributor", "Teacher", "Lawyer", "Lawyer", "Lawyer", "Lawyer"]}


census_sample = pd.DataFrame(census_sample)

# prints data type, and dataframe
print(f"{type(census_sample)}\r\n :{census_sample}")


        # filtering, selecting, subsetting this dataframe:

#   slicing by label 
# think of iloc as index-locate to select rows/cols by index position

census_sample.iloc[5] # returns row 5, with elements listed out
# if there is no second arguement, it assumes you want all columns
census_sample.iloc[[5]] # returns row 5, in the shape of a dataframe

census_sample.iloc[:, [1]] # returns all the elements in columnn 2 in the shape of dataframe, with col names
census_sample.iloc[:, 1]   # returns all col 2, no cal names

census_sample.iloc[1, 0] # returns the second row in col 1
census_sample.iloc[1:3, [0]] # returns rows 1-2 in col 1
census_sample.iloc[:, [0,1]] # returns all rows in columns 0&1
 


# the loc method selects rows and columns by label name
census_sample.loc[census_sample["Name"] == "Gus F."]

# create a boolean mask
mask =  (census_sample["Country"] == "United States") & (census_sample["Profession"] == "Lawyer")
mask
#  use the mask as a filter 
census_sample.loc[mask] # returns only the row-index where mask = True

# or you can enter directly into the loc method:
census_sample.loc[ (census_sample["Country"] == "United States") & (census_sample["Profession"] == "Lawyer")]


# select by column name
census_sample[["Name"]]
census_sample[['Name', 'Age']]

# select and filter in conjunction
census_sample[["Name"]].loc[census_sample["Profession"] == "Lawyer"]
census_sample.iloc[:, [0,1]].loc[census_sample["Profession"] == "Teacher"]
