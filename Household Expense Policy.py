# Household Policy Impact Simulator
# Casual, user-friendly version (Round 1 ready)

def classify_impact(percent):
    percent = abs(percent)
    if percent < 2:
        return "🟢 Low Impact (barely noticeable)"
    elif percent <= 5:
        return "🟡 Moderate Impact (you will feel this)"
    else:
        return "🔴 High Impact (significant monthly change)"


def show_result(old_cost, new_cost, insight_line):
    change = new_cost - old_cost
    percent_change = (change / old_cost) * 100

    print("\n📊 RESULT SUMMARY")
    print("--------------------------------------------------")
    print(f"Earlier monthly expense : ₹{old_cost:.2f}")
    print(f"Current monthly expense : ₹{new_cost:.2f}")

    if change > 0:
        print(f"📉 This policy causes a LOSS of ₹{change:.2f} per month")
    else:
        print(f"📈 This policy gives a GAIN of ₹{abs(change):.2f} per month")

    print(f"📌 Impact Level : {classify_impact(percent_change)}")

    if change > 0:
        print(f"💡 To stay within your old budget, reduce spending by ₹{change:.2f}")
    else:
        print(f"💡 You can spend ₹{abs(change):.2f} more and still be safe")

    print("\n🧠 Why this happens?")
    print(insight_line)
    print("--------------------------------------------------\n")


def lpg_subsidy():
    print("\n🔥 LPG GAS SUBSIDY CHECK")

    base_cost = float(input("Monthly LPG cost (before subsidy) ₹: "))
    old_subsidy = float(input("Old subsidy amount ₹: "))
    new_subsidy = float(input("New subsidy amount ₹: "))

    old_total = base_cost - old_subsidy
    new_total = base_cost - new_subsidy

    insight = (
        "Subsidies directly reduce household expenses. "
        "When subsidies are reduced or removed, families immediately feel the cost increase."
    )

    show_result(old_total, new_total, insight)


def food_gst():
    print("\n🥦 DAILY FOOD ITEMS GST CHECK")

    spending = float(input("Monthly food spending (before GST) ₹: "))
    old_gst = float(input("Old GST rate %: "))
    new_gst = float(input("New GST rate %: "))

    old_total = spending * (1 + old_gst / 100)
    new_total = spending * (1 + new_gst / 100)

    insight = (
        "GST is paid every time you buy food. "
        "Even small rate changes slowly add up because food is a frequent expense."
    )

    show_result(old_total, new_total, insight)


def appliance_gst():
    print("\n🛒 HOUSEHOLD APPLIANCE GST CHECK")

    price = float(input("Appliance base price ₹: "))
    old_gst = float(input("Old GST rate %: "))
    new_gst = float(input("New GST rate %: "))

    old_total = price * (1 + old_gst / 100)
    new_total = price * (1 + new_gst / 100)

    insight = (
        "Higher GST on appliances increases the upfront cost. "
        "This often delays important household purchases."
    )

    show_result(old_total, new_total, insight)


def run_program():
    print("\n🏠 HOUSEHOLD POLICY IMPACT SIMULATOR")
    print("Choose what you want to check:")
    print("1️⃣  LPG Gas Cylinder Subsidy")
    print("2️⃣  Daily Food Items GST")
    print("3️⃣  Household Appliance GST")

    choice = input("Enter your choice (1 / 2 / 3): ")

    if choice == "1":
        lpg_subsidy()
    elif choice == "2":
        food_gst()
    elif choice == "3":
        appliance_gst()
    else:
        print("❌ Invalid choice. Please restart and try again.")
        return


while True:
    run_program()
    again = input("🔄 Do you want to check another policy? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for using the Policy Impact Simulator!")
        break
