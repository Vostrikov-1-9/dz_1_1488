from app.matrix import Matrix
import pytest


def test_init():
    a = Matrix()
    assert a.spisok == [[0]]


def test_input(mocker):
    mocker.patch('builtins.input', side_effect=['3', '3', '1', '1', '1', '1', '2', '3', '4', '5', '6'])
    f = Matrix()
    f.input()
    assert f.spisok == [[1, 1, 1], [1, 2, 3], [4, 5, 6]]


def test_str():
    z = Matrix([[2, 1, 8], [3, 4, 6]])
    q = str(z)
    assert q == '2\t1\t8\n3\t4\t6'
