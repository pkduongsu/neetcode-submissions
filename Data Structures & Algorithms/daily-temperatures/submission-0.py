class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Input: temperatures: List[int] - array of temperatures where each element represents daily temperature on ith day
        #Output: result: List[int] - array of the number of days after ith day before a warmer temperature appears
        #Question: what if there are no days that have higher temperature than the current one?
        # -> result[i] = 0

        #Ex: [19, 20, 18, 21, 30, 35]
        # result: [1, 2, 1, 1, 1, 0]

        #brute force solution: use a nested loop to go through every combinations and calculate the number of days till
        #higher temperature through a variable that is defined for each temperatures array element
        #if result is found (higher temperature date), append to result array

        res = []

        for i in range(len(temperatures)):
            cnt = 0
            print("temperatures i: " + str(temperatures[i]))
            for j in range(i + 1, len(temperatures)):
                print("temperatures j: " + str(temperatures[j]))
                if (temperatures[j] > temperatures[i]):
                    cnt += 1
                    break
                else:
                    cnt += 1
                if j == len(temperatures) - 1:
                    cnt = 0
            res.append(cnt)

        return res   



        