
def parse(grammar):
    # Extract every line of the file and put it into lines array
    lines = [line.strip() for line in grammar]
    # Representing the grammar as a python dict
    grammar_dict = {}
    # first elements in lines is consisted of all starting symbols
    starting_symbols = filter(None, lines[0].split(" "))
    # Extract rules from lines array and enrich the grammar dict
    for line in lines[1:]:
        if line.strip() != "":
            rule = [x.strip() for x in line.split("->")]
            if len(rule) != 2:
                l = None
                r = None
            else:
                l, r = rule
                # When we have multiple choices
                r = filter(None, [x.strip().split(' ') for x in r.split(" | ")])

            if not l in grammar_dict.keys():
                grammar_dict[l] = []
            grammar_dict[l] = grammar_dict[l] + r

    # Extract grammars in the form of A -> B C
    grammar_rules_with_variables = dict_traversal(grammar_dict, 1)
    # Extract grammars in the form of A -> a
    grammar_rules_with_terminals = dict_traversal(grammar_dict, 2)

    # Extract the list of terminals
    terminals = []
    for variables in grammar_dict.keys():
        for rules in grammar_dict[variables]:
            for rule in rules:
                if not rule in grammar_dict.keys() and \
                        not rule in terminals:
                    terminals = terminals + [rule]

    return starting_symbols, grammar_dict.keys(), terminals, \
           grammar_rules_with_variables, grammar_rules_with_terminals


# Search into a dictionary
# gets out the rules in the form
# of A -> B C or A -> a based on length
def dict_traversal(dic, length):
    rules = {}
    for key, values in dic.iteritems():
        rules[key] = []
        for value in values:
            if len(value) == length:
                rules[key] = rules[key] + [value]
        if len(rules[key]) == 0:
            del rules[key]
    return rules
