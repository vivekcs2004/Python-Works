class MergeIntervals:
    
    
    def solution(self,intervals):

        merged = []

        merged.append(intervals[0])

        for lst in intervals:

            if merged[-1][1]>=lst[0]:

                merged[-1][1]=lst[1]

            else:

                merged.append(lst)

        return merged

merge_instance = MergeIntervals()

print(merge_instance.solution([[4,8],[1,8],[10,12]]))
