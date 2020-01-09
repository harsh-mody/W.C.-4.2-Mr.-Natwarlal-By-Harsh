array = list(map(int, input("Please Enter The List : ").split(",")))
earningsOfWinner = sum(array)
scoreOfNatwarlal = 0
scoreOfOponent = 0
count = 0
lengthOfArray = len(array)
while lengthOfArray >= 0:
    count = count + 1
    if count % 2 != 0:
        if array[0] > array[-1]:
            scoreOfNatwarlal = scoreOfNatwarlal + array[0]
            del array[0]
        elif array[0] < array[-1]:
            scoreOfNatwarlal = scoreOfNatwarlal + array[-1]
            del array[-1]
        lengthOfArray = lengthOfArray - 1
    else:
        if array[0] > array[-1]:
            scoreOfOponent = scoreOfOponent + array[0]
            del array[0]
        elif array[0] < array[-1]:
            scoreOfOponent = scoreOfOponent + array[-1]
            del array[-1]
        lengthOfArray = lengthOfArray - 1
if scoreOfNatwarlal > scoreOfOponent:
    print("Natwarlal Wins!!, His Earnings", earningsOfWinner)
elif scoreOfOponent > scoreOfNatwarlal:
    print("Oponent Wins!!, His Earnings", earningsOfWinner)