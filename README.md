🚀 AIOps Infrastructure Anomaly Detection Platform

End-to-End Observability + Intelligent Anomaly Detection using Prometheus, Loki, Grafana & Python

📌 Project Overview

This project demonstrates a real-world AIOps pipeline designed to monitor infrastructure metrics, collect logs, visualize system health, and detect anomalies automatically.

It simulates how modern DevOps & SRE teams build observability platforms to:

Detect abnormal system behavior

Reduce downtime

Enable data-driven operational decisions

⚙️ Built & tested on AWS EC2 (Linux)

🧠 Why This Project?

Traditional monitoring only shows what happened.
AIOps answers why it happened and when it will happen again.

This project:

Collects metrics and logs

Centralizes observability

Applies Python-based anomaly detection

Visualizes everything in Grafana

Perfect for:

DevOps Engineers

Cloud Engineers

SRE roles

AIOps / Observability interviews

🏗️ Architecture
┌────────────┐
│  EC2 Host  │
│            │
│ NodeExporter ──▶ Prometheus ──▶ Python (Anomaly Detection)
│     │                              │
│     ▼                              ▼
│  Promtail ──▶ Loki ───────────▶ Grafana
│
└────────────┘


📸 Architecture Diagram
(see /architecture/architecture-diagram.png)

🧩 Tech Stack
Layer	Tool
Metrics	Prometheus
Logs	Loki
Log Shipper	Promtail
Visualization	Grafana
Anomaly Detection	Python
Platform	AWS EC2
OS	Linux
📂 Project Structure
aiops-infrastructure-anomaly-detection/
│
├── README.md
├── architecture/
│   └── architecture-diagram.png
│
├── prometheus/
│   └── prometheus.yml
│
├── loki/
│   └── loki-config.yml
│
├── promtail/
│
├── grafana/
│   └── dashboards/
│       └── node-exporter-full.json
│
├── anomaly-d
