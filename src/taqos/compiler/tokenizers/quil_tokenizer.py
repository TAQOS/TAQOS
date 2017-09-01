###############################################################################
#
#   quil_tokenizer.py - Utilities for tokenizing and detokenizing Quil code
#
#   Authors: Harley Patton
#   Created on: July 12, 2017
#   Last modified: July 18, 2017
#
###############################################################################

def tokenize(src):
    """
    Breaks a Quil program up into instruction tokens.

    :param src: Quil code in string form
    :return: list of tokenized instructions
    """

    tokenized = src.split("\n")
    while tokenized[-1] == "":
        tokenized.pop()
    return map(parse, tokenized)

def detokenize(tokens):
    """
    Combines instruction tokens back into a Quil program

    :param tokens: list of tokenized instructions
    :return: Quil code in string form
    """

    tokens = map(deparse, tokens)
    combine = lambda x, y :  x + "\n" + y
    return reduce(combine, tokens) + "\n"

def parse(token):
    """
    Parses a token for its instruction, parameter, and qubits.

    :param token: instruction token
    :return: mappings of parsed token components
    """

    terms = token.split(" ")

    i = 0

    # get instruction name
    while i < len(terms[0]) and terms[0][i] != "(":
        i += 1
    inst = terms[0][:i]

    # get parameter
    if i < len(terms[0]) and terms[0][i] == "(":
        j = i
        while terms[0][j] != ")":
            j += 1
        param = [float(terms[0][i + 1 : j])]
    else:
        param = None

    # get qubits
    qubits = list(map(int, terms[1:]))

    parsed = {
        "inst": inst,
        "params": param,
        "qubits": qubits}

    return parsed

def deparse(token):
    """
    Combine a token's isntruction, parameters, and qubits
    back into a readable string.

    :param token: mappings of parsed token components
    :return: instruction token
    """

    inst_str = token["inst"]
    params = token["params"]
    if params != None:
        assert len(params) == 1
        inst_str += "({0})".format(params[0])
    for qubit in token["qubits"]:
        inst_str += " {0}".format(qubit)

    return inst_str

