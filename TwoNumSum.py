'''
# O(n^2) time | O(1) space
def TwoNumSum(array, targetNum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            print(f'firstNum = {firstNum}')
            print(f'secondNum = {secondNum}')
            print('='*20)
            if firstNum + secondNum == targetNum:
                return [firstNum, secondNum]
    return []
'''
'''
# O(nLog(n)) | O(1) space
def TwoNumSum(array, targetNum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        print(array)
        print(f'targetNum = {targetNum}')
        print(f'left = {array[left]}')
        print(f'right = {array[right]}')
        print(f'currentSum = {currentSum}')
        print('='*20)
        if currentSum == targetNum:
            return [array[left], array[right]]
        elif currentSum < targetNum:
            left += 1
        elif currentSum > targetNum:
            right -= 1
    return []
'''


# O(n) time | O(n) space
def TwoNumSum(array, targetNum):
    nums = {}
    for num in array:
        potentialMatch = targetNum - num
        print(array)
        print(f'num = {num}')
        print(f'targetNum = {targetNum}')
        print(f'potentialMatch = {potentialMatch}')
        print(f'nums = {nums}')
        print('='*20)
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


numlist = [3, 5, -4, 8, 11, 1, -1, 6]

res = TwoNumSum(numlist, 10)
print(res)
