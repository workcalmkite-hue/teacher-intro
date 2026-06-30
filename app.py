import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="안정연 선생님",
    page_icon="👩‍💻",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.avatar {
    font-size: 5rem;
    display: block;
    text-align: center;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.name {
    font-size: 2.4rem;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #e94560, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0.4rem 0 0.2rem;
}
.sub { text-align: center; color: #888; font-size: 1rem; }
.badge-row {
    display: flex; flex-wrap: wrap; gap: 8px;
    justify-content: center; margin: 1.2rem 0;
}
.badge {
    padding: 5px 14px; border-radius: 999px;
    font-size: 0.82rem; font-weight: 600;
}
.b-purple { background: rgba(168,85,247,0.2); color: #c084fc; border: 1px solid rgba(168,85,247,0.4); }
.b-pink   { background: rgba(233,69,96,0.2);  color: #f87171; border: 1px solid rgba(233,69,96,0.4); }
.b-blue   { background: rgba(59,130,246,0.2);  color: #93c5fd; border: 1px solid rgba(59,130,246,0.4); }
.b-green  { background: rgba(34,197,94,0.2);   color: #86efac; border: 1px solid rgba(34,197,94,0.4); }
.b-yellow { background: rgba(234,179,8,0.2);   color: #fde047; border: 1px solid rgba(234,179,8,0.4); }
</style>
""", unsafe_allow_html=True)

# ── 헤더
st.markdown('<span class="avatar">👩‍💻</span>', unsafe_allow_html=True)
st.markdown('<div class="name">안정연 선생님</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">방배중학교 · 기술 교과</div>', unsafe_allow_html=True)

st.markdown("""
<div class="badge-row">
  <span class="badge b-pink">🏆 2025 교육력 제고 우수교원 표창</span>
</div>
""", unsafe_allow_html=True)

# ── 한 줄 소개
st.markdown("---")
st.markdown("""
> **AI**랑 **코딩**으로 세상을 탐험하는 기술 선생님.
> 수업에서 여러분이 **"나도 만들 수 있겠는데?"** 라고 느끼는 순간을 제일 좋아해요.
""")

# ── 활동 배지
st.markdown("""
<div class="badge-row">
  <span class="badge b-purple">AI 선도교사단</span>
  <span class="badge b-pink">디지털 새싹 주강사</span>
  <span class="badge b-blue">AI 미래교육연구회</span>
  <span class="badge b-green">AI업무자동화 분과장</span>
  <span class="badge b-yellow">바이브코딩 강사</span>
  <span class="badge b-purple">AIEDAP 선도교사</span>
  <span class="badge b-blue">SEN 선도교사</span>
</div>
""", unsafe_allow_html=True)

# ── 테마곡
st.markdown("---")
st.markdown("### 🎵 선생님의 테마곡")
st.markdown("**어른이 되어버렸다** — 원필")
components.html("""
<iframe width="100%" height="200"
  src="https://www.youtube.com/embed/qE5y9eh_PCA"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen style="border-radius:12px;">
</iframe>
""", height=215)

st.markdown("---")
st.caption("👈 왼쪽 메뉴에서 더 많은 정보를 확인하세요!")
