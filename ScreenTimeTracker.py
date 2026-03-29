import json
import matplotlib.pyplot as plt

#------Data Storage------------
screen_times = []
data = {}

#-------Load Data from JSON File--------
def load_data():
    global data, screen_times
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            screen_times = [info["hours"] for info in data.values()]
    except FileNotFoundError:
        data = {}
        screen_times = []

def save_data():
    with open("data.json", "w") as file:
        json.dump(data, file)

#------Feedback---------------------
def get_message(hours):
    if hours < 2:
        return "WOW, PRODUCTIVE DAY"
    elif hours < 5:
        return "BAD, YOU NEED TO REDUCE YOUR SCR-TIME"
    elif hours < 8:
        return "WORST, Give Yourself a Break"
    else:
        return "Go Touch Grass! Right Now"

#------Graph Function------------------------------
def show_graph():
    if not data:
        print("No Data to display!")
        return

    date = list(data.keys())
    hours = [info["hours"] for info in data.values()]
    plt.bar(date, hours, color='skyblue')
    plt.xlabel("Date")
    plt.ylabel("Screen Time (hours)")
    plt.title("Screen Time Analysis")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#---Load Existing Data------------------
load_data()

#----------Main Menu--------------------------
while True:
    print("\n======= Your Screen Time ==========")
    print("1. Log Time")
    print("2. View Report")
    print("3. Reality Check")
    print("4. Show Graph")
    print("5. Exit")
    
    choice = input("\nEnter Choice (1-5): ")
    
    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        try:
            hours = float(input("Enter screen time (hours): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        app = input("Most used app: ").strip()
        if app == "":
            print("App name can't be empty!")
            continue

        entry_time = (date, "Logged")
        screen_times.append(hours)
        data[date] = {
            "hours": hours,
            "app": app,
            "entry": entry_time
        }
        save_data()
        print("\nData Saved!")

    elif choice == "2":
        if not screen_times:
            print("No data available!")
        else:
            total = sum(screen_times)
            avg = total / len(screen_times)
            print("\n======= Report =======")
            print("Total Screen Time:", total, "hours")
            print("Average Screen Time:", round(avg, 2), "hours")
            print("\nDaily Details:")
            for date, info in data.items():
                print(f"{date} -> {info['hours']} hrs (App: {info['app']})")

    elif choice == "3":
        if not screen_times:
            print("No data! Please log screen time first.")
        else:
            last_hours = screen_times[-1]
            message = get_message(last_hours)
            print("\n======= Reality Check =======")
            print(message)
            if last_hours > 8:
                print("Warning! Too much screen time today!")

    elif choice == "4":
        show_graph()

    elif choice == "5":
        print("Exiting... Stay productive!")
        break

    else:
        print("Invalid choice, try again!")
