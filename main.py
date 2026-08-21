from groq import Groq
from dotenv import load_dotenv
from vector import Vector
load_dotenv()

messages=Vector()

client=Groq()

chat_completion=client.chat.completions.create(
messages=[
{
 "role":"system",
 "content":"You are assistant your job is to read the question of user and then relevant chunks  of answers would be given to you and you have to answer the question of user using that chunks "
},{
    "role":"user",
    "content":"what is the shape of the earth"

},{
    "role":"assistant",
    "content":messages
}
],




model="openai/gpt-oss-120b",
)
print(chat_completion.choices[0].message.content)