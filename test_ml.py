import pytest
# TODO: add necessary import
from ml.model import (compute_model_metrics, inference, save_model, load_model, train_model)
import numpy as np
# TODO: implement the first test. Change the function name and input as needed
def test_compute_model_metrics():
    """
   Check that precision, recall, and F1 equal the expected values
    """
    # Your code here
    y = np.array([1, 1, 0, 0])
    preds = np.array([1, 0, 1, 0])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert precision == 0.5
    assert recall == 0.5
    assert fbeta == 0.5

# TODO: implement the second test. Change the function name and input as needed
def test_save_and_load_model(tmp_path):
    """
    # Verifies pickle serialization
    """
    # Your code here
    orig_object = {"model": "random_forest", "random_state": 19}
    file_path = tmp_path / "test_model.pkl"
    save_model(orig_object, file_path)
    loaded_object = load_model(file_path)
    assert loaded_object == orig_object


# TODO: implement the third test. Change the function name and input as needed
def test_train_model_and_inference():
    """
    # Checks that training and prediction work together as expected
    """
    # Your code here
    X = np.array([[0], [1], [2], [3]])
    y = np.array([0, 0, 1, 1])
    trained = train_model(X, y)
    preds = inference(trained, X)
    assert len(preds) == len(y)
