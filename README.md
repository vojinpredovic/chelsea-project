# Chelsea Data Analysis

**By Vojin Predovic and Ryu Hoshino**

This project explores Chelsea FC's Premier League match data from the
2024–25 and 2025–26 seasons. It investigates whether match outcomes are 
associated with the referee, the venue (home vs away), and the number 
of fouls Chelsea commit. The project produces both data visualizations 
and statistical significance tests.

## Required Installations
* `pandas`
* `scipy`
* `matplotlib.pyplot`
* `seaborn`

You can install them with
```
pip install pandas scipy seaborn matplotlib
```
No other environment, tools, or external downloads are required, and 
the csv data files are included in the files, along with images of
what each visualization should look like.

## Files

**Data**
 
- `chelsea_data.csv` — The full dataset: one row per Chelsea match, with
  columns for date, opponent, goals for/against, result, venue, fouls,
  formations, referee, penalties, cards, and season.
- `chelsea_data_small.csv` — A small subset of the data used only for
  conveniently testing the code.
  
**Code**
 
* `chelsea_analysis.py` — Defines the `ChelseaAnalysis` class, which loads
  the dataset and generates the project's visualizations: Chelsea win %
  by referee, match results by foul-count range, and results by venue.
  Each chart is saved as a `.png` file.
* `chelsea_results.py` — Uses SciPy to run the project's significance
  tests: a Mann-Whitney U test comparing fouls in wins vs non-wins, and
  chi-square tests of independence for referees and for venue against
  match result. Prints each test's statistic, p-value, and significance
  result to the terminal.
* `chelsea_test.py` — A tester file that runs the `ChelseaAnalysis`
  visualizations on `chelsea_data_small.csv` to conveniently verify they
  work. Not required to reproduce the main results.

