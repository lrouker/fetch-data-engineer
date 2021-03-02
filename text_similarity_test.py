import pytest  
from text_similarity import RatingGenerator

def test_0_case():
    rg = RatingGenerator()
    assert rg.rate({"1"}, {"2"})==0