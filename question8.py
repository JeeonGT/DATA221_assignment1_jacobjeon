import pandas as pd

data_of_letters = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

dataframe_data_of_letters = pd.DataFrame(data_of_letters)
dataframe_data_of_letters["D"] = dataframe_data_of_letters["A"] + dataframe_data_of_letters["B"]

print(dataframe_data_of_letters)