from inspect import Parameter, Signature

class Descriptor:
	def __init__(self, name=None):
		self.name = name

	def __get__(self, instance):
		print("Get", self.name)
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		print("Set", self.name, value)
		instance.__dict__[self.name] = value

	def __del__(self, instance):
		print("Delete", self.name)
		del instance.__dict__[self.name]

class Typed(Descriptor):
	ty = object  # Expected type
	def __set__(self, instance, value):
		if not isinstance(value, self.ty):
			raise TypeError("Expectd %s" % self.ty)
		super().__set__(instance, value)

class Positive(Descriptor):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError("Value must be > 0")
		super().__set__(instance, value)

class Sized(Descriptor):
	def __init__(self, *args, maxlen, **kwargs):
		self.maxlen = maxlen
		super().__init__(*args, **kwargs)

	def __set__(self, instance, value):
		if len(value) > self.maxlen:
			raise ValueError("Too long string")
		super().__set__(instance, value)

class Integer(Typed):
	ty = int

class Float(Typed):
	ty = float

class String(Typed):
	ty = str

class PositiveInteger(Integer, Positive):
	pass

class PositiveFloat(Float, Positive):
	pass

class SizedString(String, Sized):
	pass

def make_signature(names):
	return Signature(
		Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
		for name in names)

class StructMeta(type):
	def __new__(cls, clsname, bases, clsdict):
		clsobj = super().__new__(cls, clsname, bases, clsdict)
		sig = make_signature(clsobj._fields)
		setattr(clsobj, '__signature__', sig)
		return clsobj

class Structure(metaclass=StructMeta):
	_fields = []
	def __init__(self, *args, **kwargs):
		bound = self.__signature__.bind(*args, **kwargs)
		for name, val in bound.arguments.items():
			setattr(self, name, val)

class Stock(Structure):
	_fields = ['name', 'shares', 'price']
	name = SizedString('name', maxlen=10)
	shares = PositiveInteger('shares')
	price = PositiveFloat('price')

# try import this file and inspect
# print(inspect.signature(Stock))
#