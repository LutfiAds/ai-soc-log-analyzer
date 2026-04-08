def classify_alerts(df):

    df = df.copy()

    def classify(row):

        # PRIORITAS 1: suspicious successful login (credential compromise indicator)
        if row.get("event") == "SUCCESS_LOGIN" and not row.get("trusted_network", True):
            return "SUSPICIOUS_SUCCESSFUL_LOGIN"

        # PRIORITAS 2: distributed brute-force campaign
        if row.get("cross_host_attack", False):
            return "DISTRIBUTED_ATTACK"

        # PRIORITAS 3: brute-force detection
        if row.get("bruteforce_alert") == "BRUTEFORCE":
            return "BRUTEFORCE_ATTACK"

        # PRIORITAS 4: sigma failed-login pattern
        if row.get("sigma_alert") == "SIGMA_ALERT":
            return "FAILED_LOGIN_PATTERN"

        # PRIORITAS 5: anomaly fallback
        if row.get("anomaly") == "SUSPICIOUS":
            return "ANOMALOUS_LOGIN"

        return "INFO"

    df["alert_type"] = df.apply(classify, axis=1)

    return df
