# Third-party imports
import pytest

# Local imports
from dspy.linked_list.error import ListIndexOutOfRange
from dspy.linked_list.fixtures.singly import singly_empty, singly_nonempty


def test_prepend_empty_list(singly_empty):
    """Test Singly.prepend on an empty list."""
    singly = singly_empty
    singly.prepend(1)
    assert singly._head
    assert singly._head.data == 1
    assert not singly._head.next


def test_prepend_nonempty_list(singly_nonempty):
    """Test Singly.prepend on a nonempty list."""
    # Linked list with three nodes 1 -> 2 -> 3
    singly = singly_nonempty
    singly.prepend(0)
    assert singly._head
    assert singly._head.next
    assert singly._head.data == 0


def test_insert_empty_list(singly_empty):
    """Test insertion of a node to the head of an empty list."""
    singly = singly_empty
    singly.insert(4, 0)
    assert singly._head
    assert singly._head.data == 4
    assert not singly._head.next


def test_insert_empty_list_out_of_range(singly_empty):
    """Test insertion of a node to a list index that is out of range."""
    singly = singly_empty
    with pytest.raises(ListIndexOutOfRange) as e:
        singly.insert(1, 1)


@pytest.mark.parametrize("index", [0, 1, 2, 3])
def test_insert_nonempty_list(index, singly_nonempty):
    """Test insertion of a node into a nonempty list as the head."""
    singly = singly_nonempty
    singly.insert(13, index)
    node = singly._head

    # Find where the node was inserted
    while index:
        node = node.next
        index -= 1

    assert node
    assert node.data == 13


def test_insert_nonempty_list_out_of_range(singly_nonempty):
    """Test insertion of a node to a list index that is out of range."""
    singly = singly_nonempty
    with pytest.raises(ListIndexOutOfRange) as e:
        singly.insert(4, 4)
        print(singly)


def test_append_empty_list(singly_empty):
    """Test Singly.append on an empty list"""
    singly = singly_empty
    singly.append(1)
    assert singly._head
    assert singly._head.data == 1
    assert not singly._head.next


def test_append_nonempty_list(singly_nonempty):
    """Test Singly.append on a nonempty list"""
    # Linked list with three nodes 1 -> 2 -> 3
    singly = singly_nonempty
    singly.append(4)
    last = singly._head.next.next.next
    assert last
    assert not last.next
    assert last.data == 4


def test_delete_first_node(singly_nonempty):
    """Test Singly.delete(0)."""
    singly = singly_nonempty
    singly.delete(0)
    assert singly._head
    assert singly._head.next
    assert singly._head.data == 2


def test_delete_middle_node(singly_nonempty):
    """Test Singly.delete(1)."""
    singly = singly_nonempty
    singly.delete(1)
    assert singly._head
    assert singly._head.next
    assert singly._head.data == 1
    assert singly._head.next.data == 3


def test_delete_last_node(singly_nonempty):
    """Test Singly.delete(2)."""
    singly = singly_nonempty
    singly.delete(2)
    assert singly._head
    assert singly._head.next
    assert singly._head.data == 1
    assert singly._head.next.data == 2
    assert not singly._head.next.next


def test_delete_all_nodes(singly_nonempty):
    """Sequentially delete every node of the list."""
    # 1 -> 2 -> 3 -> None
    singly = singly_nonempty
    singly.delete(0)

    # Expecting 2 -> 3 -> None
    assert singly._head
    assert singly._head.next
    assert singly._head.data == 2
    assert singly._head.next.data == 3
    assert not singly._head.next.next

    singly.delete(0)

    # Expecting 3 -> None
    assert singly._head
    assert singly._head.data == 3
    assert not singly._head.next

    singly.delete(0)

    # Expecting None
    assert not singly._head