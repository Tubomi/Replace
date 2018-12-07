def canjump(pos,nums):
    if pos==len(nums)-1:
        return True
    fur=min(pos+nums[pos],len(nums)-1)
    for nexpos in range(pos+1,fur+1):
        print(nexpos)
        if canjump(nexpos,nums):
            return True
    return "失敗しました"
def jumps(nums):
    return canjump(0,nums)
