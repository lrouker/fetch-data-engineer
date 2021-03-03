import pytest  
from text_similarity import RatingGenerator

#Test for basic requirements of prompt, text which matches exactly has rating of 1, text which does not match at all has rating of 0
def test_0_case():
    rg = RatingGenerator()
    assert rg.rate(["1"], ["2"]) == 0

def test_unordered_0_list():
    rg = RatingGenerator()
    rating = rg.rate(["string1", "string2"], ["string3", "string"])
    assert rating == 0

def test_1_case():
    rg = RatingGenerator()
    assert rg.rate(["string"], ["string"]) == 1

#Test for intermediate case, the algorithm should return a value between 1 and 0 when the lists are not identical but have some matching
def test_inbetween_case():
    rg = RatingGenerator()
    rating = rg.rate(["string", "A"], ["string", "B"])
    assert rating < 1
    assert rating > 0

def test_unordered_identical_list():
    rg = RatingGenerator()
    rating = rg.rate(["string", "string2"], ["string2", "string"])
    assert rating < 1
    assert rating > 0

def test_unordered_similar_list():
    rg = RatingGenerator()
    rating = rg.rate(["string", "string3"], ["string2", "string"])
    assert rating < 1
    assert rating > 0