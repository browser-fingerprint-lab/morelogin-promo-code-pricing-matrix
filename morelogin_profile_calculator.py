#!/usr/bin/env python3
"""MoreLogin Profile Tier & Team Seat TCO Calculator 2026."""
import argparse

TIER_BASE = {
    "starter": {"profiles": 10, "base_monthly": 9.0, "seats": 1},
    "growth": {"profiles": 50, "base_monthly": 25.0, "seats": 2},
    "pro": {"profiles": 100, "base_monthly": 40.0, "seats": 2},
    "scale": {"profiles": 200, "base_monthly": 80.0, "seats": 4},
    "enterprise": {"profiles": 500, "base_monthly": 150.0, "seats": 10}
}

def calculate(tier="pro", extra_seats=0, annual=True):
    data = TIER_BASE.get(tier.lower(), TIER_BASE["pro"])
    base = data["base_monthly"]
    seat_cost = extra_seats * 5.0
    monthly_subtotal = base + seat_cost
    discount_pct = 0.20 if annual else 0.0
    effective_monthly = monthly_subtotal * (1.0 - discount_pct)
    annual_total = effective_monthly * 12.0
    annual_savings = (monthly_subtotal * 12.0) - annual_total if annual else 0.0

    print("=" * 65)
    print(f"MoreLogin Antidetect Pricing Calculator: Tier {tier.upper()}")
    print("=" * 65)
    print(f"Browser Profiles:          {data['profiles']}")
    print(f"Included Team Seats:       {data['seats']} (+{extra_seats} extra)")
    print(f"Standard Monthly Total:    ${monthly_subtotal:.2f}/mo")
    print(f"Effective Monthly (20%):   ${effective_monthly:.2f}/mo")
    print(f"Annual Billed Total:       ${annual_total:.2f}/yr")
    if annual:
        print(f"Annual Discount Savings:   ${annual_savings:.2f}/yr")
    print("=" * 65)
    return effective_monthly, annual_savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MoreLogin Pricing Calculator")
    parser.add_argument("--tier", default="pro", choices=["starter", "growth", "pro", "scale", "enterprise"])
    parser.add_argument("--extra-seats", type=int, default=0)
    parser.add_argument("--monthly", action="store_true")
    args = parser.parse_args()
    calculate(tier=args.tier, extra_seats=args.extra_seats, annual=not args.monthly)
