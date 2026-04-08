import json
import os
from datetime import datetime


def export_alerts_to_json(df, output_path="alerts/alerts.json"):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    alerts = df[df["risk_level"].isin(["HIGH", "CRITICAL"])].copy()

    if alerts.empty:
        print("[INFO] No high severity alerts to export.")
        return

    # convert timestamp ke string supaya JSON compatible
    alerts["timestamp"] = alerts["timestamp"].astype(str)

    alerts["export_timestamp"] = datetime.utcnow().isoformat()

    export_fields = [
        "timestamp",
        "hostname",
        "ip",
        "country",
        "alert_type",
        "mitre_attack_technique",
        "mitre_attack_tactic",
        "risk_level",
        "export_timestamp"
    ]

    alerts = alerts[export_fields]

    alerts_list = alerts.to_dict(orient="records")

    with open(output_path, "w") as f:
        json.dump(alerts_list, f, indent=4)

    print(f"[+] Alerts exported successfully → {output_path}")
