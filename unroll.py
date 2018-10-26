def printMatrix(matrix):
    # write code here
    def unroll(m, ru, rd, cl, cr):
        if not m: return []
        if not (ru <= rd and cl <= cr):return []
        retList = []
        if ru <= rd:
            retList.extend(m[ru][cl:cr+1])
            ru += 1
        if cl <= cr:
            temp = [row[cr] for row in m[ru:rd+1]]
            retList.extend(temp)
            cr -= 1
        if ru <= rd:
            temp = m[rd][cl:cr+1]
            temp.reverse()
            retList.extend(temp)
            rd -= 1
        if cl <= cr:
            temp = [row[cl] for row in m[ru:rd + 1]]
            temp.reverse()
            retList.extend(temp)
            cl += 1
        return retList + unroll(m, ru, rd, cl, cr)
    if not matrix:return []
    ru, rd, cl, cr = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    return unroll(matrix, ru, rd, cl, cr)
if __name__ == "__main__":
    m = [[1],[2],[3],[4],[5]]
    print(m)
    print(printMatrix(m))
