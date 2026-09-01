def no_power_troubleshooting():
    print("\n--- PC Won't Power On ---")

    answer = input("Does the PC show any lights or fan movement? (yes/no): ").lower()

    if answer == "no":
        print("\nPossible causes:")
        print("- Power cable disconnected")
        print("- PSU switch is turned off")
        print("- Faulty power supply")
        print("- Front panel power connector disconnected")
        print("\nRecommended action:")
        print("Check the power cable, PSU switch, and motherboard power connections.")

    elif answer == "yes":
        print("\nThe system is receiving power.")
        print("Continue with display or POST troubleshooting.")

    else:
        print("\nInvalid answer. Please enter yes or no.")


def no_display_troubleshooting():
    print("\n--- PC Powers On But No Display ---")

    answer = input("Are the monitor and display cable connected correctly? (yes/no): ").lower()

    if answer == "no":
        print("\nRecommended action:")
        print("Reconnect the monitor power and HDMI/DisplayPort cable.")

    elif answer == "yes":
        print("\nCheck the following:")
        print("- Reseat the RAM")
        print("- Check GPU power cables")
        print("- Try motherboard video output if supported")
        print("- Check motherboard debug LEDs")
        print("- Try another display cable or monitor")

    else:
        print("\nInvalid answer. Please enter yes or no.")


def main():
    while True:
        print("\n================================")
        print("       PC TROUBLESHOOTING")
        print("================================")
        print("1. PC Won't Power On")
        print("2. PC Powers On But No Display")
        print("3. Exit")

        choice = input("\nSelect a problem: ")

        if choice == "1":
            no_power_troubleshooting()
        elif choice == "2":
            no_display_troubleshooting()
        elif choice == "3":
            print("\nExiting PC Troubleshooting Tool...")
            break
        else:
            print("\nInvalid option. Please select 1-3.")


if __name__ == "__main__":
    main()
