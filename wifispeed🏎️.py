import speedtest

def convert_bytes_to_speed(size_bytes, unit):
    if unit.lower() == 'm':
        # Convert bytes to megabits per second (Mbps)
        speed = size_bytes / 1024 / 1024
        unit_str = "Mbps"
    elif unit.lower() == 'g':
        # Convert bytes to gigabits per second (Gbps)
        speed = size_bytes / 1024 / 1024 / 1024 * 8  # Convert to bits and then to Gbps
        unit_str = "Gbps"
    else:
        return "Invalid unit"
    
    return f"{speed:.2f} {unit_str}"

def run_speed_test(unit):
    wifi = speedtest.Speedtest()
    print("Testing download speed...")
    download_speed = wifi.download()

    print("Testing upload speed...")
    upload_speed = wifi.upload()

    print(f"Download Speed: {convert_bytes_to_speed(download_speed, unit)}")
    print(f"Upload Speed:   {convert_bytes_to_speed(upload_speed, unit)}")

def main():
    while True:
        ask_user = input("Welcome to the WiFi speed tester. Enter 'm' for megabytes per second or 'g' for gigabits per second: ").lower()

        if ask_user not in ['m', 'g']:
            print("Invalid input. Please enter 'm' for megabytes or 'g' for gigabits.")
            continue
        
        run_speed_test(ask_user)

        final_input = input("Do you want to test again? (y/n): ").lower()
        if final_input != "y":
            print("Thank you for using the WiFi speed tester. Have a great day! 😊")
            break

if __name__ == "__main__":
    main()
