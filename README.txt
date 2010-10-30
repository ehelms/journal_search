How to use:

The main entry point is comb.py.  From there you can run the following:

Functions
-------------------
python comb.py test

This serves to run all provided tests.

------------------
python comb.py search

This runs a search without an upper bound, instead the setting STOPPING_THRESHOLD is used to determine when to stop the search.  See settings.py.sample for more information.

------------------
python comb.py search [number]

This runs a search that sets an upper bound on the number of search results.  While not exact, this search does return +/- 10 results of the target number.

------------------
python comb.py combine

This attempts to combine each search criteria's results into one master list while eliminating duplicates.
