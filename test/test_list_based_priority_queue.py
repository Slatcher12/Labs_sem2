import unittest
from src.list_based_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_empty_queue(self):
        queue = PriorityQueue()
        assert queue.is_empty() is True
        assert queue.delete_from_queue() is None
        assert queue.returning_high_priority_element() is None

    def test_insertion_and_removal(self):
        queue = PriorityQueue()
        queue.insert_to_queue("number1", 1)
        queue.insert_to_queue("number2", 4)
        queue.insert_to_queue("number3", 6)

        assert queue.delete_from_queue() == "number3"
        assert queue.delete_from_queue() == "number2"
        assert queue.delete_from_queue() == "number1"

    def test_priority_queue(self):
        queue = PriorityQueue()
        queue.insert_to_queue("number1", 1)
        queue.insert_to_queue("number2", 4)
        queue.insert_to_queue("number3", 6)
        highest_priority_value = queue.returning_high_priority_element()
        assert highest_priority_value == "number3"
