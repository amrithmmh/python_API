import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

class ReadXl_CSV:
    """reads xl using pandas library"""
    def __init__(self):
        pass
    def read_xl(self,file_name):
        try:
            self.dfXL = pd.read_excel(str(file_name), sheet_name='Sheet1')
        except Exception:
            print("error reading file")
            return -1
        return 0

    def search_xl(self,column,row):
        return self.dfXL[str(column)][row]

    def read_CSV(self,file_name):
        try:
            self.dfCSV=pd.read_csv(str(file_name))
        except Exception:
            print("error reading file")
            return -1
        return 0

    def search_CSV(self,column,row):
        return self.dfXL[str(column)][row]
        


def main():
    Read=ReadXl_CSV()
    print(Read.read_xl('calc.xlsx'))
    print(Read.search_xl('key',1))
    print(Read.read_CSV('calc.csv'))
    print(Read.search_CSV('key',1))

if __name__ == "__main__":
    main()
