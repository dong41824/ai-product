import streamlit as st
from zhipuai import ZhipuAI

model = ZhipuAI(api_key="468938ac8691508a3879e5b059f5ab7f.tgSCW7ofE4LIzw4R")
st.title("设计大师")
# 初始化缓存列表，如果尚未存在
if "cache" not in st.session_state:
    st.session_state.cache = []

desc = st.chat_input("请输入图片描述")
if desc:
    with st.chat_message("user"):
        st.write(desc)
    response = model.images.generations(
        model="cogview-3-plus", # 填写需要调用的模型编码
        prompt=desc
    )
    image_url = response.data[0].url
    with st.chat_message("assistant"):
        st.image(image_url, width=300)
        # 将对话记录添加到缓存中
        st.session_state.cache.append({"role": "user", "content": desc})
        st.session_state.cache.append({"role": "assistant", "content": image_url})

    # 如果历史记录存在，显示历史记录
    if st.session_state.cache:
        for message in st.session_state.cache:
            if message['role'] == 'user':
                with st.chat_message("user"):
                    st.write(message["content"])
            elif message['role'] == 'assistant':
                with st.chat_message("assistant"):
                    st.image(message["content"], width=300)
# desc = st.chat_input("请输入图片描述")
# if desc:
#     with st.chat_message("user"):
#         st.write(desc)
#
# response = model.images.generations(
#     model="cogview-3-plus",  # 填写需要调用的模型编码
#     prompt="desc"
# )
# with st.chat_message("assistant"):
#     st.image(response.data[0].url,width=300)
#     st.session_state.cache.append({"role": "assistant", "content": result['data[0].url']})
