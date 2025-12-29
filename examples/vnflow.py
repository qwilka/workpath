"""
"""
import copy
import functools
import hashlib
import inspect
import json


def argdict2hash(argdict):
    """Calculate a hash value for an argdict."""
    adjson = json.dumps(argdict, sort_keys=True)
    m = hashlib.md5()
    m.update(adjson.encode())
    _hash = m.hexdigest()
    print(f"adjson={adjson}")
    print(f"_hash={_hash}")
    return _hash
    

def ttest2(a, b, c=10):
	varnms = ttest.__code__.co_varnames
	print(f"varnms={varnms}")
	print(f"ttest.__dict__={ttest.__dict__}")
	print(f"locals()={locals()}")
	print(f"dir(ttest)={dir(ttest)}")
	for ii in range(ttest.__code__.co_argcount):
		ag = locals().get(varnms[ii])
		print(f"{ii} {varnms[ii]} {ag}")
	return a+b+c    


def ff(func):
	func_argcount = func.__code__.co_argcount 
	func_varnames = func.__code__.co_varnames
	sig = inspect.signature(func)
	argdict = {}
	for name, para in sig.parameters.items():
		if para.default is inspect.Parameter.empty:
			argdict[name] = None
		else: 
			argdict[name] = para.default
	print(f"argdict={argdict}")
	#print(f"func.__code__.co_varnames={varnms}")
	#print(f"unc.__dict__={func.__dict__}")
	#print(f"locals()={locals()}")
	#print(f"dir(unc)={dir(func)}")	
	#for ii in range(func.__code__.co_argcount):
	#	ag = locals().get(varnms[ii])
	#	print(f"{ii} {varnms[ii]} {ag}")
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		#varnms = wrapper.__code__.co_varnames
		#print(f"wrapper.__code__.co_varnames={varnms}")
		#print(f"unc.__dict__={wrapper.__dict__}")
		#print(f"locals()={locals()}")
		#print(f"dir(unc)={dir(wrapper)}")
		#for ii in range(argc):
		#	ag = locals().get(varnms[ii])
		#	print(f"{ii} {varnms[ii]} {ag}")
		print(f"sig={sig}")
		print(f"sig.parameters={sig.parameters}")
		print(f"wrapper args={args}, kwargs={kwargs}")
		if len(args) > func_argcount:
			print(f"WARNING: function «{func.__name__}» called with {len(args)} arguments (expected max. {func_argcount} arguments.)")
			retVal = None
		else:
			_argd = copy.deepcopy(argdict)
			_argd.update(kwargs)
			for ii, _arg in enumerate(args):
				_argd[func_varnames[ii]] = _arg
			print(f"_argd={_argd}")
			_hash = argdict2hash(_argd)
			print(f"func(*args, **kwargs)={func(*args, **kwargs)}")
			retVal = func(**_argd)
			print(f"func(**_argd)={retVal}")
		return retVal
	return wrapper


#@ff
def ttest(x, y, z=99):
	return x+y+z

ttest = ff(ttest)

