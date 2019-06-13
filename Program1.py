def appendElementsToList(listForNumbers):
    listLength = int(input("How many elements do you want to append? "))
    for i in range(listLength):
        elementInp = int(input("What element do you want to append? "))
        listForNumbers.append(elementInp)
    return listForNumbers

def chekIfElementsAreEqual(listForCheck):
    for i in range(len(listForCheck)):
        for j in range(len(listForCheck)-1):
            if listForCheck[i] == listForCheck[j]:
                outputBool = True
    return outputBool


##    ##    ## Main part ##    ##    ##    ##    ##    
myList = []
fullList = appendElementsToList(myList)
result = chekIfElementsAreEqual(fullList)

if result == True:
    print("Result: All elements in the given list are equal.")
else:
    print("Result: Not all elements in the given list are equal.")
