from mlproject.distance import haversine

def test_lenght():
    assert haversine(1,2,3,4)>0
