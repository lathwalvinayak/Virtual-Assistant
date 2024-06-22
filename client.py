from openai import OpenAI


# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Your Api Key",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Virtual Assistant named Jarvis skilled in general tasks like Google assistant and Alexa"},
    {"role": "user", "content": "founder of python"}
  ]
)

print(completion.choices[0].message.content)