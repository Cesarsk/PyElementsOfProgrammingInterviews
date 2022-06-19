import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))

# TODO repeat this exercise
def group_by_age(people: List[Person]) -> None:
    people = [Person(29, "Luca"), Person(26, "Ana"), Person(29, "Rosa"), Person(27, "Carlo"), Person(27, "Bea")]

    age_to_count = collections.Counter(p.age for p in people)
    age_to_offset, offset = {}, 0

    # i.e. {luca:29, max:29, ana:27, eli:21, gian:29}
    # age_to_count  = {29:3, 27:1, 21:1}
    # age_to_offset = {29:0,27:3,21:4}
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        # will return always the same value unless we delete it
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]

        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]

        # switch elements from_idx and to_idx
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        # use age_to_count to check whether we finished with a particular age
        age_to_count[to_age] -= 1

        if age_to_count[to_age]:
            # age_to_offset = {29:0->1,27:3,21:4}
            age_to_offset[to_age] = to_idx + 1
        else:
            # delete so we go to the next element to evaluate
            del age_to_offset[to_age]

    print(people)
    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
