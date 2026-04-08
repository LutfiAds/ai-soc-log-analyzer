import yaml


def apply_ip_reputation(df, feed_path):

    df = df.copy()

    with open(feed_path, "r") as f:
        feed = yaml.safe_load(f)

    malicious_ips = set(feed.get("malicious_ips", []))
    suspicious_ips = set(feed.get("suspicious_ips", []))

    def classify(ip):

        if ip in malicious_ips:
            return "MALICIOUS"

        if ip in suspicious_ips:
            return "SUSPICIOUS"

        return "UNKNOWN"

    df["ip_reputation"] = df["ip"].apply(classify)

    return df
