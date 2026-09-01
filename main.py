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

def random_shutdown_troubleshooting():
    print("\n--- Random Shutdowns / Restarts ---")

    answer = input(
        "Does the PC shut down more often during gaming or heavy use? (yes/no): "
    ).lower()

    if answer == "yes":
        print("\nPossible causes:")
        print("- CPU or GPU overheating")
        print("- Power supply instability")
        print("- Loose GPU or motherboard power cables")

        print("\nRecommended action:")
        print("- Check CPU and GPU temperatures")
        print("- Clean dust from fans and heatsinks")
        print("- Check PSU and GPU power connections")
        print("- Make sure all fans are spinning correctly")

    elif answer == "no":
        second_answer = input(
            "Does the PC restart without showing a shutdown message? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- Power supply problem")
            print("- RAM instability")
            print("- Driver or Windows crash")
            print("- Motherboard issue")

            print("\nRecommended action:")
            print("- Reseat the RAM")
            print("- Check Windows Event Viewer")
            print("- Update chipset and GPU drivers")
            print("- Test with another PSU if available")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Check Windows updates")
            print("- Scan for malware")
            print("- Review recently installed software")
            print("- Check Event Viewer for shutdown errors")

        else:
            print("\nInvalid answer. Please enter yes or no.")

    else:
        print("\nInvalid answer. Please enter yes or no.")

def main():
    while True:
        print("\n================================")
        print("       PC TROUBLESHOOTING")
        print("================================")
        print("1. PC Won't Power On")
        print("2. PC Powers On But No Display")
        print("3. Random Shutdowns / Restarts")
        print("4. Exit")

        choice = input("\nSelect a problem: ")

        if choice == "1":
            no_power_troubleshooting()
        elif choice == "2":
            no_display_troubleshooting()
        elif choice == "3":
            random_shutdown_troubleshooting()
        elif choice == "4":
            print("\nExiting PC Troubleshooting Tool...")
            break
        else:
            print("\nInvalid option. Please select 1-4.")


if __name__ == "__main__":
    main()
