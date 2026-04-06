import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from parser.log_parser import parse_auth_log
from detection.network_context import apply_network_context
from detection.anomaly_detector import detect_anomalies
from detection.sigma_rules_engine import apply_sigma_rules
from detection.bruteforce_detector import detect_bruteforce
from detection.geoip_enrichment import enrich_geoip
from detection.threat_intel import apply_country_risk
from scoring.risk_score import assign_risk_score

st.title("AI SOC Log Analyzer Dashboard")

df = parse_auth_log("data/auth.log")

df = apply_network_context(
    df,
    "config/trusted_networks.yaml"
)

df = enrich_geoip(
    df,
    "config/GeoLite2-City.mmdb"
)

df = apply_country_risk(
    df,
    "config/high_risk_countries.yaml"
)

df = detect_anomalies(df)

df = apply_sigma_rules(
    df,
    "config/multiple_failed_login.yaml"
)

df = detect_bruteforce(df)

df = assign_risk_score(df)

st.subheader("All Events")
st.dataframe(df)


st.subheader("Suspicious Events Only")

suspicious_df = df[df["risk_level"] == "HIGH"]

st.dataframe(suspicious_df)


st.subheader("Risk Level Summary")
st.bar_chart(df["risk_level"].value_counts())
