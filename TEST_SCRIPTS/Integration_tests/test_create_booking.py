"""
Author: Perumal
obj: create and verify POST requests
TC1: verify status code, headers
TC2: verify body--> booking_id
TC3: verify json is valid
"""
import pytest

@pytest.mark.run(order=1)
def test_create_booking_tc1():
    assert True == True   # assertion (expected result = actual result)

@pytest.mark.run(order=2)
def test_create_booking_tc2():
    assert True == False

@pytest.mark.run(order=3)
def test_create_booking_tc3():
    assert True == True