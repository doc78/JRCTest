import netCDF4 as nc
from netCDF4 import Dataset    
import numpy as np

def load_data(filename):
    ds = nc.Dataset(filename)
    return ds

def save_data(filename, max_values_ta, ds):
    ncfile = Dataset('data/max_ta.nc',mode='w',format='NETCDF4_CLASSIC') 
    print(ncfile)
    lat_dim = ncfile.createDimension('lat', max_values_ta.shape[0])     # latitude axis, yc
    lon_dim = ncfile.createDimension('lon', max_values_ta.shape[1])    # longitude axis, xc

    ncfile.title='Max ta per cell'
    print(ncfile.title)

    ncfile.subtitle="Test data containing max temperature average per cell"
    print(ncfile.subtitle)
    print(ncfile)


    # a conventional way to define "coordinate variables".
    lat = ncfile.createVariable('lat', np.float64, ('lat',))
    lat.units = 'degrees_north'
    lat.long_name = 'latitude'
    lon = ncfile.createVariable('lon', np.float64, ('lon',))
    lon.units = 'degrees_east'
    lon.long_name = 'longitude'
    # Define a 2D variable to hold the data
    max_ta = ncfile.createVariable('max_ta',np.float32,('lat','lon'))
    max_ta.units = 'C' # degrees Celsius
    max_ta.standard_name = 'max_temperature_in_input_timeslot'
    print(max_ta)

    # Write latitudes, longitudes, from input Dataset
    lat[:] = ds['lat'][:]
    lon[:] = ds['lon'][:]
    # Write the data.  This writes the whole 2D netCDF variable all at once.
    max_ta[:,:] = max_values_ta  # Appends data along lat and lon dimension
    print("-- Wrote data, max_ta.shape is now ", max_ta.shape)
    # read data back from variable (by slicing it), print min and max, excluding nan values
    ta_max_masked = np.ma.masked_where(np.isnan(max_ta), max_ta)
    print("-- Min/Max values:", ta_max_masked[:,:].min(), ta_max_masked[:,:].max())

