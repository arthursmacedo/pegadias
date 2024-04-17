# Copyright (c) 2024 pegadias developers
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Pegadias project.
#

def test_get_days(file):
    """Test if the function get_days return the correct values."""
    assert get_days('viena.csv') == ['2023/01/01']
    
def test_generate_request_file(self):

    """
    Test case for the generate_request_file function.

    This test verifies the behavior of generate_request_file by supplying example input data,
    generating request files using the function, and then comparing the content of the generated
    request file with an expected IMS 2.0 request string.
    """
    
    # Example input data
    date_list = ['2023/01/01']
    station_code = 'test'
    
    # Call the function to generate request files
    generate_request_file(date_list, station_code)
    
    # Define the expected IMS 2.0 request string
    expected_request = (
        'begin ims2.0\n'
        'msg_type request\n'
        'msg_id mseed_test\n'
        'time 2023/01/01 00:00:00 to 2023/01/01 23:59:59\n'
        'sta_list TEST\n'
        'chan_list BDF\n'
        'waveform ims2.0:ms_st2_512\n'
        'stop\n'
    )
    
    # Read the generated request file
    req_file_path = 'TEST_2023_01_01.req'
    with open(req_file_path, 'r') as req_file:
        generated_request = req_file.read()

    # Assert that the generated request matches the expected request
    assert generated_request == expected_request, "Generated request does not match expected request"