import os
import sys
os.chdir('/home/nalcaraz/TradingAgents')
os.environ['OPENAI_API_KEY'] = 'sk-cp-gyQ8LLTK3s9rOTDEz7sWckbIVCBFAjI18o7Z5qyOupBaddCTY0OZxepVqbqdL5RSOJrDPrqv2RrbU83Ij4Qk8-gahr3cSRsg5ls4UkygsoTu4nK2RCAihXo'

sys.path.insert(0, '/home/nalcaraz/TradingAgents')

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config['llm_provider'] = 'openai'
config['deep_think_llm'] = 'miniMax-Text-01'
config['quick_think_llm'] = 'miniMax-Text-01'
config['backend_url'] = 'https://api.minimax.io/v1'

print('Starting TradingAgents with MiniMax...')
print('=' * 60)

tickers = ['BTC/USDT', 'ETH/USDT']
start = '2026-01-15'

for ticker in tickers:
    print(f'Running {ticker}...')
    sys.stdout.flush()
    try:
        ta = TradingAgentsGraph(debug=False, config=config)
        _, decision = ta.propagate(ticker, start)
        print(f'SUCCESS: {decision[:200]}')
    except Exception as e:
        print(f'ERROR: {str(e)[:100]}')
    print()

print('Done')
