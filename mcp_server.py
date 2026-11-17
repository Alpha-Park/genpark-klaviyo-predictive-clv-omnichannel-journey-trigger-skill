#!/usr/bin/env python3
import json
import sys
from client import KlaviyoPredictiveCLVOmnichannelJourneyTrigger

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-klaviyo-predictive-clv-omnichannel-journey-trigger-skill')

@mcp.tool()
def evaluate_customer_journey(customer_profile: Optional[Dict[str, Any]] = None) -> str:
    """Evaluate the customer journey using the provided profile."""
    return json.dumps(KlaviyoPredictiveCLVOmnichannelJourneyTrigger().evaluate_customer_journey(customer_profile if customer_profile is not None else {}))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        trigger = KlaviyoPredictiveCLVOmnichannelJourneyTrigger()
        cust = {"customer_id": "C-1209", "total_orders": 5, "total_spend_usd": 450.0, "days_since_last_order": 95, "days_since_last_touchpoint": 7}
        res = trigger.evaluate_customer_journey(cust)
        assert res["verdict"] == "JOURNEY_TRIGGERED_SUCCESSFULLY"
        assert res["predictive_metrics"]["churn_probability"] > 0.5
        print(f"[TEST PASS] Klaviyo Journey Trigger Passed! Flow: {res['automated_journey_trigger']['flow_name']}")
        sys.exit(0)

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
