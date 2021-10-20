
import pytest
from balancer import server_balancer


def test_balancer():
    tasks_time = 4
    max_users = 2
    new_users = [1, 3, 0, 1, 0, 1]

    output = server_balancer(tasks_time, max_users, new_users)

    expected_value = [
        [1], [2, 2], [2, 2], [2, 2, 1], [1, 2, 1], [2], [2], [1], [1], [0]
    ]

    assert output == expected_value


def test_balancer_lower_task_time():
    """
    New out tot servers
    5   0   5   4,1
    2   0   7   4,3
    0   5   2   2
    3   2   3   3
    -   0   3   3
    -   3   0   3
    -   0   0   0
    """
    tasks_time = 2
    max_users = 4
    new_users = [5, 2, 0, 3]

    output = server_balancer(tasks_time, max_users, new_users)

    expected_value = [[4, 1], [4, 3], [2], [3], [3], [3], [0]]

    assert output == expected_value


def test_balancer_ten_ten():
    """
    New out tot servers
    1   0   1   1
    11  0   12  10, 2
    1   0   13  10, 3
    3   0   16  10, 6
    -   0   16  10, 6
    -   0   16  10, 6
    -   0   16  10, 6
    -   0   16  10, 6
    -   0   16  10, 6
    -   0   16  10, 6
    -   1   15  9, 6
    -   11  4   4
    -   1   3   3
    -   3   0   0
    """
    tasks_time = 10
    max_users = 10
    new_users = [1, 11, 1, 3]

    output = server_balancer(tasks_time, max_users, new_users)

    expected_value = [
        [1], [10, 2], [10, 3], [10, 6], [10, 6], [10, 6], [10, 6], [10, 6],
        [10, 6], [10, 6], [9, 6], [4], [3], [0]
    ]

    assert output == expected_value


def test_balancer_one_one():
    """
    New out tot servers
    1   0   1   1
    1   1   1   1
    1   1   1   1
    1   1   1   1
    1   1   1   1
    1   1   1   1
    -   1   0   0
    -   0
    """
    tasks_time = 1
    max_users = 1
    new_users = [1, 1, 1, 1, 1, 1]

    output = server_balancer(tasks_time, max_users, new_users)

    expected_value = [[1], [1], [1], [1], [1], [1]]

    assert output == expected_value


def test_balancer_one_user():
    tasks_time = 3
    max_users = 2
    new_users = [1]

    output = server_balancer(tasks_time, max_users, new_users)

    expected_value = [[1], [1], [1], [0]]

    assert output == expected_value


def test_max_timer():
    tasks_time = 11
    max_users = 2
    new_users = [1, 3, 0, 1, 0, 1]

    with pytest.raises as error:
        server_balancer(tasks_time, max_users, new_users)
        assert error.args[0] == 'Value error'


def test_max_users():
    tasks_time = 2
    max_users = 11
    new_users = [1, 3, 0, 1, 0, 1]

    with pytest.raises as error:
        server_balancer(tasks_time, max_users, new_users)
        assert error.args[0] == 'Value error'


def test_zero_timer():
    tasks_time = 0
    max_users = 2
    new_users = [1, 3, 0, 1, 0, 1]

    with pytest.raises as error:
        server_balancer(tasks_time, max_users, new_users)
        assert error.args[0] == 'Value error'


def test_zero_users():
    tasks_time = 2
    max_users = 0
    new_users = [1, 3, 0, 1, 0, 1]

    with pytest.raises as error:
        server_balancer(tasks_time, max_users, new_users)
        assert error.args[0] == 'Value error'
