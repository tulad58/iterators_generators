class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count = -1
        self.flat_list = []


    def __iter__(self):
        return self

    def __next__(self):
        self.flat_list = [element for sublist in self.list_of_list for element in sublist]
        self.count += 1
        if self.count >= len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.count]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()