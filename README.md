# Superflous data profiler
A Python based data profiling tool designed to support early stage exploratory data analysis and data profiling in high volume projects where there is value in having a single HTML page to summarize the data from each source.

Initial target:

# Processing data from CSV files

A CSV file is read into memory. The resulting dataframe is parsed one column at a time. Each column is cast as a Eda abstract object with composite concrete classes implementing different visualiation and statistics for each data type.

# Future work

* Add number of duplicated rows https://github.com/ydataai/pandas-profiling/blob/develop/src/pandas_profiling/model/pandas/duplicates_pandas.py

* Add measures that look at the entire dataframe, not just one column at a time:
    * Missing values https://www.kdnuggets.com/wp-content/uploads/sharma-pandas-profiling-8.png
    * Correlations (top correlated columns)
    


