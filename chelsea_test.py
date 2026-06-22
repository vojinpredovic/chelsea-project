'''
Vojin Predovic
CSE 163
This files tests the functionality of the visualizations
and the results class helper methods.
'''
import pandas as pd
from chelsea_analysis import ChelseaAnalysis
from chelsea_results import (fouls_by_outcome, get_table_referee,
                             chi_square_venue)

TEST_PATH = '/Users/vojinpredovic/CSE 163/Project/chelsea_data_small.csv'


def test_fouls_by_outcome():
    '''
    Checks that fouls_by_outcome splits the small dataset into the
    correct win and non-win groups. The small file has 6 wins and 8
    non-wins, with foul totals of 62 and 103 respectively.
    '''
    df = pd.read_csv(TEST_PATH)
    win_fouls, non_win_fouls = fouls_by_outcome(df)
    assert len(win_fouls) == 6
    assert len(non_win_fouls) == 8
    assert win_fouls.sum() == 62
    assert non_win_fouls.sum() == 103


def test_get_table_referee():
    '''
    Checks that get_table_referee keeps only referees with at least
    five matches and labels outcomes correctly. In the small file,
    only Anthony Taylor has officiated enough games.
    '''
    df = pd.read_csv(TEST_PATH)
    table = get_table_referee(df)
    assert len(table) == 6
    assert set(table['referee']) == {'Anthony Taylor'}
    assert set(table['outcome']) <= {'Win', 'Non-win'}
    assert (table['outcome'] == 'Win').sum() == 3
    assert (table['outcome'] == 'Non-win').sum() == 3


def test_chi_square_venue():
    '''
    Checks that chi_square_venue builds a 2x2 table and
    returns one degree of freedom on the small dataset.
    '''
    df = pd.read_csv(TEST_PATH)
    chi2, p, dof, expected = chi_square_venue(df)
    assert dof == 1


def main():
    test_fouls_by_outcome()
    test_get_table_referee()
    test_chi_square_venue()
    print('All assert tests passed')

    analysis = ChelseaAnalysis(TEST_PATH)
    analysis.referee_winrate('test_referee_winrate.png')
    analysis.foul_result('test_foul_result.png')
    analysis.venue_result('test_venue_result.png')


if __name__ == '__main__':
    main()
