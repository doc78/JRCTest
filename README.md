# JRCTest
 JRC Test script computes max average temperature over timesteps
 
1. Uses dataset `ta.nc` from the repository [https://github.com/ec-jrc/lisflood-lisvap/tree/master/tests/data/input/glofas](https://github.com/ec-jrc/lisflood-lisvap/tree/master/tests/data/input/glofas).

2. Computes the maximum of the average temperature (ta) for each cell for the input period. 

3. Writes the output as a map using [https://unidata.github.io/python-training/workshop/Bonus/netcdf-writing/](https://unidata.github.io/python-training/workshop/Bonus/netcdf-writing/)

4. Makes unit tests to verify the solution

Requirements:

JRCTest requires python package `netCDF4`

Data dir:
Dataset should be dowloaded into `data` folder. In this repository you will already find `ta.nc` file downloaded on April 15th 2021.
Output file will be stored in the same folder and named `max_ta.nc`

Usage:
```
python JRCTest.py
```
Unit tests:

Unit test is already set up to run after the output generation. 
To run unit tests on already generated output use the command:
```
python -m unittest -v JRCTest.py
```
Unit test will check correctness of computation of the max values as well as latitude and longitude values of the output file. Other 3 slower tests are included to check every single value to be less or equal to the max value. To enable them just remove `@unittest.skip(...)` from the script.