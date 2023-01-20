from types import MappingProxyType
from collections import namedtuple


id = namedtuple('username', 'username, password, token')

CLIENTS = MappingProxyType(
    {
        'Andrii': (
            id('Andrii', '123', '.....'),
        ),
        'Andrii_888': (
            id('Andrii_888', '123', '.....'),
        )
    }
)
