class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        if event1[1] == event2[0] or event1[0] == event2[1]:
            return True

        end1 = event1[1][:2] + event1[1][3:]
        start1 = event1[0][:2] + event1[0][3:]
        start2 = event2[0][:2] + event2[0][3:]
        end2 = event2[1][:2] + event2[1][3:]

        return int(start2) < int(end1) and int(start1) < int(end2)
