def equal_to(lhs, rhs, ops):
    operations = list(ops) + ['']
    expressions = [lhs]
    for idx in range(len(lhs) - 1, 0, -1):
        updated_expressions = []
        for expression in expressions:
            for operation in operations:
                updated_expressions.append(expression[0:idx] + operation + expression[idx:])
        expressions = updated_expressions
    ans = set()
    for expression in expressions:
        if eval(expression) == rhs:
            ans.add(expression + "=" + str(rhs))
    return ans
