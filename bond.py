import os
import requests
FX_API_URL = "https://er-api.com" 

class FinancialRouter:
    def __init__(self, business_type, capex):
        self.business_type = business_type
        self.capex = float(capex)
        self.tier = self._determine_tier()

    def _determine_tier(self):
        """Categorizes the project based on CAPEX requirements."""
        if self.capex < 1_000_000:
            return "Tier 3: Small to Medium Business (SME)"
        elif 1_000_000 <= self.capex < 50_000_000:
            return "Tier 2: Mid-Market Commercial"
        else:
            return "Tier 1: Global Institutional / Mega-Project"

    def match_banks(self):
        """Identifies the best banking partners based on CAPEX tier."""
        print(f"\n[+] Analyzing FinTech Router Matrix for Category: {self.business_type}")
        print(f"[+] Targeted Tier: {self.tier}")
        
        if "Tier 3" in self.tier:
            return {
                "Recommended Banks": ["Wells Fargo", "Chase Business", "Local Credit Unions"],
                "Strategy": "Standard SBA Loans, Line of Credit, or Asset-Based Lending."
            }
        elif "Tier 2" in self.tier:
            return {
                "Recommended Banks": ["Bank of America Global Commercial", "PNC", "Fifth Third"],
                "Strategy": "Syndicated credit facilities, equipment financing, and commercial mortgages."
            }
        else:
            return {
                "Recommended Banks": ["Goldman Sachs", "J.P. Morgan Chase Co.", "Citi Institutional", "HSBC Global"],
                "Strategy": "Project Finance, Debt Capital Markets (Bond Issuance), or International Syndication."
            }

    def fetch_live_forex_trends(self):
        """
        Fetches live macro forex data to assess macro economic conditions.
        Demonstrates API integration capabilities for GitHub portfolios.
        """
        print("\n[+] Pinging Live Forex API for Global Macro Metrics...")
        try:
            response = requests.get(FX_API_URL, timeout=10)
            if response.status_code == 200:
                data = response.json()
                rates = data.get("rates", {})
                return {
                    "USD": rates.get("USD", 1.0),
                    "JPY": rates.get("JPY", "N/A"),
                    "EUR": rates.get("EUR", "N/A"),
                    "AUD": rates.get("AUD", "N/A")
                }
            else:
                print("[!] API responded with an error status.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"[-] Failed to reach Forex API: {e}")
            return None

    def analyze_carry_trade(self, fx_rates):
        """Evaluates FX carry trade ideas for Tier 1 mega-projects."""
        if "Tier 1" not in self.tier:
            return "Carry trade analysis bypassed. Project scale does not justify cross-border FX risk."
        
        if not fx_rates or fx_rates.get("JPY") == "N/A":
            return "Unable to calculate carry trade metrics due to missing live API data."

        analysis = (
            f"\n===========================================================\n"
            f"GLOBAL CARRY TRADE MEMO FOR MEGA CAPEX (${self.capex:,.2f})\n"
            f"===========================================================\n"
            f"Live Base Rates (Relative to USD):\n"
            f" - USD Base: {fx_rates['USD']}\n"
            f" - JPY (Traditional Funding Currency): {fx_rates['JPY']}\n"
            f" - AUD (Traditional Commodity Yield Currency): {fx_rates['AUD']}\n\n"
            f"STRATEGY:\n"
            f"Given your massive CAPEX of ${self.capex:,.2f} for a {self.business_type} project,\n"
            f"your institutional desk (e.g., Goldman Sachs/HSBC) may evaluate borrowing capital\n"
            f"in a low-yield currency (like JPY) to fund operations, provided currency hedges\n"
            f"are structured via FX Forwards/Swaps to protect against sudden exchange shocks."
        )
        return analysis

def main():
    print("====================================================")
    print("      INSTITUTIONAL CAPEX & BANK ROUTER SYSTEM     ")
    print("====================================================\n")
    
    business_type = input("What kind of business or project is this? (e.g., Energy, SaaS, Manufacturing): ").strip()
    
    while True:
        try:
            capex_input = input("What is the estimated CAPEX of the business/project (in USD)? $").replace(',', '').strip()
            capex = float(capex_input)
            if capex <= 0:
                print("CAPEX must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    router = FinancialRouter(business_type, capex)
    bank_results = router.match_banks()
    print("\n--- BANK MATCHING RESULTS ---")
    for key, val in bank_results.items():
        if isinstance(val, list):
            print(f"{key}: {', '.join(val)}")
        else:
            print(f"{key}: {val}")
    fx_data = router.fetch_live_forex_trends()
    macro_memo = router.analyze_carry_trade(fx_data)
    print(macro_memo)

if __name__ == "__main__":
    main()
