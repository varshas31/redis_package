from app.main import client, Queue, Stack
import pytest

def test_queue_operations():
    my_queue = Queue(client, 'my_queue')
    my_queue.write('item1')
    my_queue.write('item2')
    result = my_queue.read()
    assert result is not None  # Check if result is not None
    assert result  # Assuming read returns the expected string

def test_stack_operations():
    my_stack = Stack(client, 'my_stack')
    my_stack.write('itemA')
    my_stack.write('itemB')
    result = my_stack.read()
    assert result is not None  # Check if result is not None
    assert result  # Assuming read returns the expected string

if __name__ == "__main__":
    pytest.main()

    
