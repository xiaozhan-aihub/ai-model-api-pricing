"""Refuse to publish a catalogue that looks broken (used by the daily sync workflow).

    python3 scripts/check.py models.json models.csv

Right after a platform release the first response can be a build-time copy without the
model list; publishing it would wipe the data here, so the sync stops instead and the
next day's run picks up the real file.
"""

import csv
import json
import sys

json_path, csv_path = sys.argv[1], sys.argv[2]

with open(json_path, encoding="utf-8") as f:
    doc = json.load(f)
models = doc.get("models") or []
with open(csv_path, encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

problems = []
if not models:
    problems.append("no models in models.json")
if doc.get("count") != len(models):
    problems.append(f"count {doc.get('count')} != {len(models)} models")
if len(rows) != len(models):
    problems.append(f"models.csv has {len(rows)} rows, models.json {len(models)} models")
if (doc.get("license") or {}).get("name") != "CC BY 4.0":
    problems.append(f"unexpected licence {doc.get('license')}")
if any(not m.get("id") or not m.get("url") for m in models):
    problems.append("a model without id or url")

if problems:
    sys.exit("refusing to publish: " + "; ".join(problems))
print(f"ok: {len(models)} models, updated_at {doc.get('updated_at')}")
