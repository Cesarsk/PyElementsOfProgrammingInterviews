from test_framework import generic_test
from test_framework.test_failure import TestFailure


# in a queue you insert in tail and remove from head
# in a circular queue it's the same but you need to move the pointer
# and if capacity is increased you need to resize the array

class Queue:

    def __init__(self, capacity: int) -> None:
        self.queue = [None] * capacity
        self.head = self.tail = self.length = 0
        return

    def enqueue(self, x: int) -> None:

        # if len is exceeded, needs resizing
        if self.length == len(self.queue):
            # recreate the queue starting from the head (which may not be in position 0)
            self.queue = self.queue[self.head:] + self.queue[:self.head]

            # resets head and tail
            self.head = 0
            self.tail = self.length  # tail points to the first none elements

            # add a new element to the list
            self.queue += [None]

        # insert in queue
        self.queue[self.tail] = x

        # reposition the tail

        self.tail = (self.tail + 1) % len(self.queue)
        self.length += 1

    def dequeue(self) -> int:
        if not self.length:
            raise Exception("empty queue")

        # reduce number of elements
        self.length -= 1

        # extract element from the queue
        elem = self.queue[self.head]

        # reposition head
        self.head = (self.head + 1) % len(self.queue)

        return elem

    def size(self) -> int:
        return self.length


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
