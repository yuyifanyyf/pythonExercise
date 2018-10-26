class Solution:
    def InversePairs(self, data):
        # write code here
        def invPa(data, start, end):
            if end - start <= 1: return 0
            mid = (start + end) / 2
            leftNormal, leftError, rightNormal, rightError = [], [], [], []
            for i in range(start, mid):
                if data[i] < data[mid]:
                    leftNormal.append(i)
                else:
                    leftError.append(i)
            for i in range(mid + 1, end):
                if data[i] > data[mid]:
                    rightNormal.append(i)
                else:
                    rightError.append(i)
            count = len(leftError) * len(rightError) + len(leftError) + len(rightError)
            for i in leftNormal:
                 for j in rightError:
                        if data[i] > data[j]:
                            count+=1
            for i in rightNormal:
                for j in leftError:
                    if data[i] <data[j]:
                        count += 1
            return count + invPa(data, start, mid) + invPa(data, mid + 1, end)
        return invPa(data, 0, len(data))
if __name__ == "__main__":
    s = Solution()
    data = [1,2,3,4,5,6,7,0]
    print(s.InversePairs(data))
