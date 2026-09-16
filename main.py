import streamlit as st
import random

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI 여행 처방전 💌",
    page_icon="🌷",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #fff7fb 0%, #f8f4ff 100%);
    }

    .main-title {
        text-align: center;
        color: #ff7fa8;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #9a8fa3;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0 8px 25px rgba(180, 150, 180, 0.15);
        border: 2px solid #ffe1ec;
    }

    .place {
        text-align: center;
        color: #ff6f9c;
        font-size: 32px;
        font-weight: 800;
    }

    .emoji {
        text-align: center;
        font-size: 65px;
        margin: 5px;
    }

    .reason {
        background: #fff4f8;
        border-radius: 18px;
        padding: 18px;
        color: #665b68;
        line-height: 1.7;
        margin-top: 18px;
    }

    .tag {
        display: inline-block;
        background: #ffe1ec;
        color: #e75f8c;
        border-radius: 20px;
        padding: 7px 14px;
        margin: 4px;
        font-size: 14px;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        color: #b0a5b3;
        font-size: 13px;
        margin-top: 35px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 여행지 데이터
# -----------------------------
travel_data = {
    "ISTJ": {
        "place": "교토 🇯🇵",
        "emoji": "⛩️",
        "type": "차분하고 계획적인 여행",
        "reason": "정돈된 거리와 전통적인 분위기 속에서 여유롭게 여행하기 좋아요. 미리 계획한 일정대로 움직이면서 교토의 예쁜 골목과 사찰을 천천히 둘러보는 여행을 추천해요.",
        "tags": ["#계획여행", "#전통미", "#조용한여행"]
    },
    "ISFJ": {
        "place": "후쿠오카 🇯🇵",
        "emoji": "🍜",
        "type": "따뜻하고 편안한 여행",
        "reason": "복잡하지 않으면서 맛있는 음식과 아기자기한 공간을 즐길 수 있어요. 맛집을 찾아다니고 예쁜 카페에서 쉬는 힐링 여행과 잘 어울려요.",
        "tags": ["#힐링", "#맛집투어", "#소소한행복"]
    },
    "INFJ": {
        "place": "스위스 🇨🇭",
        "emoji": "🏔️",
        "type": "마음이 깊어지는 여행",
        "reason": "웅장한 자연을 바라보며 혼자만의 생각에 잠기기 좋은 곳이에요. 아름다운 풍경 속에서 천천히 걷고, 사진을 남기며 자신만의 시간을 가져보세요.",
        "tags": ["#자연", "#감성여행", "#혼자만의시간"]
    },
    "INTJ": {
        "place": "싱가포르 🇸🇬",
        "emoji": "🌃",
        "type": "효율적인 도시 탐험",
        "reason": "깔끔하고 체계적인 도시 환경과 다양한 볼거리를 한 번에 즐길 수 있어요. 동선을 효율적으로 짜서 여러 명소를 정복하는 여행이 잘 어울려요.",
        "tags": ["#도시여행", "#효율적인동선", "#스마트여행"]
    },
    "ISTP": {
        "place": "제주도 🇰🇷",
        "emoji": "🏄",
        "type": "자유로운 액티비티 여행",
        "reason": "정해진 일정에 얽매이기보다 그날의 기분에 따라 움직여보세요. 드라이브, 서핑, 오름 등 하고 싶은 걸 골라 즐기는 여행을 추천해요.",
        "tags": ["#자유여행", "#액티비티", "#드라이브"]
    },
    "ISFP": {
        "place": "파리 🇫🇷",
        "emoji": "🎨",
        "type": "감성 가득한 여행",
        "reason": "예쁜 거리와 미술관, 카페를 천천히 구경하면서 순간순간의 분위기를 즐겨보세요. 사진 찍기 좋은 장소를 발견하는 재미도 가득해요.",
        "tags": ["#감성", "#미술관", "#카페투어"]
    },
    "INFP": {
        "place": "아이슬란드 🇮🇸",
        "emoji": "🌌",
        "type": "동화 같은 여행",
        "reason": "현실에서 잠시 벗어나고 싶을 때 딱 좋은 여행지예요. 오로라와 폭포, 빙하를 바라보면서 평소에는 느끼기 어려운 특별한 감정을 경험해보세요.",
        "tags": ["#동화같은풍경", "#오로라", "#낭만"]
    },
    "INTP": {
        "place": "런던 🇬🇧",
        "emoji": "📚",
        "type": "호기심을 채우는 여행",
        "reason": "박물관과 과학관, 독특한 서점과 다양한 문화 공간이 많아요. 하나의 장소를 방문해도 '왜?'라는 호기심을 마음껏 펼칠 수 있어요.",
        "tags": ["#박물관", "#지적호기심", "#문화탐방"]
    },
    "ESTP": {
        "place": "방콕 🇹🇭",
        "emoji": "🌴",
        "type": "신나게 즐기는 여행",
        "reason": "맛있는 음식부터 야시장, 액티비티까지 재미있는 것들이 가득해요. 계획보다 현장에서 즉흥적으로 새로운 경험을 찾아다니는 여행을 추천해요.",
        "tags": ["#즉흥여행", "#액티비티", "#야시장"]
    },
    "ESFP": {
        "place": "하와이 🇺🇸",
        "emoji": "🌺",
        "type": "행복 충전 여행",
        "reason": "예쁜 바다와 맛있는 음식, 다양한 액티비티를 한꺼번에 즐길 수 있어요. 친구들과 함께 떠나면 더욱 신나는 추억을 만들 수 있어요.",
        "tags": ["#바다", "#친구여행", "#행복충전"]
    },
    "ENFP": {
        "place": "바르셀로나 🇪🇸",
        "emoji": "🍊",
        "type": "두근두근 모험 여행",
        "reason": "독특한 건축물과 맛있는 음식, 활기찬 거리가 가득한 곳이에요. 우연히 발견한 골목에서 새로운 장소를 만나는 여행이 잘 어울려요.",
        "tags": ["#모험", "#즉흥", "#새로운경험"]
    },
    "ENTP": {
        "place": "뉴욕 🇺🇸",
        "emoji": "🗽",
        "type": "새로운 자극을 찾아서",
        "reason": "매일 새로운 일이 일어나는 듯한 도시예요. 다양한 사람과 문화, 음식과 전시를 경험하면서 끊임없이 새로운 아이디어를 얻을 수 있어요.",
        "tags": ["#도시탐험", "#새로운자극", "#문화"]
    },
    "ESTJ": {
        "place": "도쿄 🇯🇵",
        "emoji": "🗼",
        "type": "알차고 완벽한 여행",
        "reason": "볼거리와 먹거리가 정말 많아서 계획을 세워 움직이기 좋아요. 쇼핑부터 관광까지 하루를 알차게 채워 만족도 높은 여행을 만들어보세요.",
        "tags": ["#알찬여행", "#쇼핑", "#도시여행"]
    },
    "ESFJ": {
        "place": "이탈리아 🇮🇹",
        "emoji": "🍝",
        "type": "함께라서 더 행복한 여행",
        "reason": "맛있는 음식과 아름다운 풍경을 사랑하는 사람과 함께 즐기기 좋은 곳이에요. 사진도 많이 찍고 맛있는 것도 함께 나눠 먹어보세요.",
        "tags": ["#친구와함께", "#맛있는여행", "#추억"]
    },
    "ENFJ": {
        "place": "캐나다 🇨🇦",
        "emoji": "🍁",
        "type": "사람과 자연을 모두 만나는 여행",
        "reason": "아름다운 자연과 다양한 도시 문화를 함께 경험할 수 있어요. 혼자보다는 소중한 사람들과 이야기를 나누며 여행할 때 더욱 즐거워요.",
        "tags": ["#소중한사람", "#자연", "#추억"]
    },
    "ENTJ": {
        "place": "두바이 🇦🇪",
        "emoji": "🏙️",
        "type": "스케일 큰 여행",
        "reason": "화려한 건축물과 다양한 경험을 한 번에 즐길 수 있어요. 목표를 정하고 하나씩 정복해 나가는 스타일의 여행과 잘 어울려요.",
        "tags": ["#럭셔리", "#도시", "#버킷리스트"]
    }
}

# -----------------------------
# 화면
# -----------------------------
st.markdown(
    '<div class="main-title">🌷 MBTI 여행 처방전 💌</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">당신의 MBTI에게 딱 맞는 여행지를 찾아드릴게요 ✈️</div>',
    unsafe_allow_html=True
)

st.markdown("### 💗 먼저 당신의 MBTI를 골라주세요!")

mbti = st.selectbox(
    "MBTI",
    list(travel_data.keys()),
    index=None,
    placeholder="MBTI를 선택해주세요 ˶ᵔ ᵕ ᵔ˶"
)

if mbti:
    data = travel_data[mbti]

    st.markdown(
        f"""
        <div class="card">
            <div class="emoji">{data['emoji']}</div>
            <div class="place">{data['place']}</div>
            <p style="text-align:center; color:#9a8fa3; font-size:17px;">
                {mbti} · {data['type']}
            </p>

            <div style="text-align:center; margin-top:15px;">
                {''.join(f'<span class="tag">{tag}</span>' for tag in data['tags'])}
            </div>

            <div class="reason">
                💌 <b>왜 여기가 잘 어울릴까요?</b><br><br>
                {data['reason']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("💗 다른 여행지도 궁금해!", use_container_width=True):
        other_places = [
            value["place"]
            for key, value in travel_data.items()
            if key != mbti
        ]

        random_place = random.choice(other_places)

        st.success(f"✨ 오늘의 깜짝 여행지는 **{random_place}**! ✨")

else:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <div style="font-size:55px;">🐰🌷</div>
        <p style="color:#8f8394; font-size:16px;">
            아직 여행지가 정해지지 않았어요!<br>
            위에서 MBTI를 골라주세요 💕
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    '<div class="footer">✈️ 당신의 다음 여행이 조금 더 설레기를 바라요 ♡</div>',
    unsafe_allow_html=True
)
