import pytest


class TestApi:

    @pytest.mark.parametrize('args', ['王思聪', '王健林', '王俊豪'])
    def test_api(self, args):
        print(args)


if __name__ == '__main__':
    pytest.main(['test_api.py'])
