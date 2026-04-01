import yaml


def apply_sigma_rules(df, rule_path):
    with open(rule_path, "r") as file:
        rule = yaml.safe_load(file)

    detection_field = list(rule["detection"]["selection"].keys())[0]
    detection_value = rule["detection"]["selection"][detection_field]

    df = df.copy()

    df["sigma_alert"] = df[detection_field].apply(
        lambda x: "SIGMA_ALERT" if x == detection_value else "NONE"
    )

    return df
