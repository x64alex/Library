class Client:

    def __init__(self, client_id, name):
        """
        Create a new Client

        :param client_id:
        :param name:
        """
        self._client_id = client_id
        self._name = name

    @property
    def id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return 'Client Id: ' + str(self._client_id) + ' Name: ' + self._name


def test_client():
    client = Client(1, '312')
    # print(client)
    assert client.id == 1
    assert client.name == '312'
    client.name = '31'
    assert client.name == '31'
    assert str(client) == 'Client Id: 1 Name: 31'


test_client()
