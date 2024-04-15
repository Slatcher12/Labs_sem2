class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None
        self.prev = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_to_queue(self, value, priority):
        new_node = Node(value, priority)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            if priority > self.head.priority:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next is not None and priority <= current_node.next.priority:
                    current_node = current_node.next

                if current_node.next is None:
                    new_node.prev = current_node
                    current_node.next = new_node
                    self.tail = new_node
                else:
                    new_node.prev = current_node
                    new_node.next = current_node.next
                    current_node.next.prev = new_node
                    current_node.next = new_node

    def delete_from_queue(self):
        if self.is_empty():
            return None

        deleted_from_queue_node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        return deleted_from_queue_node.value

    def returning_high_priority_element(self):
        if self.is_empty():
            return None

        return self.head.value

    def queue_without_changes(self):
        elem = self.head
        while elem:
            print(elem.priority)
            elem = elem.next

    def queue_tail_to_head(self):
        elem = self.tail
        while elem:
            print(elem.priority)
            elem = elem.prev

