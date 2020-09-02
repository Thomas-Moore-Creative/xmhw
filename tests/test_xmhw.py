#!/usr/bin/env python
# Copyright 2020 ARC Centre of Excellence for Climate Extremes
# author: Paola Petrelli <paola.petrelli@utas.edu.au>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from xmhw.xmhw import threshold #, detect, mhw_filter 
from xmhw_fixtures import *
from numpy import testing as nptest

def test_mhw_filter():
#mhw_filter(exceed, minDuration, joinGaps, maxGap):
    assert True

def test_threshold(clim_oisst, oisst_ts):
    clim = threshold(oisst_ts)
    #threshold(temp, climatologyPeriod=[None,None], pctile=90, windowHalfWidth=5, smoothPercentile=True, 
    th1 = clim['thresh'].sel(lat=-42.625, lon=148.125)
    seas1 = clim['seas'].sel(lat=-42.625, lon=148.125)
    th2 = clim['thresh'].sel(lat=-41.625, lon=148.375)
    seas2 = clim['seas'].sel(lat=-41.625, lon=148.375)
    print(clim_oisst.thresh1.values[40:80])
    print(th1.values[40:80]) 
    nptest.assert_array_almost_equal(clim_oisst.thresh1.values,th1.values, decimal=2, verbose=True) 
    nptest.assert_array_almost_equal(clim_oisst.thresh2.values,th2.values) 
    nptest.assert_array_almost_equal(clim_oisst.seas1.values,seas1.values) 
    nptest.assert_array_almost_equal(clim_oisst.seas2.values,seas2.values) 

def test_detect():
    assert True
#detect(temp, clim=None, minDuration=5, joinAcrossGaps=True, maxGap=2, maxPadLength=False, coldSpells=False, 

def test_mhw_ds():
#mhw_ds(start, end, events, ts, clim):
    assert True
