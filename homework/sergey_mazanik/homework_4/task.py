my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['a', 'b', 'c', 'd', 'e'],
    'dict': {'one': 1.0, 'two': 2.0, 'three': 3.0, 'four': 4.0, 'five': 5.0},
    'set': {None, True, False, 'set', '10'}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('f')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 6.0
del my_dict['dict']['one']
my_dict['set'].add('new')
my_dict['set'].discard(None)
print(my_dict)
