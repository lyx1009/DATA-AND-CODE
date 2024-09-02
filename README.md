# DATA-AND-CODE
# This repository contains:
1. data (collected and used)
2. code (scraping and processing via Python and Stata 17)

# data files: 
the first part (1-3).xlsx files after Python and Excel cleaning /// second part (4-6) .dta files after Stata processing

1. London-flat.xlsx
2. London-terrace.xlsx
3. London-detached.xlsx

4. London-flat-proceed.dta
5. London-terrace-proceed.dta
6. London-detached-proceed.dta

# code files:
Python
1. Python scraping code.py (to scrap information from Rightmove.com)
2. Python processing code 1 (merge by region).py (to group boroughs by Inner and Outer London)
3. Python processing code 2 (cleaning).py (to clean row data after scraping and merging)
Stata 17
4. Stata processing code.do (do file of Stata, to process database and do Empirical test)

It is noted that:
The code is shown as an example of one of the boroughs or room types. 
In practice, we manually collected all the data by replacing the index of 32 boroughs and 3 house types.

# The index of each borough in Rightmove.com:
Barking and Dagenham  5E61400
Barnet 5E93929
Bexley 5E93932
Brent 5E93935
Bromley 5E93938
Camden 5E93941
Croydon 5E93944
Ealing 5E93947
Enfield 5E93950
Greenwich 5E61226
Hackney 5E93953
Hammersmith and Fulham 5E61407
Haringey 5E61227
Harrow 5E93956
Havering 5E61228
Hillingdon 5E93959
Hounslow 5E93962
Islington 5E93965
Kensington and Chelsea 5E61229
Kingston upon Thames 5E93968
Lambeth 5E93971
Lewisham 5E61413
Merton 5E61414
Newham 5E61231
Redbridge 5E61537
Richmond upon Thames 5E61415
Southwark 5E61518
Sutton 5E93974
Tower Hamlets 5E61417
Waltham Forest 5E61232
Wandsworth 5E93977
Westminster 5E93980

# Boroughs are grouped by Inner and outer
1. Inner London (12 boroughs):
Camden
Greenwich
Hackney
Hammersmith and Fulham
Islington
Kensington and Chelsea
Lambeth
Lewisham
Southwark
Tower Hamlets
Wandsworth
Westminster
2. Outer London (20 boroughs):
Barking and Dagenham
Barnet
Bexley
Brent
Bromley
Croydon
Ealing
Enfield
Haringey
Harrow
Havering
Hillingdon
Hounslow
Kingston upon Thames
Merton
Newham
Redbridge
Richmond upon Thames
Sutton
Waltham Forest

