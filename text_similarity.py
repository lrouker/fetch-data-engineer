class RatingGenerator():
    def __init__(self, rating=0):
        self.rating = rating

    def rate(self, list1, list2):
        if list1==list2:
            self.rating = 1
        return self.rating