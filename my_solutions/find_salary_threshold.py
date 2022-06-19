from typing import List

from test_framework import generic_test


# i.e.
# Target: 210
# current_salaries:                                     [20,30,40,90,100]
# current_salary * number of people on the right        [20*5, 30*4+20, 40*3+20+30, 90*2+20+30+40, 100*1+20+30+40+90]
#                   the above condition is important to evaluate how many people will have adjusted_salaries
# result will be (210 - (20+30+40)) / 2

def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()  # increasing order

    unadjusted_salary_sum = 0.0

    for i, current_salary in enumerate(current_salaries):
        # the people that will change salary
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people

        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people

        unadjusted_salary_sum += current_salary

    return -1  # error: no solution


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
