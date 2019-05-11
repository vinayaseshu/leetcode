class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lists=nums;
        ln = len(lists)
        resultlist =[];
        print('Printing all possible pairs from list')
        for i in range(0, ln):
            for j in range(i + 1, ln):
                if (lists[i] + lists[j]) == target:
                    resultlist.append(i);
                    resultlist.append(j);
        return resultlist


if __name__ == '__main__':
    l = [2, 7, 11, 15]
    k = 9

    a = Solution();
    print('Priniting all list of pairs matching to sum using list comprehension', a.twoSum(l, k));