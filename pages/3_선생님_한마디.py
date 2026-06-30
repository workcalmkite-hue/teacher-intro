import streamlit as st
import random

st.set_page_config(page_title="선생님의 한마디", page_icon="💬", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.msg-box {
    background: rgba(168,85,247,0.1);
    border: 1px solid rgba(168,85,247,0.3);
    border-radius: 20px;
    padding: 36px 28px;
    text-align: center;
    font-size: 1.15rem;
    line-height: 1.85;
    color: #e2e8f0;
    margin: 1.5rem 0;
    min-height: 130px;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 선생님의 한마디")
st.markdown("버튼을 눌러 선생님의 메시지를 받아보세요!")
st.markdown("---")

messages = [
    "코딩은 영어나 수학처럼 하나의 언어예요. 처음엔 낯설어도 쓰다 보면 익숙해져요. 🧩",
    "AI가 세상을 바꾸고 있어요. 여러분이 그 AI를 쓰는 사람이 됐으면 좋겠어요. 🤖",
    "선생님도 처음엔 코드가 하나도 안 됐어요. 지금 여러분이랑 똑같았어요. 😅",
    "에러 메시지를 읽는 사람이 진짜 개발자예요. 영어 무서워하지 마세요! 🔍",
    "오늘 배운 것 하나만 기억하고 가도 충분해요. 내일 또 하나 추가하면 돼요. ✨",
    "여러분이 만든 작품에 선생님이 제일 신나요. 꼭 보여주세요! 🙌",
    "기술은 '어떻게 쓰느냐'가 전부예요. 도구를 잘 다루는 사람이 되세요. 🛠️",
    "메모장 하나로 이렇게 만들 수 있어요. 앞으로 뭘 또 만들 수 있을지 기대되지 않아요? 🚀",
    "완성 못 해도 괜찮아요. 시작한 것만으로도 대단해요. 💪",
    "막히면 선생님한테 오세요. 같이 해결하는 게 수업이에요. 😊",
]

if "msg_idx" not in st.session_state:
    st.session_state.msg_idx = random.randint(0, len(messages) - 1)

st.markdown(f'<div class="msg-box">{messages[st.session_state.msg_idx]}</div>', unsafe_allow_html=True)

if st.button("🎲 다음 메시지", use_container_width=True, type="primary"):
    new_idx = st.session_state.msg_idx
    while new_idx == st.session_state.msg_idx:
        new_idx = random.randint(0, len(messages) - 1)
    st.session_state.msg_idx = new_idx
    st.rerun()

st.markdown("---")
st.caption("메시지는 총 10개예요. 다 눌러봐요!")
