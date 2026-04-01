def detect_bruteforce(df, threshold=3):
    df = df.copy()

    ip_counts = df.groupby("ip").size()

    suspicious_ips = ip_counts[ip_counts >= threshold].index

    df["bruteforce_alert"] = df["ip"].apply(
        lambda x: "BRUTEFORCE" if x in suspicious_ips else "NONE"
    )

    return df
