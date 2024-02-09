location = (6.51, 3.39, 'Lagos', 'Nigeria')


def test_tuples():
    assert type(location) == tuple
    assert len(location) == 4
    assert location[0] == 6.51
    assert location[1] == 3.39
    assert location[2] == 'Lagos'
    assert location[3] == 'Nigeria'


def test_tuple_unpacking():
    latitude, longitude, city, country = location
    assert latitude == 6.51
    assert longitude == 3.39
    assert city == 'Lagos'
    assert country == 'Nigeria'
