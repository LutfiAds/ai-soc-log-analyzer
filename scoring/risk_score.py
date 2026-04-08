def assign_risk_score(df):

    df = df.copy()

    if "cross_host_attack" not in df.columns:
        df["cross_host_attack"] = False

    if "bruteforce_alert" not in df.columns:
        df["bruteforce_alert"] = "NONE"

    if "trusted_network" not in df.columns:
        df["trusted_network"] = False

    if "high_risk_country" not in df.columns:
        df["high_risk_country"] = False

    def score(row):

        if row["cross_host_attack"]:
            return "CRITICAL"

        if row["bruteforce_alert"] == "BRUTEFORCE":
            return "CRITICAL"

        if row["high_risk_country"]:
            return "HIGH"

        if row.get("event") == "SUCCESS_LOGIN" and not row.get("trusted_network", True):
            return "SUSPICIOUS_SUCCESSFUL_LOGIN"

        if row["anomaly"] == "SUSPICIOUS" and not row["trusted_network"]:
            return "HIGH"

        if row["anomaly"] == "SUSPICIOUS":
            return "MEDIUM"

        return "LOW"

    df["risk_level"] = df.apply(score, axis=1)

    return df
