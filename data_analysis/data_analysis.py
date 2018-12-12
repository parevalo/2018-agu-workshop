"""
Analysis data function used to download and process some termperature time
series from Berkeley Earth.
"""

import numpy as np
import requests

def generate_url(location):
    """Generate download URL for any location"""
    url=f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-TAVG-Trend.txt'
    return url


def download_data(location):
    """Download data for a given location"""
    url = generate_url(location)
    response = requests.get(url)
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data


def moving_average(data, width):
    """Calculate a moving average for a given width
    :param data: Input data
    :param width: Width in samples
    """
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, data.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])

    return moving_avg


def test_moving_avg():
    avg = moving_average(np.ones(10), 2)
    assert np.all(np.isnan(avg[0:2]))
    assert np.all(np.isnan(avg[-2:]))
    assert np.allclose(avg[2:-2] == 1, 1)
