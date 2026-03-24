import sys
sys.path.insert(0, '/app')

from tradingagents.llm_clients.openai_client import OpenAIClient

client = OpenAIClient(
    model='miniMax-Text-01',
    base_url='https://api.minimax.io/v1',
    provider='openai',
    api_key='sk-cp-gyQ8LLTK3s9rOTDEz7sWckbIVCBFAjI18o7Z5qyOupBaddCTY0OZxepVqbqdL5RSOJrDPrqv2RrbU83Ij4Qk8-gahr3cSRsg5ls4UkygsoTu4nK2RCAihXo'
)

print('Testing API...')
result = client.invoke('Say hello in one word')
print('Response:', result)
