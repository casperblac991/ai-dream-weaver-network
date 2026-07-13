# ai-dream-weaver-network 🚀

Autonomous AI-powered digital products store, fully automated using GitHub Actions and Gumroad API for passive income.

## Features
- **AI Idea Generation**: Uses OpenAI's GPT-4o to brainstorm and create unique digital product concepts.
- **Automated Listing**: Automatically creates products on Gumroad with descriptions and pricing.
- **Scheduled Execution**: Runs periodically via GitHub Actions to keep the store fresh.

## Setup
1. Fork this repository.
2. Add your secrets to GitHub Actions:
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `GUMROAD_ACCESS_TOKEN`: Your Gumroad Access Token.
3. Enable GitHub Actions in the "Actions" tab.

## Structure
- `bots/product_bot.py`: The core logic for generation and publishing.
- `.github/workflows/main.yml`: The automation pipeline.
