import openai
import config

openai.api_key = config.api_key
messages = [
        {"role": "system", "content": "Eres un asistente muy útil"},
      
    ]

response = openai.ChatCompletion.create( model="gpt-3.5-turbo",
                              messages= messages)
while True:

  content = input("¿Sobre que quieres hablar?")
  if content == 'exit':
   break
  
  messages.append({"role":"user","content":content})
  response = openai.ChatCompletion.create( model="gpt-3.5-turbo",
                                messages= messages)
  
  response_content = response.choices[0].message.content
  messages.append({"role":"assistant","content": response_content})
  print(response_content)
  