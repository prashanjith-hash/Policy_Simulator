# Policy Impact Simulator
# Unified Menu-Driven Program (Round 1 Ready)

def classify_impact(percent):
    percent = abs(percent)
    if percent < 2:
        return "🟢 Low Impact (barely noticeable)"
    elif percent <= 5:
        return "🟡 Moderate Impact (you will feel this)"
    else:
        return "🔴 High Impact (significant impact)"


def show_result(old_cost, new_cost, insight):
    change = new_cost - old_cost
    percent_change = (change / old_cost) * 100

    print("\n📊 IMPACT SUMMARY")
    print("--------------------------------------------------")
    print(f"Earlier monthly cost : ₹{old_cost:.2f}")
    print(f"Current monthly cost : ₹{new_cost:.2f}")

    if change > 0:
        print(f"📉 LOSS of ₹{change:.2f} per month")
        print(f"💡 To maintain old budget, reduce spending by ₹{change:.2f}")
    else:
        print(f"📈 GAIN of ₹{abs(change):.2f} per month")
        print(f"💡 You can spend ₹{abs(change):.2f} more safely")

    print(f"📌 Impact Level : {classify_impact(percent_change)}")

    print("\n🧠 Why this happens?")
    print(insight)
    print("--------------------------------------------------\n")


# ---------------- STUDENT ----------------
def student_restaurant_gst():
    print("\n🎓 STUDENT – RESTAURANT GST CHECK")

    spending = float(input("Monthly restaurant spending (before GST) ₹: "))
    old_gst = float(input("Old GST rate %: "))
    new_gst = float(input("New GST rate %: "))

    old_total = spending * (1 + old_gst / 100)
    new_total = spending * (1 + new_gst / 100)

    insight = (
        "Students eat out frequently. Even small GST increases add up over time "
        "because the tax is paid repeatedly on every bill."
    )

    show_result(old_total, new_total, insight)


# ---------------- HOUSEHOLD ----------------
def household_lpg_subsidy():
    print("\n🏠 HOUSEHOLD – LPG SUBSIDY CHECK")

    base_cost = float(input("Monthly LPG cost before subsidy ₹: "))
    old_subsidy = float(input("Old subsidy amount ₹: "))
    new_subsidy = float(input("New subsidy amount ₹: "))

    old_total = base_cost - old_subsidy
    new_total = base_cost - new_subsidy

    insight = (
        "LPG subsidies directly reduce household expenses. "
        "Any reduction is immediately felt in monthly budgets."
    )

    show_result(old_total, new_total, insight)


# ---------------- SMALL BUSINESS ----------------
def business_import_duty():
    print("\n🏪 SMALL BUSINESS – IMPORT DUTY CHECK")

    base_cost = float(input("Monthly raw material cost (before duty) ₹: "))
    old_duty = float(input("Old import duty rate %: "))
    new_duty = float(input("New import duty rate %: "))

    old_total = base_cost * (1 + old_duty / 100)
    new_total = base_cost * (1 + new_duty / 100)

    insight = (
        "Import duty increases raw material costs. "
        "Small businesses often absorb this cost before increasing prices."
    )

    show_result(old_total, new_total, insight)


# ---------------- MENUS ----------------
def student_menu():
    student_restaurant_gst()


def household_menu():
    household_lpg_subsidy()


def business_menu():
    business_import_duty()


def main_menu():
    print("\n🌍 POLICY IMPACT SIMULATOR")
    print("Select your category:")
    print("1️⃣  Student")
    print("2️⃣  Household")
    print("3️⃣  Small Business")

    choice = input("Enter choice (1 / 2 / 3): ")

    if choice == "1":
        student_menu()
    elif choice == "2":
        household_menu()
    elif choice == "3":
        business_menu()
    else:
        print("❌ Invalid choice. Please restart.")


# ---------------- PROGRAM LOOP ----------------
while True:
    main_menu()
    again = input("🔄 Do you want to check another case? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for using the Policy Impact Simulator!")
        break

