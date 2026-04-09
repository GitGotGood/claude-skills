#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "## 1. Current frame",
    "## 2. Best alternative frames",
    "## 3. Hidden assumptions",
    "## 4. Key omissions",
    "## 5. Perspective shifts",
    "## 6. Metric audit",
    "## 7. Premortem",
    "## 8. Priority summary",
]

if len(sys.argv) != 2:
    print("Usage: validate_report.py <report.md>")
    sys.exit(2)

text = Path(sys.argv[1]).read_text(encoding="utf-8")
missing = [section for section in required if section not in text]

if missing:
    print("Missing sections:")
    for section in missing:
        print(f"- {section}")
    sys.exit(1)

print("Report structure valid.")
