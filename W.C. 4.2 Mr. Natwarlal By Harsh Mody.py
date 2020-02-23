inputList = list(map(int, input("Enter A List : ").split(',')))
sumOfEvenPile = 0
sumOfOddPile = 0
for i in range(0, len(inputList)):
    if i % 2 == 0:
        sumOfEvenPile = sumOfEvenPile + inputList[i]
    else:
        sumOfOddPile = sumOfOddPile + inputList[i]
if sumOfEvenPile > sumOfOddPile:
    print("Natwarlal Wins !!!", sumOfEvenPile + sumOfOddPile)
else:
    print("Natwarlal Wins !!!", sumOfEvenPile + sumOfOddPile)