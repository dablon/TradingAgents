import os
import sys
from datetime import datetime

os.environ['OPENAI_API_KEY'] = 'sk-cp-gyQ8LLTK3s9rOTDEz7sWckbIVCBFAjI18o7Z5qyOupBaddCTY0OZxepVqbqdL5RSOJrDPrqv2RrbU83Ij4Qk8-gahr3cSRsg5ls4UkygsoTu4nK2RCAihXo'
os.environ['backend_url'] = 'https://api.minimax.io/v1'

sys.path.insert(0, '/home/nalcaraz/TradingAgents')

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config['llm_provider'] = 'openai'
config['deep_think_llm'] = 'miniMax-Text-01'
config['quick_think_llm'] = 'miniMax-Text-01'
config['backend_url'] = 'https://api.minimax.io/v1'

tickers = ['BTC', 'ETH', 'NVDA']
start_date = '2026-01-15'

print('=' * 60)
print('TradingAgents Simulation - MiniMax LLM')
print('=' * 60)
print(f'Starting at: {datetime.now()}')
print(f'Tickers: {tickers}')
print()

results = []
for ticker in tickers:
    print(f'Running {ticker}...')
    try:
        ta = TradingAgentsGraph(debug=False, config=config)
        _, decision = ta.propagate(ticker, start_date)
        print(f'  Decision: {decision[:150]}...' if len(decision) > 150 else f'  Decision: {decision}')
        results.append({'ticker': ticker, 'status': 'success', 'decision': decision})
        print(f'  ✅ {ticker} - SUCCESS')
    except Exception as e:
        print(f'  ❌ {ticker} - Error: {str(e)[:100]}')
        results.append({'ticker': ticker, 'status': 'error', 'error': str(e)})
    print()

print('=' * 60)
print('SIMULATION COMPLETE')
print('=' * 60)
print(f'Finished at: {datetime.now()}')
for r in results:
    if r['status'] == 'success':
        print(f"✅ {r['ticker']}: SUCCESS")
    else:
        print(f"❌ {r['ticker']}: {r['error'][:80]}")
