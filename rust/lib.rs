use pyo3::prelude::*;
use pyo3_tch::{tch::Tensor, PyTensor};

/// It returns a 2D-tensor as a computation result
#[pyfunction]
fn the_answer_of_a_triangle() -> PyResult<PyTensor> {
    let t = Tensor::from_slice2(&[[1, 2], [0, 1]]);
    Ok(PyTensor(t * 2))
}

/// It multiplies two tensors by calling the `matmul` method
#[pyfunction]
fn tensor_mat_mul(a: PyTensor, b: PyTensor) -> PyResult<PyTensor> {
    Ok(PyTensor(a.matmul(&b)))
}

/// A Python module implemented in Rust, using PyTorch
#[pymodule]
fn python_rust_torch_playground(_: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(the_answer_of_a_triangle, module)?)?;
    module.add_function(wrap_pyfunction!(tensor_mat_mul, module)?)?;
    Ok(())
}
