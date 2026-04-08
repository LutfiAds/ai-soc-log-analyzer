def map_mitre_techniques(df):

    df = df.copy()

    mitre_map = {
        "FAILED_LOGIN_PATTERN": {
            "technique": "T1110",
            "tactic": "Credential Access"
        },
        "BRUTEFORCE_ATTACK": {
            "technique": "T1110",
            "tactic": "Credential Access"
        },
        "DISTRIBUTED_ATTACK": {
            "technique": "T1110",
            "tactic": "Credential Access"
        },
        "ANOMALOUS_LOGIN": {
            "technique": "T1078",
            "tactic": "Persistence"
        },
        "SUSPICIOUS_SUCCESSFUL_LOGIN": {
            "technique": "T1078",
            "tactic": "Persistence"
        }
    }

    df["mitre_attack_technique"] = df["alert_type"].apply(
        lambda x: mitre_map.get(x, {}).get("technique", "UNKNOWN")
    )

    df["mitre_attack_tactic"] = df["alert_type"].apply(
        lambda x: mitre_map.get(x, {}).get("tactic", "UNKNOWN")
    )

    return df
