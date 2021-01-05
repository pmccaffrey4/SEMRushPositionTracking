import pandas as pd


def clean_raw_semrush(df):

    # removing columns not needed
    rank_cols_only = [col for col in df.columns if not any(x in col for x in ['type', 'landing', 'Tags', 'Search',
                                                                              'CPC', 'difference'])]

    # copy df with only columns needed
    clean_df = df.copy()[rank_cols_only]

    # cleaning date_cols
    for col in clean_df.columns:
        clean_df.rename(columns={col: col.strip('*.smartmouth.com/*_')}, inplace=True)

    # transforming data so dates are rows and not columns
    df_melt = pd.melt(clean_df, id_vars=['Keyword'], value_vars=list(clean_df.columns[1:]),
                      var_name='date', value_name='position')

    # formatting to datetime
    df_melt['date'] = pd.to_datetime(df_melt['date'])

    return df_melt


if __name__ == '__main__':

    filename = 'smartmouth_1108_1219_2020_positions.xlsx'
    df = pd.read_excel(filename, skiprows=7, sheet_name='Data')

    print(clean_raw_semrush(df).head())