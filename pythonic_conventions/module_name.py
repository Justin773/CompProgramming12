class ExceptionName(Exception):
    pass

def running_this_wont_work():
    raise ExceptionName()
