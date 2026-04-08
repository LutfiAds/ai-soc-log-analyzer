import json
import os
from datetime import datetime


def export_alerts_to_json(df, output_path="alerts/alerts.json"):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    alerts = df[df["risk_level"].isin(["HIGH", "CRITICAL"])].copy()

    if alerts.empty:
        print("[INFO] No high severity alerts to export.")
        return

    alerts["@timestamp"] = alerts["timestamp"].astype(str)

    alerts["event.category"] = "authentication"

    alerts["event.outcome"] = alerts["event"].apply(
        lambda x: "success" if x == "SUCCESS_LOGIN" else "failure"
    )

    alerts["host.name"] = alerts["hostname"]

    alerts["source.ip"] = alerts["ip"]

    alerts["event.severity"] = alerts["risk_level"]

    alerts["threat.technique.id"] = alerts["mitre_attack_technique"]

    alerts["threat.tactic.name"] = alerts["mitre_attack_tactic"]

    alerts["event.created"] = datetime.utcnow().isoformat()

    export_fields = [
        "@timestamp",
        "event.category",
        "event.outcome",
        "host.name",
        "source.ip",
        "ip_reputation",
        "alert_type",
        "threat.technique.id",
        "threat.tactic.name",
        "event.severity",
        "event.created"
    ]

    alerts = alerts[export_fields]

    alerts_list = alerts.to_dict(orient="records")

    with open(output_path, "w") as f:
        json.dump(alerts_list, f, indent=4)

    print(f"[+] ECS alerts exported → {output_path}")
