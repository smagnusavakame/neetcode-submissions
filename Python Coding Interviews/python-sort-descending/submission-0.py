from typing import List


def sort_words(words: List[str]) -> List[str]:
    ##Input : here is a list of words 
    ##output : is a list of owrds returned sorted in descending orderee
    #edge casews, consider if the word in itself is empty, or is in some form of location, 
    """plan:
    use the sort feature, 
    take in the list of words, sort with parameter as true, and then return the sorted words"""
    words.sort(reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
