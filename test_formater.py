from service.formater import plain_text_upper_case, plain_text, get_formatted
from pytest import fixture
import pytest


class Test_Formater:
    # content of test_module.py
    @pytest.fixture
    def name(self):
        return 'Jose'

    @pytest.fixture
    def msg(self):
        return 'message'

    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEeMSG")
        name = r.split(" ")[0]  # Splitting the string to check if both variables
        msg = r.split(" ")[1]  # has been converted properly to upper case
        assert (name.isupper() and msg.isupper), f' Failing to convert to upper case the variable name with the value {name} or the variable msg with the value {msg}'

    def test_plain_text(self, name, msg):  # Passing the variables name and msg as a fixture of pytest,
        r = plain_text(msg, name)  # so we need to call them with the same name as the function is defined
        assert (r == 'Jose message'), f' Failing to display plain text with the values {name} or the variable msg with the value {msg}'

    def test_get_formatted(self, name, msg):
        r = get_formatted(msg, name, "plain_uppercase")
        assert (r == 'JOSE MESSAGE'), f' Failing to convert to upper case the variable name with the value {name} or the variable msg with the value {msg}'