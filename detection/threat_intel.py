import yaml


def load_high_risk_countries(config_path):

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config["high_risk_countries"]


def apply_country_risk(df, config_path):

    high_risk = load_high_risk_countries(config_path)

    df = df.copy()

    df["high_risk_country"] = df["country"].apply(
        lambda x: x in high_risk
    )

    return df
