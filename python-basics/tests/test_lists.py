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
