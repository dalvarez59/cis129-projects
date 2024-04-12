# Module 5 Lab
# Author: Diego Alvarez
# Description: This code calculates the amount of bottles in 7 days
# Step 1: Declare variables
total_bottles = 0
today_bottles = 0
counter = 0
total_payout = 0
keep_going = "y"


# Step 2: Loop to run program again
while keep_going.lower() == "y":
    # Step 3: Code to set value of variables
    total_bottles = 0
    today_bottles = 0
    counter = 0
    total_payout = 0

    # Loop for the seven days to get number of bottles
    NUMBER_OF_DAYS = 7
    total_bottles = 0
    for counter in range(NUMBER_OF_DAYS):
        print("Enter number of bottles returned for day #", counter + 1, ":")
        today_bottles = int(input())
        total_bottles += today_bottles


    # Calculate total payout
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    # Print total bottles collected and total payout
    print()  # Print a blank line for spacing
    print("Total number of bottles collected:", total_bottles)
    print("Total payout amount: $", format(total_payout, ".2f"))
    print()  # Print a blank line for spacing

    # Display user to continue or exit
    print("Do you want to enter another week's worth of data? (Enter y or n)")
    keep_going = input().lower()
