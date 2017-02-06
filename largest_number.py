'''

    WatrHub Technical Interview
    Candidate: Jessy Yameogo
    
    Problem: Given a random list of integers (all positive) 
        e.g. [9, 95, 99, 23, 4] return the concatenation of all the numbers 
        that is the largest possible number
    
    @param {integer[]} nums
    @return {string}
    
    O(nlogn) time
    O(logn) space
    
'''
class LargestNumber(object):
    def concatenate(self, nums):
        if not nums or len(nums) == 0:
            return '0'
            
        return ''.join(self.quicksort([str(n) for n in nums]))

        
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[i] + nums[i + 1] < nums[i + 1] + nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
            else:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                j -= 1
            
        return self.quicksort(nums[:i]) + [nums[i]] + self.quicksort(nums[i + 1:])
        
    
numbers = {
    '99995423': [9, 95, 99, 23, 4],
    '0': [],
    '87887': [87, 878],
    '99713': [97, 9, 13],
    '9955171': [9, 1, 95, 17, 5],
    '99799713': [97, 9, 13, 979],
    '10100': [100, 10],
    '13213': [13, 132],
    '8788717': [87, 17, 878],
    '93621221': [936, 21, 212],
    '11101110': [1, 1101, 110],
}
def test(f):
    for k,v in numbers.items():
        print('{} -> {} ({})'.format(v, f(v), 'correct' if f(v) == k else 'incorrect, should be {}'.format(k)))

test(LargestNumber().concatenate)