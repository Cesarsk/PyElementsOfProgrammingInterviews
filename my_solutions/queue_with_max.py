from test_framework import generic_test
from test_framework.test_failure import TestFailure


class SimpleQueueWithMax:
    elements = []

    def enqueue(self, x: int) -> None:
        self.elements.append(x)

    def dequeue(self) -> int:
        return self.elements.pop(0)

    def max(self) -> int:
        return max(self.elements)


# improved version: it basically uses the concept of "dominated element" to keep a sorted queue of max elements
# when inserting new elements in the queue
class QueueWithMax:
    elements = []
    max_elements = []

    def enqueue(self, x: int) -> None:
        self.elements.append(x)

        # when we put an element into the queue, clean all the elements smaller than said element x from max_elems
        while self.max_elements and self.max_elements[-1] < x:
            self.max_elements.pop()

        self.max_elements.append(x)

    def dequeue(self) -> int:
        if self.elements:
            result = self.elements.pop(0)
            if result == self.max_elements[0]:
                self.max_elements.pop(0)
            return result

        raise Exception("empty queue")

    def max(self) -> int:
        # since it's sorted, returning the first element means returning the maximum
        if self.max_elements:
            return self.max_elements[0]

        return Exception("empty queue")


def queue_tester(ops):
    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
