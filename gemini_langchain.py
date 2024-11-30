import os
from dotenv import load_dotenv
import mesop as me
import mesop.labs as mel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# 加載 .env 檔案中的環境變數
load_dotenv()

# 建立聊天模型實例
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.5,
    top_p=0.90,
    top_k=65,
    max_output_tokens=8192,
    streaming=True,
    api_key=os.environ["GEMINI_API_KEY"]
)

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/",
    title="Mesop Demo Chat - Gemini via Langchain",
)
def page():
    mel.chat(transform, title="Gemini Chat", bot_user="Mesop Bot")

def transform(input_text: str, history: list[mel.ChatMessage]):
    # 將聊天歷史轉換為模型可處理的格式
    chat_history = [HumanMessage(content=msg.content) for msg in history]
    # 加入當前使用者輸入
    chat_history.append(HumanMessage(content=input_text))
    # 生成回應
    for chunk in chat_model.stream(chat_history):
        yield chunk.content

