'''
Vojin Predovic and Ryu Hoshino
CSE 163
This file uses the SciPy library to conduct
a significance test on the Chelsea data.
'''

import pandas as pd
from scipy import stats

DATA_PATH = '/Users/vojinpredovic/CSE 163/Project/chelsea_data.csv'


def fouls_by_outcome(df: pd.DataFrame) -> tuple:
    '''
    Splits the matches into two groups based on result: wins
    and non-wins. Returns two Series, one with the foul counts
    from wins and one with the foul counts from non-wins.
    '''
    temp = df.copy()
    win_mask = temp['result'] == 'W'
    non_win_mask = temp['result'] != 'W'

    return (temp[win_mask]['fouls'], temp[non_win_mask]['fouls'])


def mann_whitney_fouls(df: pd.DataFrame) -> tuple:
    '''
    Runs a Mann-Whitney U test comparing the number of fouls
    Chelsea commits in wins versus non-wins. Returns the U
    statistic and the p-value as a tuple.
    '''
    win_fouls, non_win_fouls = fouls_by_outcome(df)
    res = stats.mannwhitneyu(win_fouls, non_win_fouls, alternative='two-sided')
    return (res.statistic, res.pvalue)


def get_table_referee(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Returns a new DataFrame with only the referees
    who officiated at least 5 games and splits
    result into either win or no-win.
    '''
    temp = df.copy()
    mask = temp.groupby('referee')['referee'].transform('count') >= 5
    temp = temp[mask].copy()
    temp['outcome'] = temp['result'].apply(lambda x:
                                           'Win' if x == 'W' else 'Non-win')

    return temp


def chi_square_referee(df: pd.DataFrame) -> tuple:
    '''
    Runs a chi-square test of independence on the referees
    and match result. Returns a tuple of the test-statistic,
    p-value, degrees of freedom, and expected values.
    '''
    temp = get_table_referee(df)
    table = pd.crosstab(temp['referee'], temp['outcome'])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    return chi2, p, dof, expected


def chi_square_venue(df: pd.DataFrame) -> tuple:
    '''
    Runs a chi-square test of independence on the venue
    and match result. Returns a tuple of the test-statistic,
    p-value, degrees of freedom, and expected values.
    '''
    temp = df.copy()
    temp['outcome'] = temp['result'].apply(lambda x:
                                           'Win' if x == 'W' else 'Non-win')

    table = pd.crosstab(temp['venue'], temp['outcome'])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    return chi2, p, dof, expected


def report_test(name: str, test_stat: float, p_value: float,
                alpha: float = 0.05) -> None:
    '''
    Prints a formatted summary of a significance test: its name,
    statistic, p-value, and whether it is significant at alpha.
    '''
    print(name)
    print(f'Test statistic: {test_stat}')
    print(f'P-value: {p_value}')
    result = 'significant' if p_value < alpha else 'not significant'
    print(f'Results are {result} at alpha = {alpha}')
    print()


def main():
    df = pd.read_csv(DATA_PATH)
    alpha = 0.05

    u, p_mw = mann_whitney_fouls(df)
    report_test('Mann-Whitney U-test for fouls in win vs non-win games',
                u, p_mw, alpha)

    chi2, p_chi, dof, expected = chi_square_referee(df)
    report_test('Chi-squared test of independence for referees and result',
                chi2, p_chi, alpha)

    chi2_2, p_chi_2, dof_2, expected_2 = chi_square_venue(df)
    report_test('Chi-squared test of independence for venue and result',
                chi2_2, p_chi_2, alpha)


if __name__ == '__main__':
    main()
