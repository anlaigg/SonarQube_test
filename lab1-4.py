class Solution:
    def Jump(self,Nums:list)->int:
        n=len(nums)
        sum_max=nums[0]
        num=1
        #print(n,sum_max)
        while(sum_max<n-1):
            t=sum_max
            #print(n,sum_max)
            for i in range(num,t+1):
                #print(nums[i]+i,sum_max)
                if(nums[i]+i>sum_max):
                    sum_max=nums[i]+i
                    #print(sum_max)
            num=num+1
        #print(sum_max)
        return num
                
nums = input().strip('[').strip(']').split(',')
nums = [int(num) for num in nums]
print(nums)
#print(nums)
sol=Solution()
print(sol.Jump(nums))
