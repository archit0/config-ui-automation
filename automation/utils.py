import time


def get_till_available(driver, times, attribute, *args, **kwargs):
    for i in range(0, int(times)):
        try:
            ele = getattr(driver, attribute)(*args, **kwargs)
            if ele:
                return ele
        except:
            pass
        # print(f"\t\tTry {i + 1} failed {attribute} {args} {kwargs}")
        time.sleep(1)
    raise Exception(f"Element couldn't be find {attribute} {args} {kwargs}")


def wait_till_this_url(driver, url, times=10, sleep_sec=1):
    for i in range(0, int(times)):
        if driver.current_url == url:
            return True
        time.sleep(sleep_sec)
    raise Exception("Didnt reach the url")
