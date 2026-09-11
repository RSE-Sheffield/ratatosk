from __future__ import annotations

import importlib.metadata

import ratatosk as m


def test_version() -> None:
    assert importlib.metadata.version("ratatosk") == m.__version__
