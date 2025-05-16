def backward(rules, facts, goal, trace=None, depth=0):
    if trace is None:
        trace = []

    indent = "  *" * depth
    trace.append(f"{indent}Checking goal: {goal}")

    if goal in facts:
        trace.append(f"{indent}✅ Goal '{goal}' is a known fact.")
        return True, trace

    for rule in rules:
        if rule['conclusion'] == goal:
            trace.append(f"{indent}Trying rule: IF {rule['conditions']} THEN {rule['conclusion']}")
            all_conditions_met = True

            for cond in rule['conditions']:
                if any(op in cond for op in ['=', '<', '>']):
                    cond_left, op, cond_right = split(cond)
                    matched = False

                    for fact in facts:
                        fact_left, fact_op, fact_right = split(fact)
                        if fact_left == cond_left:
                            try:
                                v1, v2 = float(fact_right), float(cond_right)
                                if op == '=' and v1 == v2:
                                    matched = True
                                elif op == '<' and v1 < v2:
                                    matched = True
                                elif op == '>' and v1 > v2:
                                    matched = True
                            except:
                                matched = False
                            break

                    if not matched:
                        all_conditions_met = False
                        break
                else:
                    result, trace = backward(rules, facts, cond, trace, depth + 1)
                    if not result:
                        all_conditions_met = False
                        break

            if all_conditions_met:
                trace.append(f"{indent}✅ Goal '{goal}' can be concluded by rule.")
                facts.append(goal)
                return True, trace

    trace.append(f"{indent}❌ Goal '{goal}' cannot be concluded.")
    return False, trace


def split(condition):
    for op in ['=', '<', '>']:
        if op in condition:
            left, right = condition.split(op)
            return left.strip(), op, right.strip()
    return condition, None, None
