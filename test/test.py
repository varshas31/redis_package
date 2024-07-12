from redis.main import client, Queue, Stack, Delete
import pytest

def test_queue_operations():
    my_queue = Queue(client, 'my_queue')
    my_queue.write('item1')
    my_queue.write('item2')
    assert my_queue.read().decode() == 'item1'  # Assuming read returns bytes, decode to string

def test_stack_operations():
    my_stack = Stack(client, 'my_stack')
    my_stack.write('itemA')
    my_stack.write('itemB')
    assert my_stack.read().decode() == 'itemB'  # Assuming read returns bytes, decode to string

def test_delete_operation():
    delete_operation = Delete(client, 'my_queue')
    assert delete_operation.delete() is True

if __name__ == "__main__":
    pytest.main()
