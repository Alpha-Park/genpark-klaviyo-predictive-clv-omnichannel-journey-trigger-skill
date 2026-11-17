# genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![MCP SDK](https://img.shields.io/badge/MCP_SDK-required-blue?style=for-the-badge)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

Klaviyo-inspired Predictive Customer Lifetime Value (CLV) & Omnichannel Journey Trigger. Estimates 365-day CLV using recency-frequency-monetary models, forecasts churn probability, and orchestrates personalized cross-channel flows (SMS, Email, Push) while enforcing fatigue limits.

---

## MCP runtime requirements

Use Python 3.10 or newer. The core `client.py` uses only the standard library; `mcp_server.py` requires the official `mcp` SDK (`mcp>=1.0.0,<2`). From this repository's checkout, create an isolated environment and install its requirements:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\python.exe` instead. You may use an existing Python environment with the requirements installed. Configure your MCP client with that interpreter's absolute path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; the GitHub repository URL is not a remote MCP endpoint.

Example client configuration (replace the placeholder paths):

```json
{
  "mcpServers": {
    "genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill": {
      "command": "/absolute/path/to/genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill/.venv/bin/python",
      "args": [
        "/absolute/path/to/genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill/mcp_server.py"
      ]
    }
  }
}
```

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

---

## 🌟 Key Features

- **Standard-Library Core**: Direct `client.py` use needs no external packages; MCP use requires Python 3.10+ and the official `mcp` SDK.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Public Source**: Maintained in the [Alpha-Park repository](https://github.com/Alpha-Park/genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill).

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import KlaviyoPredictiveCLVOmnichannelJourneyTrigger

def main():
    trigger = KlaviyoPredictiveCLVOmnichannelJourneyTrigger()
    profile = {
        "customer_id": "VIP-8812",
        "total_orders": 8,
        "total_spend_usd": 1280.0,
        "days_since_last_order": 20,
        "days_since_last_touchpoint": 5
    }
    result = trigger.evaluate_customer_journey(profile)
    print("--- Klaviyo Predictive CLV & Journey Trigger ---")
    print(f"Customer: {result['customer_id']} | 365d Predicted CLV: ${result['predictive_metrics']['predicted_next_365d_clv_usd']}")
    print(f"Churn Risk: {result['predictive_metrics']['churn_probability']*100:.1f}%")
    print(f"Flow Triggered: {result['automated_journey_trigger']['flow_name']} via {result['automated_journey_trigger']['channel']}")
    print(f"Incentive: {result['automated_journey_trigger']['incentive_offer']}")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
.venv/bin/python mcp_server.py
```

Execute embedded test harness:

```bash
.venv/bin/python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
