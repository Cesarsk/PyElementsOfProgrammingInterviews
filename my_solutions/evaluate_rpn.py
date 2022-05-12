from test_framework import generic_test


def evaluate(expression: str) -> int:
    partial_results = []
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y),
    }

    for token in expression.split(','):
        if token in operators:
            partial_results.append(
                operators[token](
                    partial_results.pop(), partial_results.pop()
                )
            )
        else:
            partial_results.append(int(token))

    return partial_results.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
