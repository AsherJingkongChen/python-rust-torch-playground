use pyo3::prelude::*;
use pyo3_tch::{tch::Tensor, PyTensor};

/// It returns a 2D-tensor as a computation result
/// 
/// # Examples
/// ```python
/// import python_rust_torch_playground as plg
/// 
/// answer = plg.the_answer_of_a_triangle()
/// assert answer.tolist() == [[2, 4], [0, 2]]
/// ```
#[pyfunction]
fn the_answer_of_a_triangle() -> PyResult<PyTensor> {
    let t = Tensor::from_slice2(&[[1, 2], [0, 1]]);
    Ok(PyTensor(t * 2))
}

/// It multiplies two tensors by calling the `matmul` method
/// 
/// # Examples
/// ```python
/// import python_rust_torch_playground as plg
/// from torch import tensor
/// 
/// answer = plg.tensor_mat_mul(tensor([[1],[2]]), tensor([[3,4]]))
/// assert answer.tolist() == [[3.0, 4.0], [6.0, 8.0]]
/// ```
#[pyfunction]
fn tensor_mat_mul(a: PyTensor, b: PyTensor) -> PyResult<PyTensor> {
    Ok(PyTensor(a.matmul(&b)))
}

/// A Python module implemented in Rust, using PyTorch
/// 
/// ## Details
/// The Rust library also dynamically links to the `PyTorch` library,
/// which is written in C++ and provides Python API.
/// 
/// ## References
/// - [PyTorch](https://pytorch.org/)
#[pymodule]
fn python_rust_torch_playground(_: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(the_answer_of_a_triangle, module)?)?;
    module.add_function(wrap_pyfunction!(tensor_mat_mul, module)?)?;
    Ok(())
}
