import functools
def  log(func):
    @functools.wraps(func)
    def  wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
——————————————————————————
@log
def now():
    print("123")
——————————————————————————
now.__name__


****************************************************
import functools
def  log(text):
    def  decorator(func):
        @functools.wraps(func)
        def  wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
———————————————————————————
@log('xad')#非常有意思的一个地方如果为@log 则now1.__name__返回的是decorator
def now1():
    print("123")
——————————————————————————
now1.__name__#log('xad')有text内容 则now1.__name__返回的是now1
