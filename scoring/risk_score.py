def assign_risk_score(df):
    df = df.copy()

    def score(row):
        if row["anomaly"] == "SUSPICIOUS":
            return "HIGH"
        else:
            return "LOW"

    df["risk_level"] = df.apply(score, axis=1)

    return df
