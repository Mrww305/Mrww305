import unittest
import sys
from unittest import mock

# Add the current directory to sys.path to allow importing chatbot
sys.path.append('.')
from chatbot import get_api_key, call_google_chat_api

class TestGetApiKey(unittest.TestCase):

    @mock.patch('sys.argv', ['chatbot.py', '--api-key', 'TEST_KEY'])
    def test_api_key_provided(self):
        self.assertEqual(get_api_key(), 'TEST_KEY')

    @mock.patch('sys.argv', ['chatbot.py'])
    def test_api_key_missing(self):
        # Argparse with required=True exits with SystemExit code 2 if arg is missing
        with self.assertRaises(SystemExit) as cm:
            get_api_key()
        self.assertEqual(cm.exception.code, 2)

class TestCallGoogleChatApi(unittest.TestCase):

    def test_generic_query(self):
        response = call_google_chat_api('TEST_KEY', 'hello bot')
        self.assertEqual(response, "Placeholder: This is a response from the Google API.")

    def test_car_maintenance_query(self):
        response = call_google_chat_api('TEST_KEY', 'I need an oil change')
        self.assertEqual(response, "Placeholder: This is a car maintenance related response from the Google API.")

    def test_simulated_api_interaction_with_none_key(self):
        # This test demonstrates the current placeholder's behavior.
        # A real API might raise an error with a None key, which the try-except should catch.
        # For the current placeholder, it will just proceed normally.
        response = call_google_chat_api(None, 'test query with None key')
        # Depending on how a real API client handles a None key, this might change.
        # For our placeholder, it doesn't differentiate based on the key's value, only its presence for the print.
        self.assertEqual(response, "Placeholder: This is a response from the Google API.")

    # To truly test the exception handling in call_google_chat_api,
    # we would need to mock something *inside* its try block to raise an error.
    # For example, if it used a library function `send_to_google_api`, we could mock that.
    # For now, the existing structure tests the keyword logic and happy paths.
    # A conceptual test for error handling would look like this if we could inject an error:
    #
    # @mock.patch('chatbot.some_internal_api_call_function', side_effect=Exception("API Failed"))
    # def test_api_call_exception(self, mock_internal_call):
    #     response = call_google_chat_api('TEST_KEY', 'any query')
    #     self.assertEqual(response, "Sorry, I encountered an error trying to process your request.")


if __name__ == '__main__':
    unittest.main()
