glossary = {
    'if' : 'Execute this block of code only if a certain condition is True.',
    'for' : 'Repeat this block of code once for each item in a sequence.',
    'in' : 'Inside of or from this collection.',
    'and' : 'Both conditions must be True.',
    'or' : 'At least one condition must be True.',
    };
glossary['sort()'] = "Sort the elements of a list."
glossary['sorted()'] = "Give me a sorted copy of a list" +\
                    " leaves the original alone."
glossary['items()'] = "Give me both the key and the value."
glossary['values()'] = "Give me the values."
glossary['keys()'] = "Give me the keys."
 

for python_term, meaning in glossary.items() :
    print(python_term + " : " + meaning);