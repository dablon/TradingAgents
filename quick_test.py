import os
os.chdir('/app')
os.environ['OPENAI_API_KEY'] = 'sk-cp-gyQ8LLTK3s9rOTDEz7sWckbIVCBFAjI18o7Z5qyOupBaddCTY0OZxepVqbqdL5RSOJrDPrqv2RrbU83Ij4Qk8-gahr3cSRsg5ls4UkygsoTu4nK2RCAihXo'

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "minimax"
config["deep_think_llm"] = "minimax-m2.7"
config["quick_think_llm"] = "minimax-m2.7"

print("Testing with AAPL...")
ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("AAPL", "2026-01-15")
print("Decision:", decision)
