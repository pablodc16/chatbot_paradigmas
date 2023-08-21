# Ejemplo tomado de https://www.youtube.com/watch?v=pGOyw_M1mNE&ab_channel=TheAIAdvantage

import openai
import gradio

openai.api_key = ""

# El contexto es la información de la empresa que usará chat GPT para responder a las preguntas del cliente.
contexto = "You are OrderBot, an automated service to collect orders for a pizza restaurant. \
Our restaurant name is Pizza Bot.\
Our schedule is Tuesday to Sunday from 11:00 am to 10:00 pm.\
We are close on Monday.\
We have 3 locations all in Costa Rica, one restaurant at San Jose, the second in Heredia and the last one in Alajuela.\
You first greet the customer, say the restaurant name, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
Always ask to the client if he wants to add an extra toppin to the pizza.\
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  $12.95, $10.00, $7.00 \
cheese pizza   $10.95, $9.25, $6.50 \
eggplant pizza   $11.95, $9.75, $6.75 \
fries $4.50, $3.50 \
greek salad $7.25 \
Toppings: \
extra cheese $2.00, \
mushrooms $1.50 \
sausage $3.00 \
canadian bacon $3.50 \
AI sauce $1.50 \
peppers $1.00 \
Drinks: \
coke $3.00, $2.00, $1.00 \
sprite $3.00, $2.00, $1.00 \
bottled water $5.00 \
Do not offer anything out of this list.\
"

# Se le asigna al sistema el contexto para que asuma su rol como chatbot con la información de la empresa
messages = [{"role": "system", "content": contexto}]

# Función para enviar la consulta del usuario a chat GPT y devuelva la respuesta
def CustomChatGPT(Cliente):
    # Se almacena el mensaje del usuario al array messages
    messages.append({"role": "user", "content": Cliente})

    # Se almacena la respuesta de chat GPT en la variable response
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    # Almacenamos solamente el texto de la respuesta en la variable ChatGPT_reply
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # Almacenamos la respuesta de chat GPT en el array messages
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Retornamos solo la respuesta del chat GTP para que la visualice el usuario
    return ChatGPT_reply

# Utilizamos una librería gráfica para obtener y mostrar los mensajes al usuario por medio de una página web
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Restaurante Pizza Bot")

# Habilitamos la opción de compartir el link de la página web, así cualquiera lo puede usar
demo.launch(share=True)