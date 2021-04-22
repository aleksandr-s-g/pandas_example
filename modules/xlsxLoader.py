import os
import pandas as pd


class xlsxLoader():
    def load_all_xlsx(dir_path):
        path = os.getcwd()
        full_path = os.path.join(path, dir_path)
        files = os.listdir(full_path)
        files = [f for f in files if f[-4:] == 'xlsx' and f[0] != '~']
        df = pd.DataFrame()
        for f in files:
            data = pd.read_excel(os.path.join(full_path, f), 0)
            df = df.append(data)
        return df
