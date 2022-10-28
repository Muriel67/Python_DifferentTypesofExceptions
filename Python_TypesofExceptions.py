#!/usr/bin/env python
# coding: utf-8

# # PYTHON EXCEPTIONS

# This documents contains different types of python exceptions with examples related to each exceptions.
# This document is prepared for better understanding ang to give more details bout the different types of exceptions which arises in python.
# 

# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning

# # StopIteration 
# Raised when the next() method of an iterator does not point to any object 
# 
# What is an iterator ?
# Iterator is an object which holds values which can be iterated upon .
# It uses __next__() method to move to the next value in the iterator.
# When the __next__() method tries to move to the next values but there are no new values. StopIteration exception is raised 
# 
# source : www.pylenin.com/blogs/stop-iteration-exception/

# ## Example 1 for StopIterationException

# In[6]:


x = [1,2,3,4]
y = iter(x)
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())


# ## Example 2 for StopIterationException

# In[9]:


x = "hello"
y = iter(x)
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())


# How to catch StopIteration ??
# Use the StopIteration Class

# In[13]:


x = [1,2,3,4]
y = iter(x)
try:
    print(y.__next__())
    print(y.__next__())
    print(y.__next__())
    print(y.__next__())
    print(y.__next__())
    print(y.__next__())
except StopIteration as e:
    print("StopIteration Exception is handled")


# # ArithmeticError
# Base class for all errors involving numeric calculation. It occurs when an error is encountered during numeri calculations.
# Under arithmetic error 
# 1) FloatingPoint Error
# 2) Overflow error
# 3) ZeroDivision Error

# In[ ]:




