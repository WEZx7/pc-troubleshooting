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

def overheating_troubleshooting():
    print("\n--- Overheating ---")

    answer = input(
        "Does the PC get very hot or loud during normal use? (yes/no): "
    ).lower()

    if answer == "yes":
        print("\nPossible causes:")
        print("- Dust buildup")
        print("- Poor airflow")
        print("- Failing or slow fans")
        print("- Old thermal paste")
        print("- High CPU or GPU load")

        print("\nRecommended action:")
        print("- Clean dust from fans and heatsinks")
        print("- Make sure case fans are installed correctly")
        print("- Check CPU and GPU temperatures")
        print("- Replace thermal paste if temperatures remain high")
        print("- Close unnecessary background applications")

    elif answer == "no":
        second_answer = input(
            "Does the PC overheat mainly during gaming or heavy workloads? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- GPU or CPU cooling limitation")
            print("- Poor case airflow")
            print("- Aggressive overclocking")
            print("- High power consumption")

            print("\nRecommended action:")
            print("- Monitor CPU and GPU temperatures")
            print("- Improve case airflow")
            print("- Reduce overclock settings")
            print("- Check fan curves")
            print("- Make sure vents are not blocked")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Check temperature sensors")
            print("- Inspect fans for unusual noise")
            print("- Verify heatsinks are mounted correctly")
            print("- Check for background processes using high CPU")

        else:
            print("\nInvalid answer. Please enter yes or no.")

    else:
        print("\nInvalid answer. Please enter yes or no.")

def slow_performance_troubleshooting():
    print("\n--- Slow Performance ---")

    answer = input(
        "Is the PC slow immediately after startup? (yes/no): "
    ).lower()

    if answer == "yes":
        print("\nPossible causes:")
        print("- Too many startup applications")
        print("- High background CPU or memory usage")
        print("- Low available storage")
        print("- Malware or unwanted software")

        print("\nRecommended action:")
        print("- Disable unnecessary startup apps")
        print("- Check Task Manager for high CPU or memory usage")
        print("- Free up disk space")
        print("- Run a malware scan")
        print("- Restart the PC and install pending updates")

    elif answer == "no":
        second_answer = input(
            "Does the PC become slow when opening programs or games? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- Insufficient RAM")
            print("- Slow or failing storage drive")
            print("- High CPU usage")
            print("- Background applications")
            print("- Thermal throttling")

            print("\nRecommended action:")
            print("- Check Task Manager performance usage")
            print("- Close unnecessary applications")
            print("- Check drive health")
            print("- Check CPU and GPU temperatures")
            print("- Consider upgrading RAM or storage if needed")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Check Windows updates")
            print("- Scan for malware")
            print("- Review installed applications")
            print("- Check available disk space")
            print("- Restart the system")

        else:
            print("\nInvalid answer. Please enter yes or no.")

    else:
        print("\nInvalid answer. Please enter yes or no.")

def boot_startup_troubleshooting():
    print("\n--- Boot / Windows Startup Problems ---")

    answer = input(
        "Does the PC reach the Windows loading screen? (yes/no): "
    ).lower()

    if answer == "no":
        print("\nPossible causes:")
        print("- Boot drive not detected")
        print("- Incorrect BIOS boot order")
        print("- Loose SATA or power cable")
        print("- Failed SSD or HDD")
        print("- Corrupted bootloader")

        print("\nRecommended action:")
        print("- Check if the storage drive appears in BIOS")
        print("- Verify the correct boot drive is selected")
        print("- Reseat storage cables if applicable")
        print("- Run drive diagnostics")
        print("- Try Windows recovery or startup repair")

    elif answer == "yes":
        second_answer = input(
            "Does Windows get stuck, restart, or show an error during startup? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- Corrupted Windows system files")
            print("- Failed Windows update")
            print("- Driver conflict")
            print("- Storage errors")
            print("- Malware or damaged startup files")

            print("\nRecommended action:")
            print("- Try Windows Safe Mode")
            print("- Run Startup Repair")
            print("- Use System Restore if available")
            print("- Check disk health")
            print("- Run system file repair tools")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Check startup applications")
            print("- Review recent Windows updates")
            print("- Check Event Viewer for boot errors")
            print("- Verify available storage space")
            print("- Restart and test again")

        else:
            print("\nInvalid answer. Please enter yes or no.")

    else:
        print("\nInvalid answer. Please enter yes or no.")

def bsod_troubleshooting():
    print("\n--- BSOD / Blue Screen ---")

    answer = input(
        "Did the blue screen start after installing a driver, update, or new hardware? (yes/no): "
    ).lower()

    if answer == "yes":
        print("\nPossible causes:")
        print("- Faulty or incompatible driver")
        print("- Problematic Windows update")
        print("- New hardware conflict")
        print("- BIOS or chipset compatibility issue")

        print("\nRecommended action:")
        print("- Roll back or uninstall the recent driver")
        print("- Remove or test recently installed hardware")
        print("- Uninstall the latest Windows update if needed")
        print("- Update chipset and motherboard drivers")
        print("- Check the BSOD stop code for more details")

    elif answer == "no":
        second_answer = input(
            "Does the blue screen happen randomly during normal use or gaming? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- Unstable or faulty RAM")
            print("- CPU or GPU overheating")
            print("- Storage drive errors")
            print("- Power supply instability")
            print("- Corrupted system files")

            print("\nRecommended action:")
            print("- Run a memory diagnostic test")
            print("- Check CPU and GPU temperatures")
            print("- Check SSD or HDD health")
            print("- Run Windows system file repair tools")
            print("- Check Windows Event Viewer")
            print("- Record the BSOD stop code")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Record the exact BSOD stop code")
            print("- Check Device Manager for driver problems")
            print("- Install pending Windows updates")
            print("- Scan for malware")
            print("- Check system logs for errors")

        else:
            print("\nInvalid answer. Please enter yes or no.")

    else:
        print("\nInvalid answer. Please enter yes or no.")

def storage_drive_troubleshooting():
    print("\n--- Storage Drive Problems ---")

    answer = input(
        "Is the storage drive missing from Windows or BIOS? (yes/no): "
    ).lower()

    if answer == "yes":
        print("\nPossible causes:")
        print("- Loose SATA or power cable")
        print("- Drive not seated correctly")
        print("- Failed SSD or HDD")
        print("- Disabled storage controller")
        print("- Incorrect BIOS configuration")

        print("\nRecommended action:")
        print("- Check SATA and power connections")
        print("- Reseat the drive if applicable")
        print("- Check if the drive appears in BIOS")
        print("- Try another SATA port or cable")
        print("- Test the drive in another system if possible")

    elif answer == "no":
        second_answer = input(
            "Is the drive very slow, freezing, or making unusual noises? (yes/no): "
        ).lower()

        if second_answer == "yes":
            print("\nPossible causes:")
            print("- Failing HDD or SSD")
            print("- File system errors")
            print("- Low free storage")
            print("- High disk usage")
            print("- Bad sectors or drive wear")

            print("\nRecommended action:")
            print("- Back up important files immediately")
            print("- Check drive health and SMART status")
            print("- Check Task Manager for high disk usage")
            print("- Run file system diagnostics")
            print("- Replace the drive if health warnings appear")

        elif second_answer == "no":
            print("\nRecommended checks:")
            print("- Check available disk space")
            print("- Review Disk Management")
            print("- Check for Windows storage errors")
            print("- Update storage controller drivers")
            print("- Restart the system and test again")

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
        print("4. Overheating")
        print("5. Slow Performance")
        print("6. Boot / Windows Startup Problems")
        print("7. BSOD / Blue Screen")
        print("8. Storage Drive Problems")
        print("9. Exit")
        choice = input("\nSelect a problem: ")

        if choice == "1":
            no_power_troubleshooting()
        elif choice == "2":
           no_display_troubleshooting()
        elif choice == "3":
           random_shutdown_troubleshooting()
        elif choice == "4":
           overheating_troubleshooting()
        elif choice == "5":
           slow_performance_troubleshooting()
        elif choice == "6":
           boot_startup_troubleshooting()
        elif choice == "7":
           bsod_troubleshooting()
        elif choice == "8":
          storage_drive_troubleshooting()
        elif choice == "9":
          print("\nExiting PC Troubleshooting Tool...")
          break
        else:
          print("\nInvalid option. Please select 1-9.")


if __name__ == "__main__":
    main()
