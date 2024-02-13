def test_list_creation():
    food = ['rice', 'beans']
    assert type(food) == list


def test_list_append():
    food = ['rice', 'beans']
    assert len(food) == 2
    food.append('broccoli')
    assert len(food) == 3


def test_list_extend():
    food = ['rice', 'beans']
    assert len(food) == 2
    food.extend(['bread', 'pizza'])
    assert len(food) == 4


def test_list_slicing():
    food = ['rice', 'beans', 'broccoli', 'bread', 'pizza']
    subset_food = food[:2]
    assert len(subset_food) == 2
    assert subset_food[0] == food[0]
    assert subset_food[1] == food[1]


def test_list_indexing():
    food = ['rice', 'beans', 'broccoli', 'bread', 'pizza']
    assert food[-1] == 'pizza'
    assert food[0] == 'rice'


def test_list_string_splitting():
    breakfast = "eggs, fruit, orange juice".split(', ')
    assert len(breakfast) == 3
    lengths = [len(x) for x in breakfast]
    assert lengths[0] == 4
    assert lengths[1] == 5
    assert lengths[2] == 12
