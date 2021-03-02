class RatingGenerator():
    def __init__(self, rating=0):
        self.rating = rating

    def simple_word_by_word_rating(self, list1, list2):
        score = 0.0
        #Swap lists to avoid index error if list1 longer than list2
        if len(list1)>len(list2):
            temp = list1
            list1 = list2
            list2 = temp
        for pos in range(len(list1)):
            if list1[pos]==list2[pos]:
                score += 1
        #Use len list1 as denominator since we know it is the longer list (reduce ratio for lists of different lengths)
        total_items = len(list1)
        return score / total_items

    def rate(self, list1, list2):
        #If the lists are identical, give a rating of 1
        if list1==list2:
            self.rating = 1
        #If the lists are not identical, score by the ratio of identical words (same word, same place in the list) to non-identical words
        else:
            self.rating = self.simple_word_by_word_rating(list1, list2)

        #print(self.rating)
        return self.rating

