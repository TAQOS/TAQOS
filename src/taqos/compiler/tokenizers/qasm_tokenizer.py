###############################################################################
#
#   qasm_tokenizer.py - Utilities for tokenizing and detokenizing Qasm code
#
#   Authors: Harley Patton
#   Created on: July 18, 2017
#   Last modified: July 18, 2017
#
###############################################################################

def tokenize(src):
    """
    Breaks a QASM program up into instruction tokens.

    :param src: QASM code in string form
    :return: list of tokenized instructions
    """

    pass


def detokenize(tokens):
    """
    Combines instruction tokens back into a QASM program

    :param tokens: list of tokenized instructions
    :return: QASM code in string form

    """
    pass


def parse(token):
    """
    Parses a token for its instruction, parameter, and qubits.

    :param token: instruction token
    :return: mappings of parsed token components
    """

    pass


def deparse(token):
    """
    Combine a token's isntruction, parameters, and qubits
    back into a readable string.

    :param token: mappings of parsed token components
    :return: instruction token
    """

    pass

