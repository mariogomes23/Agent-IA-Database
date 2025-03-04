import os 
import streamlit as st
from dotenv import load_dotenv
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import create_sql_agent 
from langchain.schema import SystemMessage,HumanMessage


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")
db_uri =os.getenv("DB_URI")

def get_agent():
    if "agent" not in st.session_state:
        db = SQLDatabase.from_uri(db_uri)
        llm = ChatOpenAI(model = model_name,openai_api_key=api_key)
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        memory = ConversationBufferMemory(return_messages=True)
        agent = create_sql_agent(llm=llm,toolkit=toolkit,memory=memory,verbose=True)
        st.session_state.agent = agent
    return st.session_state.agent



def main():
    st.title("Assistente de Banco de Dados 🤖")
    agent = get_agent()
    
    if agent.memory and hasattr(agent.memory, 'chat_memory'):
        agent.memory.chat_memory.add_message(SystemMessage(content="Você é um assistente que fala apenas português."))
           
    with st.sidebar:
        st.header("Histórico")
        if agent.memory and hasattr(agent.memory, 'chat_memory'): 
           for msg in agent.memory.chat_memory.messages:
               st.text(f"{msg.type}: {msg.content}")
    
    user_input = st.text_input("digite a sua pergunta ou a  instrução ")
    if st.button("Enviar"):
         with st.spinner("Pensando..."):
              if agent.memory and hasattr(agent.memory, 'chat_memory'):
                   agent.memory.chat_memory.add_message(HumanMessage(content=user_input))
              response = agent.run(user_input)
         st.success("Reposta do agente")
         st.write(response)  
    
        
      

if __name__ == "__main__":
    main()

        
        
    