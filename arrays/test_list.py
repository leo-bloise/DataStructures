from arrays.list import List
import pytest

def test_len_returns_list_size():
    l = List()

    l.insert_at(0, 1)
    
    assert len(l) == 1

    l.insert_at(1, 2)

    assert len(l) == 2

def test_remove_from_the_middle():
    l = List()

    for i in range(0, 3):
        l.insert_at(i, i + 1)

    removed = l.remove_at(1)

    assert removed == 2
    assert len(l) == 2

    assert l.get(0) == 1
    assert l.get(1) == 3
    

def test_insert_in_the_middle():
    l = List()

    for i in range(0, 3):
        l.insert_at(i, i + 1)

    assert len(l) == 3

    assert l.get(0) == 1
    assert l.get(1) == 2
    assert l.get(2) == 3

    l.insert_at(1, 10)

    assert l.get(0) == 1
    assert l.get(1) == 10
    assert l.get(2) == 2
    assert l.get(3) == 3

def test_insert_at_the_end():
    l = List()

    for i in range(0, 3):
        l.insert_at(i, i + 1)

    assert len(l) == 3

    l.insert_at(len(l), 10)

    assert l.get(0) == 1
    assert l.get(1) == 2
    assert l.get(2) == 3
    assert l.get(3) == 10


def test_get_element_from_list_success():
    l = List()

    l.insert_at(0, 1)

    assert l.get(0) == 1

def test_get_element_from_list_out_of_bounds():
    l = List()

    l.insert_at(0, 1)

    with pytest.raises(IndexError):
        l.get(1)