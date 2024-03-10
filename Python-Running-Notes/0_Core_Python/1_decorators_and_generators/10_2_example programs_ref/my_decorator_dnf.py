import time
import functools 
def timer(some_func):
	def wrapper(*args, **kwargs):
		t1= time.time()
		some_func()
		t2 = time.time()
		print (f'{some_func.__name__} took {t2 - t1} seconds to execute')
		
	return wrapper
	

@timer
def my_func():
	time.sleep(3)

my_func()