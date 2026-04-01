from parser.log_parser import parse_auth_log
from detection.anomaly_detector import detect_anomalies
from scoring.risk_score import assign_risk_score
from detection.sigma_rules_engine import apply_sigma_rules
from detection.bruteforce_detector import detect_bruteforce

df = parse_auth_log("data/auth.log")

df = detect_anomalies(df)

df = assign_risk_score(df)

df = apply_sigma_rules(df, "config/multiple_failed_login.yaml")

df = detect_bruteforce(df)

print(df)
