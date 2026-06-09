# Chelsea Data Analysis 

**By Vojin Predovic**

This project explores Chelsea FC's Premier League match data from the
2024–25 and 2025–26 seasons. It investigates whether match outcomes are 
associated with the referee, the venue (home vs away), and the number 
of fouls Chelsea commit. The project produces both data visualizations 
and statistical significance tests.

## Required Installations
* `pandas`
* `scipy`
* `matplotlib`
* `seaborn`

You can install them with
```
pip install pandas scipy seaborn matplotlib
```

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

## Instructions For Running

1. **Install the libraries**

   Install the 4 required libraries with the above pip command if not already
   installed.

3. **Place all files in one folder**

   Place the three `.py` files and the two `.csv` file in one folder.

5. **Update File Paths**

   Each `.py` file has a path constant near the top, replace this with the file
   path of each `.csv` file on your machine. If each `.csv` is in the same folder
   as the `.py` files, you can set these to just the file name.

   * In `DATA_PATH`, set it to the path of `chelsea_data.csv`
   * In `TEST_PATH`, set it to the path of `chelsea_data_small.csv`

6. **Run `chelsea_analysis.py` to generate the visualizations**

   You can either run it using the run button in the top right or
   paste this in the terminal
   ```
   python chelsea_analysis.py
   ```
   This will save the 3 `.png` files into the folder you ran it from.

7. **Run `chelsea_results.py` to summarize the statistical findings**
   You can either run it using the run button in the top right or
   paste this in the terminal
   ```
   python chelsea_results.py
   ```
   This will print the test-statistics, p-values, and results in
   the terminal.

8. **(Optional) Run `chelsea_test.py` to generate test visualizations**
   You can either run it using the run button in the top right or
   paste this in the terminal
   ```
   python chelsea_test.py
   ```
   This will save the 3 `.png` files in the folder you ran it from,
   use this to check the visualizations of the `chelsea_data_small.csv`
   file.
   
