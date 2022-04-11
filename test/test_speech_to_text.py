'''test for chats module'''
import unittest
import requests


class ApiTest(unittest.TestCase):
    '''test api response'''
    api_url = "http://127.0.0.1:5000"
    chats_url = f"{api_url}/chats"
    text_chat_url = f"{api_url}/chat/2"
    audio_chat_url = f"{api_url}/chat/1"

    def test_get_all_chats(self):
        '''test get all chats'''

        req = requests.request('GET', ApiTest.chats_url)
        self.assertEqual(req.status_code, 200)

    def test_get_text_chat(self):
        '''test get text chat'''

        req = requests.request('GET', ApiTest.text_chat_url)
        self.assertEqual(req.status_code, 200)

    def test_get_audio_chat(self):
        '''test get audio chat'''

        req = requests.request('GET', ApiTest.audio_chat_url)
        self.assertEqual(req.status_code, 200)


if __name__ == "__main__":
    unittest.main()
