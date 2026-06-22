'''
Vojin Predovic
CSE 163
This file introduces data visualization and exploration for
Chelsea data from the Premier League, seasons 24-25 and
25-26
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

DATA_PATH = '/Users/vojinpredovic/CSE 163/Project/chelsea_data.csv'


class ChelseaAnalysis:
    def __init__(self, path: str) -> None:
        '''
        Initializes the ChelseaAnalysis class by loading
        the dataset from the given path.
        '''
        self._df = pd.read_csv(path)

    def referee_winrate(self, save: str = 'referee_winrate.png') -> None:
        '''
        Visualizes a horizontal bar graph for referee win %
        based on each referee, and includes a 50% mark for
        comparison. Removes referees with low game
        count under 2 to avoid skewed numbers.
        '''

        df = self._df[self._df.groupby('referee')['referee'].transform(
            'count') > 2]

        ref = df.groupby('referee').agg(
            games=('result', 'count'),
            wins=('result', lambda x: (x == 'W').sum())
        ).reset_index()
        ref['win_pct'] = ref['wins'] / ref['games'] * 100
        ref = ref.sort_values('win_pct')

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(ref['referee'], ref['win_pct'])
        ax.axvline(50, color='red', linestyle='--', label='50%')
        ax.set_xlabel('Win %')
        ax.set_title('Chelsea Win % by Referee '
                     'for the 24/25 and 25/26 Premier League Seasons')
        ax.legend()

        plt.tight_layout()
        plt.savefig(save, bbox_inches='tight')

    def foul_result(self, save: str = 'fouls_result.png') -> None:
        '''
        Visualizes a stacked and standardized bar graph
        that shows the proportion of match results based on
        a range of foul counts.
        '''

        df = self._df.copy()

        df['foul_bin'] = pd.cut(df['fouls'], bins=[4, 8, 11, 14, 21],
                                labels=['5-8', '9-11', '12-14', '15+'])
        counts = df.groupby(['foul_bin', 'result']).size().unstack(
            fill_value=0)

        proportions = counts.div(counts.sum(axis=1), axis=0)
        proportions.plot(kind="bar", stacked=True, legend=True)

        plt.xlabel('Foul Count Range')
        plt.ylabel('Proportion of Games')
        plt.title('Chelsea Results by Foul Count For The '
                  '24/25 and 25/26 Premier League Seasons')
        plt.tight_layout()
        plt.xticks(rotation=0)
        plt.savefig(save, bbox_inches='tight')

    def venue_result(self, save: str = 'venue_result.png') -> None:
        '''
        Visualizes win rate showing the proportion of wins
        for each venue, either home or away.
        '''

        df = self._df.copy()
        df['outcome'] = df['result'].apply(lambda x:
                                           'Win' if x == 'W' else 'Non-win')

        counts = df.groupby(['venue', 'outcome']).size().unstack(fill_value=0)
        proportions = counts.div(counts.sum(axis=1), axis=0)
        proportions.plot(kind='bar', stacked=True, legend=True)

        plt.xlabel('Venue')
        plt.ylabel('Win proportion')
        plt.title('Chelsea Results by Venue For The 24/25 and '
                  '25/26 Premier League Seasons')
        plt.tight_layout()
        plt.savefig(save, bbox_inches='tight')


def main():
    analysis = ChelseaAnalysis(DATA_PATH)
    analysis.referee_winrate()
    analysis.foul_result()
    analysis.venue_result()


if __name__ == '__main__':
    main()
