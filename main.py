while True:
    answer = input("Want to play rock, paper, scissors? y/n: ")
    if answer.lower() != "y" and answer.lower() != "n":
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

    elif answer.lower() == "n":
        print("Thanks for playing!")
        break
    elif answer.lower() == "y":
        while True:
            user_choice = input("Enter your choice (r/p/s): ")
            if user_choice.lower() not in ["r", "p", "s"]:
                print("Invalid choice. Please choose r, p or s next time.")
                continue
            else:
                import random

                choices = ["r", "p", "s"]
                computer_choice = random.choice(choices)
                print(f"Computer chose: {computer_choice}")
                if user_choice == computer_choice:
                    print("It's a tie!")
                    break
                elif (
                    computer_choice == "r"
                    and user_choice == "s"
                    or computer_choice == "s"
                    and user_choice == "p"
                    or computer_choice == "p"
                    and user_choice == "r"
                ):
                    print("Computer wins!")
                    break
                elif (
                    computer_choice == "p"
                    and user_choice == "r"
                    or computer_choice == "s"
                    and user_choice == "r"
                    or computer_choice == "r"
                    and user_choice == "p"
                ):
                    print("You win!")
                    break
    elif answer.lower() == "n":
        print("Thanks for playing!")
        break
