class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    
                    temp.append(arr[i-1][j-1]+ arr[i-1][j])
            arr.append(temp)
        return arr
