from typing import List


class Solution:
    def numberOfWeakCharacters_brute_force(self, properties: List[List[int]]) -> int:
        result = 0
        print(sorted(properties))
        for i in range(len(properties)):
            for j in range(len(properties)):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    properties[i] = [0, 0]
                    result += 1
                    break
        return result

    def numberOfWeakCharacters_improved_brute_force(self, properties: List[List[int]]) -> int:
        result = 0
        properties = sorted(properties)
        length = len(properties)
        for i in range(length - 1):
            if properties[i][0] < properties[-1][0]:
                j = length - 1
                while properties[i][1] >= properties[j][1] and j > i:
                    j -= 1
                if properties[i][1] < properties[j][1] and properties[i][0] < properties[j][0]:
                    result += 1
        return result

    def numberOfWeakCharacters_two_max(self, properties: List[List[int]]) -> int:
        weak_characters = 0
        properties.sort(key=lambda x:(-x[0], x[1]))
        max_attack = properties[0][0]
        max_defence = properties[0][1]
        for i in range(1, len(properties)):
            if properties[i][0] < max_attack and properties[i][1] < max_defence:
                weak_characters += 1
            else:
                max_attack = properties[i][0]
                max_defence = properties[i][1]
        return weak_characters

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak_characters = 0
        properties.sort(key=lambda x:(-x[0], x[1]))
        max_defense = 0
        for _, defense in properties:
            if defense < max_defense:
                weak_characters += 1
            else:
                max_defense = defense
        return weak_characters

properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
properties.sort(key=lambda x: (-x[0], x[1]))
print(properties)

print(Solution().numberOfWeakCharacters(properties))
