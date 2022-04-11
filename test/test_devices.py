'''test for devices module'''
import unittest
import requests


class ApiTest(unittest.TestCase):
    '''test devices response'''
    api_url = "http://127.0.0.1:5000"
    devices_url = f"{api_url}/devices"
    single_device_url = f"{api_url}/device/1"
    new_device_url = f"{api_url}/device/7"
    apts_url = f"{api_url}/appointments"
    single_apt_url = f"{api_url}/appointment/1"
    device_obj = {"Device_ID": 8, "Device_Name": "test_device2"}

    def test_get_all_devices(self):
        '''test get all devices'''
        req = requests.request('GET', ApiTest.devices_url)
        self.assertEqual(req.status_code, 200)

    # def test_add_new_device(self):
    #     """test add a new device"""
    #     req = requests.request(
    #         'POST', ApiTest.devices_url, json=ApiTest.device_obj)
    #     self.assertEqual(req.status_code, 201)

    def test_get_single_device(self):
        '''test get single device'''
        req = requests.request('GET', ApiTest.single_device_url)
        self.assertEqual(req.status_code, 200)

    # def test_update_device(self):
    #     '''test update device'''
    #     req = requests.request(
    #         'PUT', ApiTest.new_device_url, json=ApiTest.device_obj)
    #     self.assertEqual(req.status_code, 204)

    def test_delete_device(self):
        '''test for deleting device'''
        req = requests.request('DELETE', ApiTest.new_device_url)
        self.assertEqual(req.status_code, 200)

    def test_get_all_apts(self):
        '''test get all appointments'''
        req = requests.request('GET', ApiTest.apts_url)
        self.assertEqual(req.status_code, 200)

    def test_get_single_apt(self):
        '''test get single appointment'''
        req = requests.request('GET', ApiTest.single_apt_url)
        self.assertEqual(req.status_code, 200)


if __name__ == "__main__":
    unittest.main()
