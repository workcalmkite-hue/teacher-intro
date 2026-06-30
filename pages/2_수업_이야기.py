import streamlit as st

st.set_page_config(page_title="수업 이야기", page_icon="📝", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.rule-card {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: #f8f4ff;
    border: 1px solid #d8b4fe;
    border-radius: 14px;
    padding: 18px 20px;
    margin: 10px 0;
}
.rule-num {
    width: 32px; height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, #a855f7, #e94560);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; font-weight: 800; color: white;
    flex-shrink: 0;
}
.class-card {
    background: #f0faff;
    border-left: 4px solid #0ea5e9;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("📝 수업 이야기")
st.markdown("---")

# ── 수업 철학
st.markdown("### 💡 선생님이 수업에서 중요하게 생각하는 것")

rules = [
    ("틀려도 괜찮아요", "오답이 정답보다 더 많이 배울 수 있어요. 틀리는 걸 두려워하지 마세요."),
    ("모르면 손 들기", "같은 질문을 가진 친구가 꼭 있어요. 질문은 용감한 거예요."),
    ("만든 것 자랑하기", "작동하면 옆 친구한테 보여주세요. 자랑해도 됩니다!"),
    ("검색은 능력이에요", "구글링, AI 활용 — 다 환영합니다. 잘 찾는 것도 실력이에요."),
    ("내 것으로 만들기", "수업에서 만든 것은 여러분 것입니다. 집에서도 써보세요."),
]

for i, (title, desc) in enumerate(rules, 1):
    st.markdown(f"""
    <div class="rule-card">
      <div class="rule-num">{i}</div>
      <div>
        <strong style="color:#1e1b4b;">{title}</strong><br>
        <span style="color:#4b5563; font-size:0.9rem;">{desc}</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ── 이번 수업 소개
st.markdown("### 🌱 이번 수업: 디지털 새싹 바이브코딩")
st.markdown("""
<div class="class-card">
  <strong style="color:#0369a1;">바이브코딩</strong>이란?<br>
  <span style="color:#374151;">AI와 함께 내가 원하는 것을 직접 만들어보는 코딩 방식이에요.<br>
  코드를 외우지 않아도 돼요. 아이디어만 있으면 됩니다!</span>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **1차시 (금요일)**
    - 메모장으로 .bat 파일 만들기
    - 메모장으로 .html 파일 만들기
    - GitHub & Streamlit 회원가입
    """)
with col2:
    st.markdown("""
    **2차시 (토요일)**
    - GitHub에 코드 올리기
    - Streamlit으로 내 사이트 배포
    - 나만의 웹 서비스 완성!
    """)
