class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        currBoxes, currUnits = 0, 0
        #print(boxTypes)

        for box in boxTypes:
            boxes = min(box[0], truckSize - currBoxes)
            currUnits += boxes * box[1]
            currBoxes += boxes

            if currBoxes == truckSize:
                break

        
        return currUnits
