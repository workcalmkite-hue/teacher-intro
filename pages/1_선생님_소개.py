import streamlit as st

st.set_page_config(page_title="선생님 소개", page_icon="👩‍💻", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.info-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 20px 24px;
    margin: 8px 0;
}
.role-card {
    background: rgba(168,85,247,0.07);
    border-left: 4px solid #a855f7;
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

st.title("👩‍💻 선생님 소개")
st.markdown("---")

# ── 기본 정보
st.markdown("### 📋 기본 정보")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
      🏫 <strong>학교</strong><br>방배중학교
    </div>
    <div class="info-card">
      📚 <strong>담당 교과</strong><br>기술
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
      👥 <strong>담당 학년</strong><br>1학년, 3학년
    </div>
    <div class="info-card">
      💡 <strong>전문 분야</strong><br>AI 교육, 바이브코딩
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ── 하는 일
st.markdown("### 💼 선생님이 하는 일들")

roles = [
    ("🤖", "AI 선도교사단", "전국 AI 교육을 함께 만들어가는 교사 그룹이에요."),
    ("🌱", "디지털 새싹 주강사", "여러분처럼 학생들에게 코딩을 가르치는 강사예요."),
    ("🔬", "AI 미래교육연구회 운영진", "선생님들끼리 AI 교육을 연구하는 모임을 운영해요."),
    ("⚙️", "AI업무자동화 분과장", "AI로 반복 업무를 자동화하는 방법을 연구해요."),
    ("💻", "바이브코딩 강사", "AI와 함께 빠르게 코딩하는 방법을 가르쳐요."),
    ("🏫", "찾아가는 학교 컨설팅", "다른 학교에 찾아가서 AI 교육을 도와줘요."),
    ("🎓", "AIEDAP 선도교사", "교육부 AI 디지털 선도 교사로 활동해요."),
    ("📡", "SEN 선도교사", "스마트 교육 네트워크 선도 교사예요."),
]

for icon, title, desc in roles:
    st.markdown(f"""
    <div class="role-card">
      <strong>{icon} {title}</strong><br>
      <span style="color:#aaa; font-size:0.9rem;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)
