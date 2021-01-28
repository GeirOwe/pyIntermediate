# automated testing with pytest
# pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 

from autTesting2 import square, inc

class TestClass:
    def test_inc(self):
        assert inc(4) == 5

    def test_square(self):
        assert square(4) == 16
