from services.command_line import CommandLine


def main():
    processor = CommandLine()
    file_path = "sample_input/input2.txt"
    with open(file_path, "r") as file:
        for line in file:
            commands = line.strip().split()
            if not commands:
                continue
            command = commands[0]
            if command == "START_SUBSCRIPTION":
                result = processor.validate_date(commands[1])
                if result:
                    print(result)
            elif command == "ADD_SUBSCRIPTION":
                result = processor.add_subscription(commands[1], commands[2])
                if result:
                    print(result)
            elif command == "ADD_TOPUP":
                result = processor.add_topup(commands[1], int(commands[2]))
                if result:
                    print(result)
            elif command == "PRINT_RENEWAL_DETAILS":
                print(processor.calculate_renewal_details())


if __name__ == "__main__":
    main()
