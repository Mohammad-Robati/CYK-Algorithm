import numpy as np


def check_if_sentence_is_in_language(starting_symbols, variables,
                                     grammar_rules_with_terminals, grammar_rules_with_variables, words):
    # words of the string e.g. " he jumps " -> ['he', 'jumps'] -> length == 2
    length_of_tape = len(words)
    # number of all symbols in the grammar
    symbols_size = len(variables)
    # main table of the cyk algorithm, initializing every element as false
    table = np.zeros((length_of_tape, length_of_tape, symbols_size))

    # For each i = 1 to n
    for i in range(0, length_of_tape):
        # For each unit production Aj -> ai, set table[i,1,j] = true.
        for R, A in grammar_rules_with_terminals.iteritems():
            for a in A:
                if words[i] == a[0]:
                    table[0, i, variables.index(R)] = 1

    # For each i = 2 to n -- Length of span
    for i in range(2, length_of_tape + 1):
        # For each j = 1 to n-i+1 -- Start of span
        for j in range(1, length_of_tape - i + 2):
            # For each k = 1 to i-1 -- Partition of span
            for k in range(1, i):
                # For each production A -> B C
                for l, R in grammar_rules_with_variables.iteritems():
                    for r in R:
                        # if table[k,j,B] and table[i-k,j+k,C] then set table[i,j,A] = true
                        if table[k - 1, j - 1, variables.index(r[0])] == 1 and \
                                table[i - k - 1, j + k - 1, variables.index(r[1])] == 1:
                            table[i - 1, j - 1, variables.index(l)] = 1

    for r in starting_symbols:
        j = variables.index(r)
        if table[length_of_tape - 1, 0, j] == 1: return True
    return False
