# Third-party imports
import pytest

# Loca imports
from ds_module.linked_list.singly import Singly, SinglyNode


@pytest.fixture(scope='function')
def singly_empty():
    """Initialize an empty singly linked list for testing."""
    singly = Singly()
    yield singly


@pytest.fixture(scope='function')
def singly_nonempty():
    """Initialize a nonempty singly linked list for testing."""
    singly = Singly()

    node3 = SinglyNode(data=3, next=None)
    node2 = SinglyNode(data=2, next=node3)
    node1 = SinglyNode(data=1, next=node2)

    singly._head = node1

    yield singly
