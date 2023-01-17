def sort_array(arr: list[int | float]) -> list[int | float] | None:
    """Sort by selection in ascending order"""

    if len(arr) < 2:
        return None
    if arr[0] > arr[1]:
        max_1, max_2 = arr[0], arr[1]
    else:
        max_1, max_2 = arr[1], arr[0]
    index = 2
    while max_1 == max_2 and index < len(arr):
        if max_1 > arr[index]:
            max_2 = arr[index]
        elif max_1 < arr[index]:
            max_1 = arr[index]
        index += 1
    if max_1 == max_2:
        return None

    for index_1 in range(len(arr)):
        k: int = index_1
        if arr[k] % 2 == 0:
            continue
        for index_2 in range(index_1, len(arr)):
            if arr[index_2] % 2 != 0 and arr[index_2] < arr[index_1]:
                k = index_2
        arr[index_1], arr[k] = arr[k], arr[index_1]

    return arr


def test_sort_array():
    result = sort_array([111, 111])
    assert result is None, f'Wrong answer: {result}'

    result = sort_array([1])
    assert result is None, f'Wrong answer: {result}'

    result = sort_array([])
    assert result is None, f'Wrong answer: {result}'

    result = sort_array([50, 50, 50, 50])
    assert result is None, f'Wrong answer: {result}'

    result = sort_array([3, 1])
    assert result == ([1, 3]), f'Wrong answer: {result}'

    result = sort_array([3, 2, -1, 4])
    assert result == [-1, 2, 3, 4], f'Wrong answer: {result}'

    result = sort_array([5, 3, 2, 8, 1, 4])
    assert result == [1, 3, 2, 8, 5, 4], f'Wrong answer: {result}'

    print('All assert_tests passed!')


if __name__ == '__main__':
    test_sort_array()
