###############################################################################
#
#   test_quil_tokenizer.py - Unit tests for Quil tokenizer
#
#   Authors: Harley Patton
#   Created on: July 14, 2017
#   Last modified: July 18, 2017
#
###############################################################################

from src.taqos.compiler.tokenizers.quil_tokenizer import *
import pytest

def test_tokenize():
    src = "H 0\n" \
          "CNOT 0 1\n" \
          "RY(3.14159) 1\n"

    expected = [
        {
            "inst": "H",
            "params": None,
            "qubits": [0]
        },
        {
            "inst": "CNOT",
            "params": None,
            "qubits": [0, 1]
        },
        {
            "inst": "RY",
            "params": [3.14159],
            "qubits": [1]
        }
    ]

    assert tokenize(src) == expected

def test_detokenize():
    tokenized = [
        {
            "inst": "H",
            "params": None,
            "qubits": [0]
        },
        {
            "inst": "CNOT",
            "params": None,
            "qubits": [0, 1]
        },
        {
            "inst": "RY",
            "params": [3.14159],
            "qubits": [1]
        }
    ]

    expected = "H 0\n" \
               "CNOT 0 1\n" \
               "RY(3.14159) 1\n"

    assert detokenize(tokenized) == expected

def test_parse():
    token = "CPHASE(3.14159) 0 1"

    expected = {
        "inst": "CPHASE",
        "params": [3.14159],
        "qubits": [0, 1]
    }

    assert parse(token) == expected


def test_deparse():
    token = {
        "inst": "CPHASE",
        "params": [3.14159],
        "qubits": [0, 1]
    }

    expected = "CPHASE(3.14159) 0 1"

    assert deparse(token) == expected

pytest.main()