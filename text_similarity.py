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

    #Adding a computation that gives higher ratings to unordered but similar lists
    def set_rating(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)

        rating=0
        if set1 == set2:
            rating = 1
        else:
            rating = float(len(set1.intersection(set2)))/len(set1.union(set2))

        return rating

    #For fun, adding a recursive Levenshtein distance calculation, a computation based on the number of edits to make strings the same
    #Full disclosure, had to look up this algorithm, but I thought it would be a neat calculation to include
    #https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    def levenshtein_distance(self, list1, list2):
        if len(list1) < len(list2):
            return levenshtein_distance(list2, list1)

        # now we know list1 is longer than list2
        if len(list2) == 0:
            return len(list1)

        #Enumerate both lists to count up deletions, substitutions, and insertions to make lists similar
        last_row = range(len(list2) + 1)
        for i, column1 in enumerate(list1):
            current_row = [i+1]
            for j, column2 in enumerate(list2):
                insertions = last_row[j+1] + 1
                deletions = current_row[j] + 1
                substitutions = last_row[i] + (column1 != column2)
                current_row.append(min(insertions, deletions, substitutions))

        return last_row[-1]

    def levenshtein_rating(self, list1, list2):
        return self.levenshtein_distance(list1, list2)/float(max(len(list1), len(list2)))

    def rate(self, list1, list2):
        #If the lists are identical, give a rating of 1
        if list1==list2:
            self.rating = 1
        #If the lists are not identical, score by the ratio of identical words (same word, same place in the list) to non-identical words
        else:
            #Use the average of various rating methods
            simple_rating = self.simple_word_by_word_rating(list1, list2)
            set_rating = self.set_rating(list1, list2)
            lev_rating = self.levenshtein_rating(list1, list2)
            if simple_rating == 0 and set_rating == 0:
                self.rating = 0
            else:
                self.rating = (simple_rating + set_rating + lev_rating) / 3.0

        #print(self.rating)
        return self.rating
