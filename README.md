# most-active-cookie
Given a cookie log file (.csv) in the following format:
```
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```
This program processes the file and returns the most active cookie for the specified day.

## Example
Running the following commands outputs:
```
>>> python most_active_cookie.py cookie_log.csv -d 2018-12-09
AtY0laUfhglK3lC7
```
```
>>> python most_active_cookie.py cookie_log.csv -d 2018-12-08
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```

To run the test file:
```
>>> python -m unittest test_most_active_cookie.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```

