'''
Vojin Predovid and Ryu Hoshino
CSE 163
This file introduces data visualization and exploration for
Chelsea data from the Premier League, seasons 24-25 and parts of
25-26 (unfinished)
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

DATA_PATH = 'Project/chelsea_data.csv'


def wins_per_referee(df: pd.DataFrame, ref: str) -> str:
    '''
    Calculates total wins per ref and returns result
    '''

    mask = (df['result'] == 'W') & (df['referee'] == ref)

    return f'{ref} has recorded {mask.sum()} wins'


def main():
    df = pd.read_csv(DATA_PATH)
    print(wins_per_referee(df, 'Anthony Taylor'))


if __name__ == '__main__':
    main()
