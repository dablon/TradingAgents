# TradingAgents - Deploy Script

## Prerequisites
- Docker installed on the server
- Minimax API key

## Setup on OVH2

1. **Connect to your server:**
```bash
ssh root@142.44.247.203
```

2. **Clone the repository:**
```bash
git clone https://github.com/dablon/TradingAgents.git
cd TradingAgents
```

3. **Configure your API key:**
```bash
cp .env.example.minimax .env
nano .env
# Replace YOUR_MINIMAX_API_KEY_HERE with your actual Minimax API key
```

4. **Build and run with Docker:**
```bash
docker-compose up -d
```

5. **Attach to the CLI:**
```bash
docker attach tradingagents
```

## Manual Setup (without Docker)

```bash
# Create virtual environment
conda create -n tradingagents python=3.13
conda activate tradingagents

# Install
pip install .

# Run
tradingagents
```

## Configuration

Edit the `.env` file:
- `OPENAI_API_KEY` - Your Minimax API key
- `llm_provider` - Use "openai" for Minimax
- `backend_url` - Minimax API endpoint (usually https://api.minimax.chat/v1)
- `deep_think_llm` - Model for complex reasoning
- `quick_think_llm` - Model for quick tasks

## Troubleshooting

If Minimax doesn't work, try:
- Check if the API endpoint is correct
- Verify your API key is valid
- Try using OpenAI as provider instead
