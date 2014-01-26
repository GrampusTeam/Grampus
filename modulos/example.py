def grampus_modulo():
	return ("ext", example_function, (["METADATA"],"txt",))


def example_function(sFile):
	f = open(sFile, 'r')
	data = {'metadata':f.read()}
	
	return data
