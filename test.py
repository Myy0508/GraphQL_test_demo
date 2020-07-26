import unittest
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

sample_transport=RequestsHTTPTransport(
    url='http://localhost:8000/graphql',
    verify=False,
    retries=3,
)

client = Client(
    transport=sample_transport,
    fetch_schema_from_transport=True,
)

query = gql('''
    query getContinents {
        hello,
        person{
            age
        }
    }
''')

class WeatherTest(unittest.TestCase):
    def setUp(self):
       pass

    def test_weather_changsha(self):
        result = client.execute(query)
        self.assertEqual(result,{'hello': 'hello world Brian!', 'person': {'age': 8}})


