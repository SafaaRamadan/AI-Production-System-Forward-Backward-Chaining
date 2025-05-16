def read_rules(rules_file):
    rules = []
    content = rules_file.read().decode("utf-8")
    lines = content.strip().splitlines()

    for line in lines:
        if 'IF' not in line.upper() or 'THEN' not in line.upper():
            raise ValueError(f"Invalid rule: `{line}`. Rule must contain 'IF' and 'THEN'.")


        _, condition_and_conclusion = line.split('IF')
        condition_part, conclusion = condition_and_conclusion.split('THEN')
        conclusion = conclusion.strip()
        or_part = condition_part.split('OR')
        for or_cond in or_part:
                conditions = [c.strip() for c in or_cond.split('AND')]
                rules.append({'conditions': conditions, 'conclusion': conclusion})
    return rules


def read_facts(facts_file):
    content = facts_file.read().decode("utf-8")
    lines = content.strip().splitlines()

    for line in lines:
        if 'IF' in line.upper() or 'THEN' in line.upper():
            raise ValueError(f"Invalid fact: `{line}`. Facts must not contain 'IF' or 'THEN'.")

    return [line.strip() for line in lines]
