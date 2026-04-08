import yaml


def apply_detection_rules(df, rules_path):

    df = df.copy()

    with open(rules_path, "r") as f:
        rules_config = yaml.safe_load(f)

    rules = rules_config.get("rules", [])

    df["rule_triggered"] = None
    df["rule_severity"] = None

    for rule in rules:

        rule_name = rule["name"]
        conditions = rule["conditions"]
        severity = rule["severity"]

        mask = True

        for column, expected_value in conditions.items():
            mask = mask & (df[column] == expected_value)

        df.loc[mask, "rule_triggered"] = rule_name
        df.loc[mask, "rule_severity"] = severity

    return df
