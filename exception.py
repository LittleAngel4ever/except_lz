import pandas as pd

class DataFrameStructureError(Exception):
    pass

class DataFrameTypeError(Exception):
    pass

class DataFrame:
    def __init__(self, filename):
        try:
            self.df = pd.read_csv(filename)
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
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError("Wrong structure")
        except DataFrameStructureError:        
            print("Please, remake your columns, we were waiting for", self.column_list_main, ", but you given", self.column_list_from_file)
        try:
            self.df_input_types = str(self.df.dtypes)
            self.df_original_types = str(self.df_original.dtypes)
            if self.df_input_types != self.df_original_types:
                raise DataFrameTypeError("Wrong types")
            else:
                print("Everything alright")
        except:
            print("Wrong types\n" 
            "Expected: ", self.df_original_types,
            "\nInput: ", self.df_input_types)


def main():
    filename = input("Please, enter name of your file: ")
    df = DataFrame(filename)

if __name__ == "__main__":
    main()