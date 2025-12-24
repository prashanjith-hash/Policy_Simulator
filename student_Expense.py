def main():
    print("🧾 Student GST Tax Change Analyzer (Custom Rates)")
    print("=" * 60)
    
    total_spent = float(input("Enter total amount spent (₹): "))
    
    categories = ['movie tickets', 'stationary', 'fast food chains', 'restaurants']
    spending = {}
    
    print("\n📋 Enter your spending breakdown:")
    for cat in categories:
        while True:
            try:
                amount = float(input(f"₹ spent on {cat}: "))
                spending[cat] = amount
                break
            except ValueError:
                print("Please enter a valid number!")
    
    print("\n💰 Enter actual TAX PERCENTAGES you experienced:")
    taxes = {}
    for cat in categories:
        print(f"\n--- {cat.upper()} ---")
        while True:
            try:
                pct_before = float(input(f"GST % BEFORE reforms: "))
                pct_after = float(input(f"GST % AFTER reforms: "))
                taxes[cat] = {'before': pct_before/100, 'after': pct_after/100}
                break
            except ValueError:
                print("Please enter valid percentages (e.g., 12 for 12%)!")
    
    print("\n" + "="*75)
    print("📊 DETAILED TAX ANALYSIS REPORT")
    print("="*75)
    
    total_tax_before = 0
    total_tax_after = 0
    total_gain_loss = 0
    
    print(f"{'Category':<18} {'Spent':<10} {'Before %':<9} {'Tax Bfr':<10} {'After %':<9} {'Tax Aft':<9} {'Gain/Loss':<10}")
    print("-" * 75)
    
    for cat, amount in spending.items():
        rate_before = taxes[cat]['before']
        rate_after = taxes[cat]['after']
        
        tax_before = amount * rate_before
        tax_after = amount * rate_after
        gain_loss = tax_before - tax_after
        
        total_tax_before += tax_before
        total_tax_after += tax_after
        total_gain_loss += gain_loss
        
        status = "💰 SAVINGS" if gain_loss > 0 else "📉 LOSS"
        print(f"{cat:<18} {amount:<10.0f} {rate_before*100:<7.1f}% {tax_before:<10.0f} {rate_after*100:<7.1f}% {tax_after:<9.0f} {gain_loss:<8.0f} {status}")
    
    print("-" * 75)
    print(f"{'TOTAL SPENT':<28} {total_spent:<10.0f}")
    print(f"{'TOTAL TAX BEFORE':<28} {total_tax_before:<10.0f}")
    print(f"{'TOTAL TAX AFTER':<28} {total_tax_after:<10.0f}")
    print(f"{'NET SAVINGS/LOSS':<28} {total_gain_loss:<10.0f}")
    print("="*75)
    
    if total_tax_before > 0:
        savings_pct = (total_gain_loss / total_tax_before * 100)
        print(f"💡 Tax burden reduced by {savings_pct:.1f}%!")
    
    if total_gain_loss > 0:
        print("🎉 GST reforms saved you money across categories!")
        print("📱 Perfect for your app - shows real user impact!")
    else:
        print("📊 Post-reform taxes higher in your spending pattern.")

if __name__ == "__main__":
    main()
    