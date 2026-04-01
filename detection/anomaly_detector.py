from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    df = df.copy()

    df["ip_numeric"] = df["ip"].apply(
        lambda x: int(x.replace(".", ""))
    )

    model = IsolationForest(contamination=0.2, random_state=42)

    df["anomaly"] = model.fit_predict(df[["ip_numeric"]])

    df["anomaly"] = df["anomaly"].map(
        {1: "NORMAL", -1: "SUSPICIOUS"}
    )

    return df
