

# Python Docstrings as mentioned above provides a convenient way of associating documentation with Python modules, functions, classes, and methods.

# Declare and access a docstrings

# # ex1 : using triple single quotes
# def my_func():
#     '''Demonstrates triple single quotes docstrings and does nothing really.'''
#     return None


# # print("Using __doc__:")
# # print(my_func.__doc__)

# print("Using help:")
# help(my_func)

# # EX2
# # Using triple double quotes
# def my_func():
#     """Demonstrates triple double quotes. docstrings and does nothing really"""
#     return None

# print("Using __doc__:")
# print(my_func.__doc__)

# print("Using help:")
# help(my_func)


                    # One-line Docstrings

# def power(a,b):
#     """Returns arg1 raised to power arg2."""
#     return a*b
# print(power.__doc__)



# Multiline Docstring

# def my_func(arg1):
#     """
#     Summary line.

#     Extended description of function.

#     Parameters:
#     arg1(int):Description of arg1

#     Returns:
#     int:Description of return value

#     """
    
#     return arg1

# print(my_func.__doc__)


# Indentation in Docstring

# Docstrings in Classes

class ComplexNumber:
    """
    This is a class for mathmatical operations on complex numbers.

    Attributes:
        real (int):The real part of complex number.
        imag (int):The imaginary part of complex number.
    """

    def __init__(self,real,imag):
        """
        The constructor for ComplexNumber class.

        Parameters:
           real (int):The real part of complex number.
           imag (int):The imaginary part of complex number.
        """

    def add(self,num):
        """
        The function to add two complex numbers.

        Parameters:
             num(ComplexNumber):The complex number to be added.

        Returns:
             ComplexNumber:A complex number which contains the sum.
        """
        re=self.real+num.real
        im=self.imag+num.imag

        return ComplexNumber(re,im)

help(ComplexNumber) #to acess class docs
help(ComplexNumber.add) #to access methods docs