###############################################################################
#
#   shell.py - An interactive read-eval-print loop for running TAQOS commands.
#
#   Authors: Aaron Vontell
#   Created on: July 21, 2017
#   Last modified: July 21, 2017
#
###############################################################################

from salsa.salsa import CommandResolver

def start_repl():
    """
    Starts the REPL for TAQOS
    """
    
    print("--------- TAQOS REPL V0.0.1 ---------")
    
    # Represents the current shell mode
    current_mode = "TAQOS"
    
    # If true, the failure will be indicated within the prompt
    last_failed = False
    
    while True:
        
        prompt = ("X " if last_failed else "") + current_mode + "> "
        last_failed = False
        request = raw_input(prompt)
        post_process = CommandResolver.process(request)
        
        # If a post process was requested, act on it
        if post_process["type"] == "none":
            continue
        if post_process["type"] == "quit":
            break
        else:
            if post_process["type"] == "success":
                if post_process["message"] is not None:
                    print(post_process["message"])
            elif post_process["type"] == "fail":
                last_failed = True
                if post_process["message"] is not None:
                    print(post_process["message"])
            continue