from typing import List

class Solution:
    def countOfPairs(self, numberOfHouses: int, houseX: int, houseY: int) -> List[int]:
        resultArray = [0] * numberOfHouses

        for startHouse in range(1, numberOfHouses + 1):
            for endHouse in range(startHouse + 1, numberOfHouses + 1):
                distanceBetweenHouses = min(
                    abs(startHouse - endHouse),
                    abs(startHouse - houseX) + 1 + abs(houseY - endHouse),
                    abs(startHouse - houseY) + 1 + abs(houseX - endHouse)
                )
                resultArray[distanceBetweenHouses - 1] += 2

        return resultArray
