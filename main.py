import datetime

def get_clutch_info():
    lay_date_str = input("When did the clutch lay? (MM/DD/YY): ")
    average_days_to_pip = int(input("What is your average total days before pip?: "))

    # Convert the lay date string to a datetime object
    try:
        lay_date = datetime.datetime.strptime(lay_date_str, "%m/%d/%y")
    except ValueError:
        print("Error: The date format should be MM/DD/YY")
        return

    # Calculate the expected hatching date
    expected_hatch_date = lay_date + datetime.timedelta(days=average_days_to_pip)

    # Format the expected hatching date as MM/DD/YY
    expected_hatch_date_str = expected_hatch_date.strftime("%m/%d/%y")

    print(f"Based on your average days to pip, you should expect the clutch to pip on {expected_hatch_date_str}")

if __name__ == "__main__":
    get_clutch_info()
