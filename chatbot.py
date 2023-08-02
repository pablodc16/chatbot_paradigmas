# Ejemplo tomado de https://www.youtube.com/watch?v=pGOyw_M1mNE&ab_channel=TheAIAdvantage

import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)