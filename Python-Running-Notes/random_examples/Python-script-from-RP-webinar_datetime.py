import dateutil
import datetime
a = ["2022-12-13:2022-12-15:foo", "2022-12-17:2022-12-18:bar", "2022-12-25:2022-12-28:baz"]
b = ["2022-12-25:2022-12-28:baz", "2022-12-29:2022-12-31:foobar"]
now = datetime.datetime.now()
print(now)


today_now = datetime.datetime.now()
start_date_range = datetime.datetime.strptime("26-11-2017", "%d-%m-%Y")
end = datetime.datetime.strptime("30-11-2017", "%d-%m-%Y")
if start_date_range <= today_now <= end:
    print ("passed")
else:
    print ("failed")

def check_if_a_date_is_in_range(data, key_date_now):
    for e in data:
        if key_date_now:
            pass
