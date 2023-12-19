import unittest
from contextlib import redirect_stdout
from io import StringIO
import most_active_cookie

class MyTestCase(unittest.TestCase):
    def test_wrong_args(self):
        args = ['most_active_cookie.py', 'cookie_log.csv']
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit) as cm:
                most_active_cookie.check_argument_length(args)
        self.assertEqual(cm.exception.code, 1)

    def test_wrong_date(self):
        args = ['most_active_cookie.py', 'cookie_log.csv', '-d', '15999-01']
        with redirect_stdout(StringIO()):
            with self.assertRaises(SystemExit) as cm:
                most_active_cookie.check_date_input(args)
        self.assertEqual(cm.exception.code, 1)

    def test_no_cookie(self):
        args = ['most_active_cookie.py', 'cookie_log.csv', '-d', '2018-12-10']
        with redirect_stdout(StringIO()):
            cookies = most_active_cookie.get_active_cookie(args)
        self.assertFalse(cookies)

    def test_correct_cookie(self):
        args = ['most_active_cookie.py', 'cookie_log.csv', '-d', '2018-12-09']
        with redirect_stdout(StringIO()):
            cookies = most_active_cookie.get_active_cookie(args)
        self.assertEqual(cookies[0], 'AtY0laUfhglK3lC7')

    def test_correct_cookies(self):
        args = ['most_active_cookie.py', 'cookie_log.csv', '-d', '2018-12-08']
        with redirect_stdout(StringIO()):
            cookies = most_active_cookie.get_active_cookie(args)
        self.assertEqual(cookies, ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'])

if __name__ == '__main__':
    unittest.main()