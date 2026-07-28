import random


def play_game():
    print("=" * 40)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("=" * 40)

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 20

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number}!")
                print(f"You guessed it in {attempts} attempt(s).")
                return

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    print("\n😢 Game Over!")
    print(f"The correct number was {secret_number}.")


def main():
    while True:
        play_game()

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again not in ["yes", "y"]:
            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()