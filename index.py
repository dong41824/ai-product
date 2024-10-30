import streamlit as st
st.title("AI大模型应用产品网")
col, col1 = st.columns(2)
with col:
    st.image("https://tse1-mm.cn.bing.net/th/id/OIP-C.h9dmt0VA30NmskyQaDDm7wHaFj?w=230&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7,width=300")
    flag = st.button("问答系统")
    if flag:
        st.switch_page("pages/demo03.py")
with col1:
    st.image("https://tse1-mm.cn.bing.net/th/id/OIP-C.h9dmt0VA30NmskyQaDDm7wHaFj?w=230&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7,width=300")
    flag1 = st.button("生图系统")
    if flag1:
        st.switch_page("pages/textToImage.py")
# c1,c2,c3,c4,c5=st.columns(5)
# with c1:
#     flag = st.button("小白版")
#     if flag:
#         st.switch_page("pages/demo,py")
# with c2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo01,py")
# with c3:
#     flag2 = st.button("进阶版1")
#     if flag2:
#         st.switch_page("pages/demo02,py")
# with c4:
#     flag3 = st.button("最终版")
#     if flag3:
#         st.switch_page("pages/demo03,py")
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textToImage,py")