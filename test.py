# Mentor Bot

import openai
openai.api_key = "sk-MICsuHUrAH9yEUE1JPfkttn0dNTIGZwSsVh604Fq"

response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)