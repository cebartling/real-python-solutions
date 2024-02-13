location = (6.51, 3.39, 'Lagos', 'Nigeria')
my_name = tuple('Christopher')


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


def test_create_tuple_from_tuple_function():
    assert type(my_name) == tuple
    assert len(my_name) == 11
    assert 'x' not in my_name
    assert len(my_name[1:]) == 10


def test_nested_tuples():
    data = ((1, 2), (3, 4))
    row = 1
    for datum in data:
        print(f'\nRow {row} sum: {sum(datum)}')
        row += 1


def test_nested_tuples_enumerate_function():
    data = ((1, 2), (3, 4))
    for row, datum in enumerate(data, start=1):
        print(f'\nRow {row} sum: {sum(datum)}')
