import pandas as pd


def combine_dublicate_entries(df):
    combined_df = df.groupby(['Brand', 'Reference'], as_index=False)[
        'Quantity'].sum()

    combined_df = combined_df.sort_values(
        by=['Brand', 'Reference']).reset_index(drop=True)
    return combined_df


def simplify_brand_names(df):
    df["Brand"] = df["Brand"].str.split(" ").str[0]
    return df
