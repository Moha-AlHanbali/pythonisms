"""This module tests pythonisms features"""

from pythonisms_iterators import url_sanitizer
from pythonisms_decorators import sanitize
from pythonisms_dunder_methods import Node



def test_pythonisms_iterators():
    # Arrange 
    expected = "a%20long%20string"
    
    # Act
    actual = url_sanitizer("a long string")

    # Assert
    assert actual == expected

def test_pythonisms_iterators_case2():
    # Arrange 
    expected = "http://code.org/hour%20of%20code.html"
    
    # Act
    actual = url_sanitizer("http://code.org/hour of code.html")

    # Assert
    assert actual == expected

def test_pythonisms_decorators():
    # Arrange 
    expected = "a%20long%20string"
    
    # Act
    actual = sanitize("a long string")

    # Assert
    assert actual == expected


def test_pythonisms_decorators_case2():
    # Arrange 
    expected = "http://code.org/hour%20of%20code.html"
    
    # Act
    actual = sanitize("http://code.org/hour of code.html")

    # Assert
    assert actual == expected

def test_pythonisms_dunder():
    # Arrange 
    true_node = Node(1)
    false_node = Node(0)
    expected_1 = True
    expected_2 = False

    # Act
    actual_1 = bool(true_node)
    actual_2 = bool(false_node)

    # Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2