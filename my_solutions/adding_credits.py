import bintrees

from test_framework import generic_test
from test_framework.test_failure import TestFailure


# i.e. client_to_credit will be of the form:
#      { "Luca": 2, "Ana": 4 }
#      credit_to_client will be a BST
#      RBTree({-1: {'Thomas'}, 29: {'Larry'}, 70: {'Vincent'}})

class ClientsCreditsInfo:
    def __init__(self):
        self._increment = 0
        self._client_to_credit = {}  # a hash table for taking care of client: credit match
        self._credit_to_clients = bintrees.RBTree()  # a BST for taking care of credit: client match

    def insert(self, client_id: str, c: int) -> None:
        self.remove(client_id)
        self._client_to_credit[client_id] = c - self._increment
        # key: c-self._increment; value: client_id
        self._credit_to_clients.setdefault(c - self._increment, set()).add(client_id)

    def remove(self, client_id: str) -> bool:
        credit = self._client_to_credit.get(client_id)
        if credit is not None:
            # you need to remove from here
            # because there may be more client_id for a specific credit
            self._credit_to_clients[credit].remove(client_id)

            # if there's no value for that you can remove it from the BST
            if not self._credit_to_clients[credit]:
                del self._credit_to_clients[credit]

            # you can remove the client as well
            del self._client_to_credit[client_id]
            return True
        return False

    def lookup(self, client_id: str) -> int:
        # the hash table is easier for lookup operation
        credit = self._client_to_credit.get(client_id)
        return -1 if credit is None else credit + self._increment

    def add_all(self, C: int) -> None:
        self._increment += C

    def max(self) -> str:
        credits = self._credit_to_clients.max_item()[1]  # the value: the list of clients
        return next(iter(credits)) if credits else ''  # first element of the value which is the first client


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == 'add_all':
            cr.add_all(i_arg)
        elif op == 'lookup':
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('adding_credits.py',
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
