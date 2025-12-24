# Small Business Policy Impact Simulator
# Menu-driven base logic (Round 1)

def classify_impact(percent):
    percent = abs(percent)
    if percent < 2:
        return "🟢 Low Impact (manageable)"
    elif percent <= 5:
        return "🟡 Moderate Impact (needs attention)"
    else:
        return "🔴 High Impact (serious business impact)"


def show_result(old_cost, new_cost, insight):
    change = new_cost - old_cost
    percent_change = (change / old_cost) * 100

    print("\n📊 BUSINESS IMPACT SUMMARY")
    print("--------------------------------------------------")
    print(f"Earlier monthly cost : ₹{old_cost:.2f}")
    print(f"Current monthly cost : ₹{new_cost:.2f}")

    if change > 0:
        print(f"📉 This policy causes a LOSS of ₹{change:.2f} per month")
    else:
        print(f"📈 This policy gives a GAIN of ₹{abs(change):.2f} per month")

    print(f"📌 Impact Level : {classify_impact(percent_change)}")

    if change > 0:
        print(f"💡 To maintain old costs, reduce expenses by ₹{change:.2f}")
    else:
        print(f"💡 You have ₹{abs(change):.2f} extra flexibility per month")

    print("\n🧠 Business Insight:")
    print(insight)
    print("--------------------------------------------------\n")


def import_duty():
    print("\n🚢 IMPORT DUTY IMPACT CHECK")

    base_cost = float(input("Monthly raw material cost (before duty) ₹: "))
    old_duty = float(input("Old import duty rate %: "))
    new_duty = float(input("New import duty rate %: "))

    old_total = base_cost * (1 + old_duty / 100)
    new_total = base_cost * (1 + new_duty / 100)

    insight = (
        "Import duties directly increase raw material costs. "
        "Small businesses often absorb this increase before passing it to customers."
    )

    show_result(old_total, new_total, insight)

def business_subsidy():
    print("\n🏭 BUSINESS SUBSIDY CHANGE CHECK")

    subsidy_type = input("Enter Resource for Subsidy: ")

    base_expense = float(input(f"Monthly {subsidy_type} expense before subsidy ₹: "))
    old_subsidy = float(input(f"Old {subsidy_type} subsidy amount ₹: "))
    new_subsidy = float(input(f"New {subsidy_type} subsidy amount ₹: "))

    old_total = base_expense - old_subsidy
    new_total = base_expense - new_subsidy

    insight = (
        f"Subsidies on {subsidy_type} help small businesses control operating costs. "
        f"Any reduction in {subsidy_type} subsidy directly increases monthly expenses "
        f"and puts pressure on profit margins."
    )

    show_result(old_total, new_total, insight)


def gst_on_sales():
    print("\n📦 GST ON BUSINESS SALES CHECK")

    monthly_revenue = float(input("Monthly sales value (before GST) ₹: "))
    old_gst = float(input("Old GST rate %: "))
    new_gst = float(input("New GST rate %: "))

    old_total = monthly_revenue * (1 + old_gst / 100)
    new_total = monthly_revenue * (1 + new_gst / 100)

    insight = (
        "GST changes affect final selling prices. "
        "Small businesses must choose between raising prices or sacrificing margins."
    )

    show_result(old_total, new_total, insight)


def run_program():
    print("\n🏪 SMALL BUSINESS POLICY IMPACT SIMULATOR")
    print("Choose what you want to check:")
    print("1️⃣  Import Duty on Raw Materials")
    print("2️⃣  Business Subsidy Change")
    print("3️⃣  GST on Business Sales")

    choice = input("Enter your choice (1 / 2 / 3): ")

    if choice == "1":
        import_duty()
    elif choice == "2":
        business_subsidy()
    elif choice == "3":
        gst_on_sales()
    else:
        print("❌ Invalid choice. Please restart and try again.")
        return


while True:
    run_program()
    again = input("🔄 Do you want to check another policy? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for using the Small Business Policy Simulator!")
        break

