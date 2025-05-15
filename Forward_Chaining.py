def read_rules():
    rules = []
    with open("rules.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if 'IF' in line and 'THEN' in line:
                _, condition_and_conclusion = line.split('IF')
                condition_part, conclusion = condition_and_conclusion.split('THEN')
                conclusion = conclusion.strip()
                or_part = condition_part.split('OR')
                for or_cond in or_part:
                    conditions = [c.strip() for c in or_cond.split('AND')]
                    rules.append({'conditions': conditions, 'conclusion': conclusion})
    return rules


def read_facts():
    with open("facts.txt", 'r') as file:
        return [line.strip() for line in file]


def forward(rules, facts, goal=None):
    known_facts = set(facts)
    new_fact = True
    cycle = 1
    while new_fact:
        print(f"\nCycle {cycle}: {known_facts}")
        new_fact = False

        for rule in rules:
            for cond in rule['conditions']:
                matched = False

                if any(op in cond for op in ['=', '<', '>']):
                    cond_left, operator, cond_right = split(cond)

                    for fact in known_facts:
                        fact_left, fact_operator, fact_right = split(fact)

                        if fact_left == cond_left:
                                value1 = float(fact_right)
                                value2 = float(cond_right)
                                if operator == '=' and fact_operator == '=' and value1 == value2:
                                    matched = True
                                elif operator == '<' and value1 < value2:
                                    matched = True
                                elif operator == '>' and value1 > value2:
                                    matched = True
                                break
                else:
                    if cond in known_facts:
                        matched = True

                if not matched:
                    break
            else:
                # add to facts after checking all conditions
                if rule['conclusion'] not in known_facts:
                    print(f"-> New Fact: {rule['conclusion']}")
                    known_facts.add(rule['conclusion'])
                    new_fact = True

                    if goal and rule['conclusion'] == goal:
                        print(f"\n✅ Goal '{goal}' reached!")
                        return known_facts

        cycle += 1

    print(f"\nFinal Facts: {sorted(known_facts)}")
    if goal and goal not in known_facts:
        print(f"\n❌ Goal '{goal}' not reached.")


    return known_facts



def split(condition):
    for op in ['=', '<', '>']:
        if op in condition:
            left, right = condition.split(op)
            return left.strip(), op, right.strip()
    return condition, None, None




goal = "citrus_fruit"
f =  forward(read_rules(), read_facts(), goal)
