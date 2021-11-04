from datetime import timedelta

import pytest

from module import compute_duration


TEST_DATA = [
    ([], timedelta()),
    ([timedelta(seconds=2.345)],
     timedelta(seconds=2.345)
     ),
    ([timedelta(seconds=1.300), timedelta(seconds=2.700)],
     timedelta(seconds=4)
     )
]


@pytest.mark.parametrize("args,result", TEST_DATA)
def test_compute_durations(args, result):
    assert compute_duration(*args) == result


if __name__ == '__main__':
    pytest.main()
