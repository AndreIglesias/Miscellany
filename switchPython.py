import collections, itertools, operator, __future__
from functools import reduce
from random import randint
from copy import deepcopy

class switch(collections.MutableMapping):
		def __init__(self, option, swt, brk, *args, **kw):
			super(collections.MutableMapping, self).__init__(*args, **kw) #self.__class__
			self.storage = swt
			self.brk = brk
			self.update(dict(*args, **kw))

		def __getitem__(self, key):
			try: return self.storage[self.__keytransform__(key)]
			except: 
				try: return self.storage[True]
				except: pass

		def __setitem__(self, key, value):
			try:
				if(type(key)==bool):
					key = str(key)
				super(switch, self).__setitem__(key, value)
				self.__dict__.update({key: value})
			except KeyError:
				super(switch, self).__setitem__(key, [])
			self[key].append(value)

		def __iter__(self): return iter(self.storage)

		def __repr__(self): return str(self.storage)

		def __keytransform__(self, key): return key

		def __delitem__(self): pass
		def __len__(self): pass

# main -------------------------------------------------------

def foo():	return ":D" # function
switch.function = foo 	# adding a method to the switch class

op = 55
s = switch(op,
	{
		1:132,
		op>3:list(filter(lambda p: ((2**(p))%3==1), range(1,20))),
		op==50:

'''for i in [1,2,3,4]
	print(i)''',

		2:switch.function(),
		3:foo(),
		'A': "Hello"
	}, True)
print(s)