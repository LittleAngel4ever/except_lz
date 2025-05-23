import pandas as pd

class DataFrameStructureError(Exception):
    pass

class DataFrameTypeError(Exception):
    pass

# Handling errors
class DataFrame:
    def __init__(self, filename):
        try:
            self.df = pd.read_csv(filename)
        except FileNotFoundError: # File presence error
            print('The following error occurred: No such file of directory: ', filename)
            raise SystemExit()
        except pd.errors.EmptyDataError: # Error in the presence of data in the file
            print("The following error occurred: Dataframe is empty.")
            raise SystemExit()
        except pd.errors.ParserError: # Strange Column Placement Error
            print("The following error occurred: Strange column arrangement")
            raise SystemExit()
        try:
            self.column_list_from_file = self.df.columns.to_list()
            self.df_orig = pd.read_csv("var7original.csv")
            self.column_list_main = self.df_orig.columns.to_list()
            if self.column_list_from_file != self.column_list_main:
                raise DataFrameStructureError("Wrong structure")
        except DataFrameStructureError: # Dataframe structure error
            print("Please, remake your columns, we were waiting for", self.column_list_main, ", but you given", self.column_list_from_file)
            raise SystemExit()
        try:
            self.df_input_types = str(self.df.dtypes)
            self.df_original_types = str(self.df_orig.dtypes)
            if self.df_input_types != self.df_original_types:
                raise DataFrameTypeError("Wrong types")
            else:
                print("Reading the dataframe completed successfully.")
        except:
            print("Wrong types\n" 
            "Expected: ", self.df_original_types,
            "\nInput: ", self.df_input_types)


def main():
    filename = input("Please, enter name of your file: ")
    df = DataFrame(filename)

if __name__ == "__main__":
    main()