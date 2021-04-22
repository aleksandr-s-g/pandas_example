from datetime import timedelta
import pandas as pd

from modules.xlsxLoader import xlsxLoader


def aggregate(x):
    d = {}
    columns = ['installs', 'costs', 'revenue', 'payers_share']
    for c in columns:
        d[c + '_avg'] = x[c].mean()
        d[c + '_std'] = x[c].std()
        d[c + '_variation'] = x[c].std()/x[c].mean()
        d[c + '_median'] = x[c].median()
        d[c + '_percentile_25'] = x[c].quantile(0.25)
        d[c + '_percentile_75'] = x[c].quantile(0.75)
    return pd.Series(d)


if __name__ == '__main__':
    data = xlsxLoader.load_all_xlsx("files")
    week_start = lambda data: data['date'] - data['date'].dt.weekday * timedelta(days=1)
    grouped_data = data.groupby(week_start(data)).apply(aggregate)
    grouped_data.to_csv('grouped_data.csv')
    correlation_coefficient = data['installs'].corr(data['revenue'] - data['costs'])
    print(f"correlation coefficient = {correlation_coefficient}")
    pd.options.display.max_columns = None
    pd.options.display.width = None
    print(grouped_data)
