import types


def flat_generator(list_of_lists):
    cursor = 0
    main_cursor = 0
    while len(list_of_lists) > main_cursor:
        if len(list_of_lists[main_cursor]) > cursor:
            yield list_of_lists[main_cursor][cursor]
            cursor += 1
        elif len(list_of_lists[main_cursor]) == cursor:
            main_cursor += 1
            cursor = 0
        else:
            break


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
