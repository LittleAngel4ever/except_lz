import pandas as pd

class DataFrameStructureError(Exception):
    print("Wrong structure of DataFrame")

class DataFrame:
    def __init__(self):
        try:
            self.df = pd.read_csv("var7.csv")
            # print(self.df)
        except FileNotFoundError:
            print("No such file")
        except pd.errors.DataError:
            print("No data in file")
        except pd.errors.ParserError:
            print("Wrong data")
        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_original = pd.read_csv("var7original.csv")
            self.column_list_main = self.df_original.columns.to_list()
            # print(self.column_list_from_file)
            # print(self.column_list_main)
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError("Wrong structure")
            else:
                print("Everything alright")
        except DataFrameStructureError:        
            print("Please remake your columns, we were waiting for", self.column_list_main, ", but you given", self.column_list_from_file)


filename = input("Please, enter name of your file: ")
df = DataFrame()

# str(df['b'].dtype)

df['c'].info()