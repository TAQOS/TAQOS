###############################################################################
#
#   compiler.py - A functional quantum instruction compiler
#
#   Authors: Harley Patton
#   Created on: July 12, 2017
#   Last modified: July 18, 2017
#
###############################################################################

import networkx as nx
from utils import *
import src.taqos.compiler.tokenizers.quil_tokenizer as quil_tokenizer
import src.taqos.compiler.tokenizers.quipper_tokenizer as quipper_tokenizer
import src.taqos.compiler.tokenizers.qasm_tokenizer as qasm_tokenizer

tokenizers = {
    "quil": quil_tokenizer,
    "quipper": quipper_tokenizer,
    "qasm": qasm_tokenizer
}

def compile(path_to_src, path_to_dest, connections, tunables, file_type=None):
    """
    Three-pass compiler for quantum instructions.
    Performs following steps:

    * Read source file
    * Tokenize source code
    * Pass 1 (Route instructions according to chip locality)
    * Pass 2 (Expand instructions according to known gate set)
    * Pass 3 (Trim away redundant instructions)
    * Detokenize compiled code
    * Write to destination

    :param path_to_src: path to the source code (.quil)
    :param path_to_dest: path to the desired destination (.quil)
    :param connections: list of connections between qubits
    :param tunables: set of tunable qubits (all others are fixed)
    :param file_type: the type of quantum instruction language
    """

    # if not provided a file type, infer from file extension
    if file_type == None:
        file_type = path_to_src.split(".")[-1]

    assert file_type in tokenizers
    tokenizer = tokenizers[file_type]

    graph = build_graph(connections)

    with open(path_to_src, 'r') as file:
        src = file.read()

    tokens = tokenizer.tokenize(src)

    tokens = first_pass(tokens, graph)

    #tokens = second_pass(tokens, gates)

    #tokens = third_pass(tokens, gates)

    compiled = tokenizer.detokenize(tokens)

    with open(path_to_dest, 'w') as file:
        file.write(compiled)


def first_pass(tokens, graph):
    """
    Routes tokenized instructions according to chip locality.

    :param tokens: list of tokenized instructions
    :param graph: graph of chip connections
    :return: routed list of tokenized instructions
    """

    ret = []

    paths = nx.shortest_path(graph)

    for token in tokens:

        qubits = token["qubits"]

        if len(qubits) == 1:
            ret.append(token)
            continue

        elif len(qubits) == 2:
            path = paths[qubits[0]][qubits[1]]
            if path == qubits:
                ret.append(token)
                continue
            else:
                i = 0
                while i < len(path) - 2:
                    new_inst = {
                        "inst": "SWAP",
                        "params": None,
                        "qubits": [path[i], path[i + 1]]
                    }
                    ret.append(new_inst)
                    i += 1

                new_inst = {
                    "inst": token["inst"],
                    "params": token["params"],
                    "qubits": [path[i], path[i + 1]]
                }
                ret.append(new_inst)

                while i > 0:
                    new_inst = {
                        "inst": "SWAP",
                        "params": None,
                        "qubits": [path[i - 1], path[i]]
                    }
                    ret.append(new_inst)
                    i -= 1


        else:
            raise Exception("Only 1 and 2 qubit gates")

    return ret

