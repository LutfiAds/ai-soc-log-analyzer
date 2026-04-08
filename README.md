# AI SOC Log Analyzer

Lightweight Authentication Threat Detection Platform for Linux SSH Monitoring
Detection engineering pipeline with enrichment, correlation, MITRE ATT&CK mapping, and SIEM-compatible alert export.

---

## Overview

AI SOC Log Analyzer is a modular authentication threat detection pipeline designed to simulate real-world SOC detection workflows.

The system ingests authentication logs from multiple Linux hosts, enriches them with threat intelligence context, detects suspicious behavior patterns, correlates attack activity across infrastructure, and exports structured alerts compatible with SIEM ingestion pipelines.

This project demonstrates how detection engineering pipelines operate internally inside modern SOC environments.

---

## Detection Capabilities

The pipeline detects:

* brute-force login attempts
* distributed password spraying campaigns
* suspicious successful logins from external networks
* authentication anomalies using machine learning
* high-risk country login attempts
* malicious IP reputation matches
* cross-host attack correlation patterns

---

## Detection Pipeline Architecture

```
multi-host ingestion
→ parsing
→ trusted subnet awareness
→ GeoIP enrichment
→ IP reputation enrichment
→ country risk classification
→ anomaly detection (IsolationForest)
→ sigma rule detection
→ brute-force detection
→ cross-host correlation
→ successful login anomaly detection
→ MITRE ATT&CK mapping
→ YAML rule-engine severity overrides
→ ECS-compatible alert export
→ Streamlit dashboard visualization
→ scheduled execution mode
```

---

## Features

### Multi-host ingestion

Supports simultaneous authentication log ingestion from multiple Linux servers.

Example:

```
data/
 ├── bastion_auth.log
 ├── web01_auth.log
 └── db01_auth.log
```

---

### GeoIP enrichment

Adds country-level context to login source IP addresses using GeoLite2.

Example:

```
185.220.101.4 → Germany
```

---

### IP reputation enrichment

Matches login IP addresses against configurable threat intelligence feeds.

Example:

```
ip_reputation = MALICIOUS
```

---

### Country risk classification

Flags authentication attempts originating from high-risk geographic regions.

---

### Machine learning anomaly detection

IsolationForest identifies abnormal authentication behavior patterns automatically.

---

### Sigma-style detection rules

Detects authentication attack patterns using configurable detection signatures.

Example:

```
multiple_failed_login.yaml
```

---

### Cross-host correlation engine

Identifies distributed attack campaigns targeting multiple servers simultaneously.

Example:

```
same IP attacking bastion + web01 + db01
```

---

### Suspicious successful login detection

Detects credential compromise indicators when authentication succeeds from external networks.

Mapped to:

```
MITRE ATT&CK T1078
Persistence
```

---

### MITRE ATT&CK mapping

Each detection event is mapped to:

* technique ID
* tactic classification

Examples:

```
T1110 Credential Access
T1078 Persistence
```

---

### YAML-based detection rule engine

Detection logic can be modified without editing Python code.

Example:

```
config/detection_rules.yaml
```

---

### ECS-compatible alert export

Exports structured detection events compatible with:

* Elastic Security
* Splunk
* Microsoft Sentinel
* QRadar ingestion pipelines

Example output:

```
source.ip
host.name
event.category
event.outcome
threat.technique.id
event.severity
```

---

### Scheduler mode

Runs detection pipeline continuously at configurable intervals.

Example:

```
python main.py --export --interval 300
```

---

### Streamlit dashboard

Interactive visualization of authentication alerts and threat activity.

Launch dashboard:

```
streamlit run dashboard/app.py
```

---

## Example Detection Output

```
{
  "@timestamp": "2026-07-10 10:25:01",
  "event.category": "authentication",
  "event.outcome": "failure",
  "host.name": "bastion",
  "source.ip": "185.220.101.4",
  "ip_reputation": "MALICIOUS",
  "threat.technique.id": "T1110",
  "threat.tactic.name": "Credential Access",
  "event.severity": "CRITICAL"
}
```

---

## Project Structure

```
parser/
detection/
classification/
scoring/
mapping/
enrichment/
exporter/
dashboard/
config/
data/
alerts/
```

---

## Use Cases

This project simulates detection workflows used by:

* Security Operations Centers (SOC)
* Detection Engineers
* Threat Hunters
* Blue Team analysts
* SIEM pipeline developers

Typical applications include:

* SSH brute-force monitoring
* credential compromise detection
* infrastructure attack correlation
* authentication anomaly detection
* SIEM enrichment pipeline prototyping

---

## Requirements

Python 3.10+

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run Detection Pipeline

Single execution:

```
python main.py --export
```

Continuous monitoring mode:

```
python main.py --export --interval 60
```

---

## Dashboard

Start visualization interface:

```
streamlit run dashboard/app.py
```

---

## Roadmap

Completed:

* multi-host ingestion
* GeoIP enrichment
* IP reputation feeds
* anomaly detection engine
* sigma detection rules
* correlation engine
* MITRE ATT&CK mapping
* YAML detection rule system
* ECS-compatible export schema
* scheduler runtime mode

Future improvements:

* external threat intelligence API integration
* container authentication monitoring support
* Windows event log support
* real-time log streaming ingestion
