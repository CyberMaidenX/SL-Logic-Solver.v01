#importing libraries
#Note: This program runs on python3
import itertools

#function to create a dictionary of propositional variables
def createDict(varlist):
   return dict(zip(varlist, [False]*len(varlist)))

#function to display the truth table
def displayTable(varlist, truthtable):
    for x in varlist:
        print(x, end="\t")
    print("Output")
    for x in truthtable:
        for y in x:
            print(y, end="\t")
        print()

#function to evaluate the truth value of a sentence
def evaluateSentence(sentence, truthdict):
    for x in sentence:
        if x not in truthdict:
            return None
    return eval(sentence, truthdict)

#function to evaluate the truth value of a set of sentences
def evaluateSet(sentences, truthdict):
    result = []
    for x in sentences:
        result.append(evaluateSentence(x, truthdict))
    return result

#main program
def main():
    print("Please enter the propositional variables as comma separated values: ")
    variables = input().split(",")
    truthdict = createDict(variables)
    truthtable = list(itertools.product([True, False], repeat=len(variables)))
    displayTable(variables, truthtable)
    print("Please enter the formulas separated by comma: ")
    sentences = input().split(",")
    result = evaluateSet(sentences, truthdict)
    print("The evaluated result is: " + str(result))

#calling the main program
main()
