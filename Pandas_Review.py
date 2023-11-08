import pandas as pd 
import numpy as np




'''Here are a few examples of how to put together a dataframe (pd.Dataframe())'''
#region: Constructing Dataframes
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
'''you can create a list of lists and then use the dataframe method to assembly the lists into 
an array (you must provide the column name arguement)'''


# example 1: list of lists
# take a list of lists, use pd.Dataframe() function to convert the object to a dataframe type
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


# example 2: dictionary conversion to dataframe
census_sample = {
    "Name" :        ["Bob J", "Gus F.", "Walter W.",  "Charles M.", "Jimmy M", "Kim W.", "Howard H."],
    "Age"  :        [55,48,52,56,45,44,50],
    "Gender":       ["M" ,"M", "M", "M", "M", "F", "M"],
    "City":         ["NYC", "Santiago", "Albaquerque", "Albaquerque", "Cicero", "Albaquerque", "Albaquerque"],
    "Country":      ["United States", "Chile", "United States", "United States", "United States", "United States", "United States"],
    "Profession":   ["Economist", "Distributor", "Teacher", "Lawyer", "Lawyer", "Lawyer", "Lawyer"]}


census_sample = pd.DataFrame(census_sample)

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
#endregion



'''Examples of how to view data at a high level (tables, heads, tails)'''
# region: viewing data(tables, heads, tails)
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

# tables - single dimensional view, great for viewing frequencies of variables
census_sample.value_counts("City")
census_sample.value_counts("City").to_dict()

# A table view by 2 dimensions:
census_sample.value_counts(["Country", "City"]).to_dict()


# view head
#shows top two rows - is more useful if we sort columns
census_sample.head(2)
# these are the 3 youngest people
census_sample.sort_values(by= "Age", ascending = True).head(3)
# this is the oldest person
census_sample.sort_values(by= "Age", ascending = False).head(1)


# view tails - this is the tail end of the dataset, while our example above let us view the oldest
# this easily lets us view the youngest
census_sample.sort_values(by= "Age", ascending = False).tail(1)

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
#endregion




'''slicing: indexing, filtering and selecting data'''
#region
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

# prints class and data:
print(f"{type(census_sample)}\r\n :{census_sample}")

        # filtering, selecting, subsetting this dataframe:


        #   slicing rows and columns by index 
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        

# iloc is a method for integer based location extracting and can be quite precise.
# think of  iloc as "index-location" indexes are often associated with rows. 

# Select row and column values by index
    # with that logic in mind 
            # calling df.iloc[100] returns all the data in row 100 
    # adding a second arguement allows you to select a specific column as opposed to all columns 
            # calling df.iloc[100, 5] returns 1 value: Only the value in the 5th column in the 100th row.
            # calling df.iloc[:, 5] returns all the elements in column 5
            # add an array arguement df.iloc[:, [5,6,7]] returns all values in cols 5,6,7

    # some examples:
census_sample.iloc[5] # returns row 5, with elements listed out
# if there is no second arguement, it assumes you want all columns
census_sample.iloc[[5]] # returns row 5, in the shape of a dataframe

census_sample.iloc[:, [1]] # returns all the elements in columnn 2 in the shape of dataframe, with col names
census_sample.iloc[:, 1]   # returns all col 2, no cal names

census_sample.iloc[1, 0] # returns the second row in col 1
census_sample.iloc[1:3, [0]] # returns rows 1-2 in col 1
census_sample.iloc[:, [0,1]] # returns all rows in columns 0&1

#***************************************************************************************************************************************    
            
            #   selecting and filtering using [[]]
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        #selecting columns by column name
# df[ [ col1, col2, ... ] ]
census_sample[["Name", "Age"]]

# or df.loc[:, [col1, col2, ...]] is equivalent 
census_sample.loc[:, ["Name", "Age"]]


        #filtering columns
# the loc method allows one to filter the dataframe based the arguement provided:
# df.loc[df["colname"] == "value"]


# the loc method selects rows and columns by label name
census_sample.loc[census_sample["Name"] == "Gus F."]

# if you dont want to establish criteria within the loc you can make a mask first
mask =  (census_sample["Country"] == "United States") & (census_sample["Profession"] == "Lawyer")
mask

#  use of the mask as a filter:
census_sample.loc[mask] # returns only the row-index where mask = True

# or you can enter directly into the loc method:
census_sample.loc[ (census_sample["Country"] == "United States") & (census_sample["Profession"] == "Lawyer")]


# select and filter in conjunction
census_sample[["Name"]].loc[census_sample["Profession"] == "Lawyer"]
census_sample.iloc[:, [0,1]].loc[census_sample["Profession"] == "Teacher"]


# filtering and selecting with iloc and loc
value = census_sample.columns[-1] #grabs the column "Profession"
census_sample.iloc[:, [0, 1, 2]].loc[census_sample[value] == "Teacher"]
#***************************************************************************************************************************************    
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


#endregion






'''applying custom functions'''
    # how to map a function to a dataframe
# there are 3 ways to apply custom functions: map, apply, applymap

#map is for custom functions that can be expressed in a lambda function
#df['new col name'].map(lambda x: postcondition if x condition else postcondition2 )



'''aggregating and grouping by data'''


'''reshaping data'''

'''reshaping by pivoting dataframe objects (much like pivot tables)'''

'''reshaping by stacking and unstacking'''

'''reshaping by melt'''

'''pivot_table()'''



'''removing duplicates in data'''
        # remove duplicates by finding duplicates and filtering out
        # remove duplicates by making entire dataframe unique



'''joining and appending data'''
        # left join
        # inner join
        # right join
        # right outer join
        # left outer join
        # full join




'''Writing data'''



'''Reading data'''



'''Index iteration'''




'''collections of dataframes'''


