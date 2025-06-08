import pytest

from dvc.repo.plots import infer_data_sources


def test_infer_data_sources_none():
    assert infer_data_sources("foo") == ["foo"]

