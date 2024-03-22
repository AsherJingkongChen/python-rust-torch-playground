import python_rust_torch_playground as plg
from torch import tensor
import sys


def test_module_doc_presents():
    assert type(plg.__doc__) is str
    assert len(plg.__doc__) > 0


def test_the_answer_of_a_triangle_is_correct():
    answer = plg.the_answer_of_a_triangle()
    assert answer.tolist() == [[2, 4], [0, 2]]


def test_tensor_mat_mul_is_correct():
    answer = plg.tensor_mat_mul(tensor([[1], [2]]), tensor([[3, 4]]))
    assert answer.tolist() == [[3.0, 4.0], [6.0, 8.0]]
