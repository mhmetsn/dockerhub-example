import pytest
from service.views import app
from service.formater import SUPPORTED


class Test_Flask_Views:
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which usually contains tests)."""
        app.config['TESTING'] = True    # Flask has a built in function/configuration to perform tests
        cls.app = app.test_client()     # Function needed to start executing the tests

    @pytest.fixture
    def data_expected(self):
        return b'{ "name":"Jose", "msg":"welcome to your first page!"}'    # Args by URL received like bytes, so we transform string to bytes with the b

    def test_output(self, data_expected):
        rv = self.app.get('/?output=json')  # Method to obtain what an UrL returns
        assert rv.data == data_expected,'Index view fails to convert data to json'   # It returns an object, the data is the method data

    def test_outputs(self):
        rv = self.app.get('/outputs')
        r = rv.data.decode('utf-8')        # Arg received as bytes, decode to obtain string
        r = r.replace(' ',"")              # Unnecessary blank spaces
        r = r.split(',')                   # Obtaining the list of args

        assert r == SUPPORTED

    def test_form(self):
        rv = self.app.get('/name=Lucas,msg=Welcome,output=plain_uppercase')
        r = rv.data.decode('utf-8')       # Arg received as bytes, decode to obtain string
        # TODO HINT for the assignment 2:
        # if you need to get a number, after decoding to utf-8 you will need to cast it to float or int
        # Example: r = int(rv.data.decode('utf-8')). But only in case that you need it
        assert r == 'LUCAS WELCOME'
        
    def test_mult(self,data_expected):
        rv = self.app.get('http://127.0.0.1:5000/plainx2')
        r = rv.data.decode('utf-8')
        assert r == 'Jose welcome to your first page!'*2
