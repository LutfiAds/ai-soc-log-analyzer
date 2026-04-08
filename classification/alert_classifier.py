def classify_alerts(df):

    df = df.copy()

    def classify(row):

        if row.get("event") == "SUCCESS_LOGIN" and not row.get("trusted_network", True):
            return "SUSPICIOUS_SUCCESSFUL_LOGIN"

        if row.get("cross_host_attack", False):
            return "DISTRIBUTED_ATTACK"

        if row.get("bruteforce_alert") == "BRUTEFORCE":
            return "BRUTEFORCE_ATTACK"

        if row.get("sigma_alert") == "SIGMA_ALERT":
            return "FAILED_LOGIN_PATTERN"

        if row.get("anomaly") == "SUSPICIOUS":
            return "ANOMALOUS_LOGIN"

        return "INFO"

    df["alert_type"] = df.apply(classify, axis=1)

    return df
