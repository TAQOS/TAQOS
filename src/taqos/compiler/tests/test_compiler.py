###############################################################################
#
#   test_compiler.py - Unit tests for quantum instruction compiler
#
#   Authors: Harley Patton
#   Created on: July 14, 2017
#   Last modified: July 18, 2017
#
###############################################################################

from src.taqos.compiler.compiler import *
from src.taqos.compiler.utils import *
import pytest

def test_first_pass():
    connections = [(0, 1), (1, 2), (2, 3)]
    graph = build_graph(connections)

    tokens = [
        {
            "inst": "CNOT",
            "params": None,
            "qubits": [0, 3]
        }
    ]

    expected = [
        {
            "inst": "SWAP",
            "params": None,
            "qubits": [0, 1]
        },
        {
            "inst": "SWAP",
            "params": None,
            "qubits": [1, 2]
        },
        {
            "inst": "CNOT",
            "params": None,
            "qubits": [2, 3]
        },
        {
            "inst": "SWAP",
            "params": None,
            "qubits": [1, 2]
        },
        {
            "inst": "SWAP",
            "params": None,
            "qubits": [0, 1]
        }
    ]

    assert first_pass(tokens, graph) == expected

pytest.main()