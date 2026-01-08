import requests
import time

PROM_URL = "http://localhost:9090/api/v1/query"
QUERY = "node_load1"

baseline = []
BASELINE_COUNT = 10
THRESHOLD = 0.2  # 20% sudden jump

def get_load():
    r = requests.get(PROM_URL, params={"query": QUERY})
    result = r.json()["data"]["result"]
    return float(result[0]["value"][1])

prev = None

while True:
    load = get_load()

    if len(baseline) < BASELINE_COUNT:
        baseline.append(load)
        print(f"Learning baseline | LOAD={load:.2f}")
    else:
        avg = sum(baseline) / len(baseline)

        if prev and load > avg * (1 + THRESHOLD):
            print(f"⚠️ ANOMALY DETECTED | LOAD JUMPED from {prev:.2f} → {load:.2f}")
        else:
            print(f"Normal | LOAD={load:.2f}")

        baseline.pop(0)
        baseline.append(load)

    prev = load
    time.sleep(5)
