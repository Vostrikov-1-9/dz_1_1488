from app.matrix3x3 import Matrix3x3
import pytest


@pytest.mark.parametrize(("f1", "f2"), [([[1, 1, 1], [1, 2, 3], [4, 5, 6]], 0),
                                        ([[15, 1, 1], [1, 2, 3], [4, 5, 10]], 74),
                                        ([[-8, -3, 1], [1, 24, 3], [13, 59, 6]], -88)])
def test_determinant(f1, f2):
    m = Matrix3x3(f1)
    f = m.determinant()
    assert f == f2


def test_determinant2():
    m = Matrix3x3([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    f = m.determinant()
    assert f == 0


def test_input(mocker):
    mocker.patch('builtins.input', side_effect=['3', '3', '1', '1', '1', '1', '2', '3', '4', '5', '6'])
    f = Matrix3x3()
    f.input()
    assert f.spisok == [[1, 1, 1], [1, 2, 3], [4, 5, 6]]
