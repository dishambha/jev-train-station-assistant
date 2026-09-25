import os
from pathlib import Path

from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise SystemExit(
        "Missing OPENROUTER_API_KEY. Create a .env file in the project root with: OPENROUTER_API_KEY=your_key_here"
    )

client = TypeSafeClient(
    api_key=api_key,
    base_url="https://openrouter.ai/api",
)


def respond(lost_something):
    if lost_something:
        print("You can find the lost and found counter on the right.")
    else:
        print("What can i help you with?")


def ask():
    while True:
        answer = input("Did you lose something? ")
        r = client.system_one(
            state=f"{answer}",
            questions={
                "lost_something": Noul(
                    instructions="is this answer from user affirmative or not?"
                ),
            },
        )
        lost_something = r.answers["lost_something"].noul
        if lost_something > 0.8:
            return True
        if lost_something < 0.2:
            return False
        print("Sorry, I didn't get that.")


def main():
    lost_something = ask()
    respond(lost_something)


if __name__ == "__main__":
    main()
