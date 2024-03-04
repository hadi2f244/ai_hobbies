from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/mixtral-8x7b-32768" # Tells OI to send messages in OpenAI's format
#interpreter.llm.model = "openai/llama2-70b-4096" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "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" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "https://api.groq.com/openai/v1" # Point this at any OpenAI compatible server
#create a k8s cluster use kind. I have the command installed. 
interpreter.chat()
