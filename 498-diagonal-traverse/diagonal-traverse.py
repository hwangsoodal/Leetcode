class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in dic:
                    dic[i+j] = [mat[i][j]]
                else:
                    dic[i+j].append(mat[i][j])

        for entry in dic.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans