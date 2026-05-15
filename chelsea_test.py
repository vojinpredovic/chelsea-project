'''
Vojin Predovic and Ryu Hoshino
CSE 163
This is a tester file that uses the chelsea_data_small.csv
to conveniently test the visual and other implementations
of the analysis class.
'''
from chelsea_analysis import ChelseaAnalysis

TEST_PATH = '/Users/vojinpredovic/CSE 163/Project/chelsea_data_small.csv'


def main():
    analysis = ChelseaAnalysis(TEST_PATH)
    analysis.referee_winrate('test_referee_winrate')
    analysis.foul_result('test_foul_result')


if __name__ == '__main__':
    main()
