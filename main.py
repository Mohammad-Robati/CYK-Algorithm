from cyk import *
from parser import *

grammar = "grammar.txt"

sentence = "she eats"

starting_symbols, variables, terminals, grammar_rules_with_terminals, \
grammar_rules_with_variables = parse(open(grammar))

exist_in_language = check_if_sentence_is_in_language(starting_symbols, variables, grammar_rules_with_terminals,
                                                     grammar_rules_with_variables, sentence.split(" "))

print "\n"

if exist_in_language:
    print "\"", sentence, "\"", "is member of the language"
else:
    print "\"", sentence, "\"", "is not member of the language"

print "\n"

# Output :
#           " she eats with a fork " is member of the language
