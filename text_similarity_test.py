import pytest  
from text_similarity import RatingGenerator

#Test for basic requirements of prompt, text which matches exactly has rating of 1, text which does not match at all has rating of 0
def test_0_case():
    rg = RatingGenerator()
    assert rg.rate(["1"], ["2"])==0

def test_1_case():
    rg = RatingGenerator()
    assert rg.rate(["string"], ["string"])==1