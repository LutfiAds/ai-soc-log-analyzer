# AI SOC Log Analyzer

AI-powered authentication monitoring detection engine inspired by modern SIEM pipelines.

This project analyzes Linux SSH authentication logs (`auth.log`) and detects suspicious login activity using a hybrid detection strategy combining anomaly detection, rule-based detection, correlation logic, and threat intelligence enrichment.

Designed as a detection engineering portfolio project simulating a lightweight SIEM authentication analytics preprocessing module.

---

# Features

## Core Detection Capabilities

- SSH failed login detection
- IsolationForest anomaly detection
- Sigma rule-based detection engine
- Brute-force correlation detection
- Hostname-aware log parsing
- Trusted subnet classification
- GeoIP country enrichment
- High-risk country detection
- Context-aware severity scoring
- Streamlit SOC-style dashboard

---

# Detection Pipeline Architecture

```
Log ingestion
    ↓
Parsing engine
    ↓
Hostname enrichment
    ↓
Trusted subnet awareness
    ↓
GeoIP enrichment
    ↓
High-risk country detection
    ↓
Anomaly detection (IsolationForest)
    ↓
Sigma rule detection
    ↓
Brute-force correlation engine
    ↓
Severity scoring engine
    ↓
Dashboard visualization
```

This pipeline mirrors authentication analytics workflows used in SIEM platforms such as Splunk, Elastic SIEM, and Wazuh.

---

# Example Detection Scenarios

### Failed SSH login

```
Failed password for root from 192.168.1.10
```

Result:

```
SIGMA_ALERT
Severity: LOW
```

---

### Brute-force detection

```
FAILED_LOGIN × 3
```

Result:

```
BRUTEFORCE_ALERT
Severity: CRITICAL
```

---

### Suspicious external login

```
Login attempt from unknown external IP
```

Result:

```
ANOMALY_DETECTED
Severity: HIGH
```

---

### High-risk country login

```
Login attempt from high-risk country
```

Result:

```
THREAT_INTEL_ALERT
Severity: HIGH
```

---

# Technology Stack

| Component | Purpose |
|----------|---------|
Python | Detection engine core |
Pandas | Structured log processing |
Scikit-learn | IsolationForest anomaly detection |
Sigma Rules | Rule-based detection |
GeoLite2 | GeoIP enrichment |
YAML | Detection configuration |
Streamlit | Dashboard visualization |

---

# Installation

Clone repository:

```
git clone https://github.com/LutfiAds/ai-soc-log-analyzer.git
cd ai-soc-log-analyzer
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Download GeoIP database:

```
./scripts/download_geoip.sh
```

Run dashboard:

```
streamlit run dashboard/app.py
```

---

# Project Structure

```
ai-soc-log-analyzer/
│
├── parser/
├── detection/
├── scoring/
├── dashboard/
├── config/
├── scripts/
│   └── download_geoip.sh
│
├── main.py
└── requirements.txt
```

---

# Detection Strategy

This system combines multiple detection layers:

### Anomaly Detection

Detects unusual authentication behavior:

```
IsolationForest
```

---

### Rule-Based Detection

Detects suspicious authentication events:

```
FAILED_LOGIN
ROOT_LOGIN
SUDO_EXECUTION
```

---

### Correlation Engine

Detects behavioral attack patterns:

```
FAILED_LOGIN × N
→ BRUTEFORCE ATTACK
```

---

### Context Enrichment

Reduces false positives using trusted subnet classification.

---

### Threat Intelligence Enrichment

Improves detection accuracy using:

```
GeoIP lookup
High-risk country classification
```

---

# Release History

| Version | Description |
|--------|-------------|
v0.1 | Initial anomaly + Sigma detection engine |
v0.2 | Context-aware detection with trusted subnet enrichment |
v0.3 | Threat intelligence enriched detection pipeline |

---

# Author

Detection engineering portfolio project by:

https://github.com/LutfiAds
