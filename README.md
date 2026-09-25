# 🚉 Jev Train Station Assistant

A small Python experiment built with Jev and Noul to explore how natural-language input can be turned into simple decisions.

The project simulates a train station information desk that asks a visitor whether they have lost something and routes them accordingly.

> Built as a small hands-on project to understand Jev, Noul, confidence scores, and practical Python scripting.

## ✨ What It Does

The assistant asks:

"Did you lose something?"

Instead of requiring the user to answer with only Y or N, the Jev-powered version can interpret natural-language responses.

For example:

"Yeah, I think I lost my wallet."

The system evaluates the response and produces a confidence score between 0 and 1.

The score is then used to make a simple decision:

- Confidence > 0.8 → Yes
- Confidence < 0.2 → No
- Confidence between 0.2 and 0.8 → Uncertain, so the assistant asks again

## 🧠 What I Learned

This project helped me understand a few concepts by actually building something rather than just reading about them:

- Basic Python functions
- while loops
- if conditions
- return statements
- User input
- Environment variables
- API clients
- Natural-language classification
- Confidence scores
- Using Noul to obtain a scored decision
- Building a small Python project from scratch

More importantly, it showed me that small projects can make Python syntax much easier to understand and remember.

## 🏗️ Project Structure

jev-train-station-assistant/
│
├── main.py
├── jev_noul.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env.example
├── .gitignore
└── README.md

### main.py

The main Jev-powered implementation.

It:

1. Takes user input.
2. Sends the response through the Jev/TypeSafe client.
3. Uses Noul to determine whether the response is affirmative.
4. Converts the confidence score into a boolean decision.
5. Routes the visitor.

### jev_noul.py

A simpler version of the same idea without Jev.

Instead of interpreting natural language, it expects:

Y
N

This version was useful as a starting point for understanding the basic Python logic before introducing Jev.

## 🔄 How It Works

User
  ↓
"Did you lose something?"
  ↓
Natural-language input
  ↓
Jev
  ↓
Noul
  ↓
Confidence score (0 → 1)
  ↓
┌───────────────┬───────────────┐
│               │               │
> 0.8         0.2 - 0.8        < 0.2
│               │               │
YES          UNCERTAIN          NO
│               │               │
│          Ask again            │
└───────────────┴───────────────┘
                ↓
        Station response

## ⚙️ Requirements

- Python 3.13+
- uv
- A valid OpenRouter API key
- Jev / typesafe-sdk

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/jev-train-station-assistant.git

cd jev-train-station-assistant

### 2. Install dependencies

uv sync

### 3. Create your environment file

Copy .env.example to .env.

Add your API key:

OPENROUTER_API_KEY=your_api_key_here

Never commit your .env file to GitHub.

### 4. Run the program

uv run main.py

## 💬 Example

Did you lose something?

> Yeah, I think I lost my wallet.

The assistant interprets the response and routes the visitor:

"You can find the lost and found counter on the right."

If the response is unclear:

Did you lose something?

> Maybe...

"Sorry, I didn't get that."

The assistant asks again.

## 🧪 The Simple Version

Before using Jev, the same idea can be implemented using basic Python:

def ask():
    while True:
        answer = input("Did you lose something? (Y/N)")

        if answer == "Y":
            return True

        if answer == "N":
            return False

        print("Please answer with Y or N")

This is intentionally simple.

The goal was to start with ordinary Python logic and then introduce Jev to make the interaction more flexible.

## 🎯 Why I Built This

This isn't meant to be a production-ready train station assistant.

It's a small learning project.

The goal was to take something I learned about Jev and turn it into an actual Python program that I could run, modify, break, and understand.

Sometimes a small project teaches more than another hour of watching tutorials.

## 🛠️ Tech Stack

- Python
- Jev
- Noul
- TypeSafe SDK
- OpenRouter
- python-dotenv
- uv

## 📌 What's Next?

Possible improvements:

- Add more train-station queries.
- Handle directions around the station.
- Add ticket-related questions.
- Create multiple decision routes.
- Improve natural-language handling.
- Turn the CLI program into a small web application.

For now, the goal is simple:

> Build small. Learn something. Build again.

## 👨‍💻 Learning Project

Built as part of my journey to become better at Python through small, practical projects.

One small script at a time. 🚀
