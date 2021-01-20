#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basis of Python Decorator"""

def decorate(function):
    """Decolator function:
    This decorator overrides original 'function' and
    returns 'wrap_function'.
    """
    def wrap_function(*args, **kwargs):
        """Wrapper function:
        This wrapper receives arguments of 'function' and
        returns additional messeage with original 'function'.
        """
        print('Hello from decorated %s.' % function.__name__)
        obj = function(*args, **kwargs)
        return obj
    return wrap_function

def decorate_with_arg(str):
    """Decorator function with arguments:
    This decorator receives an argument 'str' and
    returns 'decorate' function like as mentioned above.
    """
    def decorate(function):
        """Decorator function:
        This decorator overrides original 'function' and
        returns 'wrap_function'.
        """
        def wrap_function(*args, **kwargs):
            """Wrapper function:
            This wrapper receives arguments of 'function' and
            returns additional messeage including decorator's
            argument with original 'function'.
            """
            print('Hi %s from decorated %s' % (str, function.__name__))
            obj = function(*args, **kwargs)
            return obj
        return wrap_function
    return decorate

@decorate
def test_decorator(name):
    """Decorated function:
    This function just shows a message with the argument.
    **Recommended way to be decorated**
    """
    print('Hey %s from decorating %s.' % (name, test_decorator.__name__))

def test_alt_decorator(name):
    """Function:
    This function just shows a message with the argument.
    **Followed code is obsolete way to decorate this function**
    """
    print('Hey %s from decorating %s.' % (name, test_alt_decorator.__name__))
test_alt_decorator = decorate(test_alt_decorator)

@decorate
@decorate_with_arg('Anonymous')
def test_decorators():
    """Decorated function by 2 decorators:
    This function just shows a messeage.
    **Recommended way to be decorated by several decorators and
      decorators having arguments**
    """
    print('Hiya %s.' % test_decorators.__name__)

def test_alt_decorators():
    """Function:
    This function just shows a messeage.
    **Followed codes are obsolete way to decorate this function
      with several decorators having arguments**
    """
    print('Hiya %s.' % test_alt_decorators.__name__)
wrapper = decorate_with_arg('Doe')
test_alt_decorators = decorate(wrapper(test_alt_decorators))

def start_test():
    """Function:
    This function just tests decorator functions and
    decorated functions as declared above.
    """
    # Run decorated functions
    print('#1')
    test_decorator('John')
    print('#2')
    test_alt_decorator('Coward')
    print('#3')
    test_decorators()
    print('#4')
    test_alt_decorators()

if __name__ == '__main__':
    start_test()