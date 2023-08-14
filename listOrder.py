def ascendingOrder(orderList):

    orderedResult = []
    confirmResult = []

    for a in range(len(orderList)):
        orderedResult.append(orderList[a])
    for b in range(len(orderedResult)):
        confirmResult.append(orderList[b])
    #print(orderedResult)

    isSame = False

    while isSame == False:
        for c in range(len(orderedResult)):
            confirmResult[c] = orderedResult[c]

        for x in range(len(orderList)-1):
            if orderedResult[x] > orderedResult[x+1]:
                tempVal = orderedResult[x]
                orderedResult[x] = orderedResult[x+1]
                orderedResult[x+1] = tempVal

        for y in range(len(orderedResult)):
            if orderedResult[y] == confirmResult[y]:
                isSame = True
            else:
                isSame = False
                break
            
    return orderedResult

def descendingOrder(orderList):

    orderedResult = []
    confirmResult = []

    for a in range(len(orderList)):
        orderedResult.append(orderList[a])
    for b in range(len(orderedResult)):
        confirmResult.append(orderList[b])
    #print(orderedResult)

    isSame = False

    while isSame == False:
        for c in range(len(orderedResult)):
            confirmResult[c] = orderedResult[c]

        for x in range(len(orderList)-1):
            if orderedResult[x] < orderedResult[x+1]:
                tempVal = orderedResult[x]
                orderedResult[x] = orderedResult[x+1]
                orderedResult[x+1] = tempVal

        for y in range(len(orderedResult)):
            if orderedResult[y] == confirmResult[y]:
                isSame = True
            else:
                isSame = False
                break

    return orderedResult