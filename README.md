# AI SOC Log Analyzer

AI-powered security log analyzer for Linux authentication monitoring.

This project implements a lightweight hybrid detection pipeline inspired by modern SIEM architectures. It analyzes SSH authentication logs (`auth.log`) and detects suspicious behavior using anomaly detection, rule-based detection (Sigma), correlation logic, and severity scoring.

Designed as a detection-engineering portfolio project and prototype SOC authentication monitoring module.

---

# Features

- Log parsing for Linux SSH authentication events
- Anomaly detection using IsolationForest
- Sigma rule-based detection engine
- Brute-force correlation detection logic
- Severity scoring system (LOW / HIGH)
- Streamlit dashboard visualization
- Modular detection pipeline architecture

---

# Detection Pipeline Architecture

```
Log ingestion
    ↓
Parsing engine
    ↓
Structured dataframe (pandas)
    ↓
Anomaly detection (IsolationForest)
    ↓
Sigma rule detection
    ↓
Correlation engine (bruteforce detection)
    ↓
Risk scoring engine
    ↓
Dashboard visualization
```

This architecture mirrors the detection workflow used in modern SIEM platforms.

---

# Example Detection Capabilities

### Failed SSH login detection

Detects repeated authentication failures:

```
Failed password for root from 192.168.1.10
```

---

### Brute-force detection

Detects multiple failed login attempts from the same IP:

```
FAILED_LOGIN × 3
→ BRUTEFORCE ALERT
```

---

### Anomalous login detection

Flags unusual login sources compared to baseline behavior:

```
internal subnet → normal
external IP → suspicious
```

---

# Technology Stack

| Component | Purpose |
|----------|---------|
Python | Detection engine core |
Pandas | Structured log processing |
Scikit-learn | IsolationForest anomaly detection |
Sigma Rules | Rule-based detection |
Streamlit | Dashboard visualization |
YAML | Detection configuration |

---

# Project Structure

```
ai-soc-log-analyzer/
│
├── parser/
│   └── log_parser.py
│
├── detection/
│   ├── anomaly_detector.py
│   ├── sigma_rules_engine.py
│   └── bruteforce_detector.py
│
├── scoring/
│   └── risk_score.py
│
├── dashboard/
│   └── app.py
│
├── config/
│   └── multiple_failed_login.yaml
│
├── main.py
└── requirements.txt
```

---

# Example Workflow

Example authentication logs:

```
Failed password for root from 192.168.1.10
Failed password for root from 192.168.1.10
Failed password for root from 192.168.1.10
```

Detection output:

```
SIGMA_ALERT
BRUTEFORCE_ALERT
Severity: HIGH
```

---

# Real-World Use Cases

This system can be integrated into:

- Linux SSH monitoring pipelines
- SOC authentication monitoring workflows
- Security lab environments
- Detection engineering research prototypes
- SIEM preprocessing layers

Example enterprise scenario:

```
Multiple Linux servers
        ↓
Log forwarder (Filebeat / rsyslog)
        ↓
Detection engine (this project)
        ↓
SIEM / Dashboard
```

---

# Future Improvements

Planned enhancements:

- GeoIP enrichment detection
- Trusted subnet awareness
- UEBA-style behavior profiling
- MITRE ATT&CK technique mapping
- JSON alert export for SIEM integration
- Dockerized deployment architecture

---

# Detection Strategy

This project combines three detection layers:

### 1. Anomaly Detection

Detects unusual login behavior using machine learning:

```
IsolationForest
```

---

### 2. Rule-Based Detection

Detects suspicious authentication patterns using Sigma rules:

```
FAILED_LOGIN
ROOT_LOGIN
SUDO_EXECUTION
```

---

### 3. Correlation Engine

Detects behavioral attack patterns:

```
FAILED_LOGIN × N
→ BRUTEFORCE ATTACK
```

---

# Severity Scoring Logic

Severity levels are assigned based on combined signals:

| Condition | Severity |
|----------|----------|
Single failed login | LOW |
Anomalous login behavior | HIGH |
Repeated failed logins | HIGH |
Brute-force pattern detected | HIGH |

---

# Author

Developed as a detection engineering portfolio project focused on hybrid SIEM-style authentication monitoring.

GitHub:
https://github.com/LutfiAds
