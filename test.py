def countSort(inArr):
    output = [0 for i in range(len(inArr))]
    C = [0 for i in range(256)]
    # Store the count of each character
    for i in inArr:
        C[ord(i)] += 1
    # C[i] contains actual position of this character
    for i in range(256):
        C[i] += C[i-1]
    # Build the output character array
    for i in range(len(inArr)):
        output[C[ord(inArr[i])]-1] = inArr[i]
        C[ord(inArr[i])] -= 1
    return output

print(countSort("UniversityOfColoradoAtDenver"))
