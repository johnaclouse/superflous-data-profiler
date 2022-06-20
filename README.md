# FlexPy
A flexdashboard alternative based on Jupyter notebook and Bootstrap to create standalone html dashboards in Python


# Flexdashboards

https://pkgs.rstudio.com/flexdashboard/



# Bootstrap

https://getbootstrap.com/docs/4.0/getting-started/introduction/

https://www.w3schools.com/bootstrap/bootstrap_templates.asp

# Code to create Bootstrap layout and components

Initial target:

* column based layout with vertical scrolling
* top navbar
* optional sidebar



# Processing data from CSV files

A CSV file is read into memory. The resulting dataframe is parsed one column at a time. Each column is cast as a Eda abstract object with composite concrete classes implementing different visualiation and statistics for each data type.



# Future work

* Add number of duplicated rows https://github.com/ydataai/pandas-profiling/blob/develop/src/pandas_profiling/model/pandas/duplicates_pandas.py

* Add measures that look at the entire dataframe, not just one column at a time:
    * Missing values https://www.kdnuggets.com/wp-content/uploads/sharma-pandas-profiling-8.png
    * Correlations (top correlated columns)
    


