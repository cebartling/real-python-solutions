import random

nouns = ['badger', 'horse', 'aardvark', 'mouse', 'gorilla', 'elephant', 'eagle', 'sparrow']
verbs = ['hugs', 'bounces', 'meows', 'hauls', 'whispers', 'flutters', 'gallops', 'shimmers']
adjectives = ['furry', 'incredulous', 'fragrant', 'exuberant', 'glistening', 'melancholic', 'serene']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'graciously', 'reluctantly', 'meticulously', 'vigorously']


def test_poetry_generator():
    selected_nouns = [
        random.choice(nouns),
        random.choice(nouns),
        random.choice(nouns)
    ]
    selected_verbs = [
        random.choice(verbs),
        random.choice(verbs),
        random.choice(verbs)
    ]
    selected_adjectives = [
        random.choice(adjectives),
        random.choice(adjectives),
        random.choice(adjectives),
    ]
    selected_prepositions = [
        random.choice(prepositions),
        random.choice(prepositions)
    ]
    selected_adverbs = [
        random.choice(adverbs)
    ]
    article = 'A'
    if selected_adjectives[0].startswith(('a', 'e', 'i', 'o', 'u')):
        article = 'An'
    poetry = [
        f'\n\n{article} {selected_adjectives[0]} {selected_nouns[0]}',
        f'',
        f'{article} {selected_adjectives[0]} {selected_nouns[0]} {selected_verbs[0]} {selected_prepositions[0]} the {selected_adjectives[1]} {selected_nouns[1]}',
        f'{selected_adverbs[0]}, the {selected_nouns[0]} {selected_verbs[1]}',
        f'{selected_nouns[1]} {selected_verbs[2]} {selected_prepositions[1]} the {selected_adjectives[2]} {selected_nouns[2]}'
    ]
    print('\n'.join(poetry))
