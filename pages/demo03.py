'''
制作一个带有自定义觉得的大模型应用
1.大模型对象
2.提示词对象
3.链chain
使用流程：首先需要构建一个大模型对象，然后创建一个提示词对象，然后使用langchain中的chain链将大模型对象
和提示词对象组合起来，此时回答问题使用链来回答
'''

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="468938ac8691508a3879e5b059f5ab7f.tgSCW7ofE4LIzw4R",
)
if "memery" not in st.session_state:
    st.session_state.memery = ConversationBufferMemory(memory_key = "history")
prompt = PromptTemplate.from_template("你的名字叫MuMu，你是一只家养的可爱猫咪，你现在2岁了，你可爱粘人，生活在一个有爱的家庭，你会回答主人的问题，只对问题作出回应，主人的的问题是{input}，你和你主人的历史对话为{history}")

chain = LL_chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memery
)

st.title("你怎么才回来呀！❀❀❀")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
problem = st.chat_input("请输入你的问题")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role":"user","content":problem})
    result = chain.invoke({"input":problem})
    with st.chat_message("assistant"):
        st.write(result['text'])
        st.session_state.cache.append({"role":"assistant","content":result['text']})