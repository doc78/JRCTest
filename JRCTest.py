from utils import load_data, save_data

import netCDF4 as nc
from netCDF4 import Dataset    # Note: python is case-sensitive!
import numpy as np

import unittest

class TestMaxTa(unittest.TestCase):

    @unittest.skip("Skip elem one by one testing")
    def test_max_ta_elem_onebyone(self):
        ds = load_data("data/ta.nc")
        ta = ds['ta'][:,:,:]
        ds_max = load_data("data/max_ta.nc")
        ta_max=ds_max['max_ta'][:,:]
        for it,iln,ilg in np.ndindex(ta.shape):   
            if ~np.isnan(ta[it,iln,ilg]):
                self.assertLessEqual(ta[it, iln, ilg], ta_max[iln, ilg], "Found greater temp")

    @unittest.skip("Skip cell by cell testing")
    def test_max_ta_cellbycell(self):
        ds = load_data("data/ta.nc")
        ta = ds['ta'][:,:,:]
        ds_max = load_data("data/max_ta.nc")
        ta_max=ds_max['max_ta'][:,:]
        for iln,ilg in np.ndindex(ta_max.shape):   
            if ~np.isnan(ta[:,iln,ilg].max()):
                self.assertLessEqual(ta[:,iln,ilg].max(), ta_max[iln, ilg], "Found greater temp")

    @unittest.skip("Skip cumulative value array elems testing")
    def test_max_ta_values(self):
        ds = load_data("data/ta.nc")
        ta = ds['ta'][:,:,:]
        ds_max = load_data("data/max_ta.nc")
        ta_max=ds_max['max_ta'][:,:]
        ta_max_values=ta.max(0)
        for iln,ilg in np.ndindex(ta_max.shape):   
            if ~np.isnan(ta_max_values[iln,ilg]):
                self.assertEqual(ta_max_values[iln,ilg], ta_max[iln, ilg], "TA max values not equal")

    def test_max_ta(self):
        ds = load_data("data/ta.nc")
        ta = ds['ta'][:,:,:]
        ds_max = load_data("data/max_ta.nc")
        ta_max=ds_max['max_ta'][:,:]
        ta_max_values=ta.max(0)
        ta_max_values_masked = np.ma.masked_where(np.isnan(ta_max_values), ta_max_values)
        ta_max_masked = np.ma.masked_where(np.isnan(ta_max), ta_max)
        self.assertTrue((ta_max_values_masked == ta_max_masked).all())

    def test_lat_values(self):
        ds = load_data("data/ta.nc")
        lat = ds['lat'][:]
        ds_max = load_data("data/max_ta.nc")
        lat_in_max=ds_max['lat'][:]
        self.assertTrue((lat_in_max == lat).all())

    def test_lon_values(self):
        ds = load_data("data/ta.nc")
        lon = ds['lon'][:]
        ds_max = load_data("data/max_ta.nc")
        lon_in_max=ds_max['lon'][:]
        self.assertTrue((lon_in_max == lon).all())



def main():
    ds = load_data("data/ta.nc")
    print(ds)
    for dim in ds.dimensions.values():
        print(dim)
    ta = ds['ta'][:,:,:]
    max_values_ta=ta.max(0)

    save_data("data/max_ta.nc", max_values_ta, ds)

    print('Running unit tests...')
    unittest.main()

if __name__ == '__main__':
    main()
