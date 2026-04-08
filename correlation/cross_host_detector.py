import pandas as pd


def detect_cross_host_attack(df, host_threshold=2):

    df = df.copy()

    host_counts = df.groupby("ip")["hostname"].nunique()

    suspicious_ips = host_counts[host_counts >= host_threshold].index

    df["cross_host_attack"] = df["ip"].apply(
        lambda x: x in suspicious_ips
    )

    return df
