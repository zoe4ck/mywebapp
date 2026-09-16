import streamlit as st

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="LOVE TAROT · MBTI",
    page_icon="🔮",
    layout="centered"
)

# ==========================================
# 신비로운 디자인 CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Noto+Sans+KR:wght@400;500;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 50% 10%, rgba(108, 72, 170, 0.35), transparent 30%),
        radial-gradient(circle at 10% 80%, rgba(82, 45, 130, 0.25), transparent 30%),
        linear-gradient(180deg, #10091d 0%, #170d29 50%, #0c0715 100%);
    color: #f8edf9;
}

/* 별 배경 */
.stApp::before {
    content: "✦  ·  ✧     ·     ✦        ·  ✧     ✦   ·      ✧     ·     ✦";
    position: fixed;
    top: 5%;
    left: 0;
    width: 100%;
    color: rgba(255, 226, 255, 0.5);
    font-size: 17px;
    letter-spacing: 14px;
    line-height: 3;
    pointer-events: none;
    z-index: 0;
}

/* 전체 컨테이너 */
.block-container {
    max-width: 760px;
    padding-top: 50px;
    padding-bottom: 50px;
}

/* 제목 */
.title {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #f5d98b;
    text-shadow:
        0 0 8px rgba(245, 217, 139, 0.5),
        0 0 25px rgba(173, 103, 255, 0.4);
}

.subtitle {
    text-align: center;
    color: #c9b7d9;
    font-size: 14px;
    letter-spacing: 2px;
    margin-top: 8px;
    margin-bottom: 35px;
}

/* 달 */
.moon {
    text-align: center;
    font-size: 70px;
    margin-bottom: -5px;
    filter: drop-shadow(0 0 15px rgba(255, 231, 155, 0.5));
}

/* 선택 영역 */
.select-title {
    text-align: center;
    color: #e9d3ef;
    font-size: 17px;
    font-weight: 500;
    margin-bottom: 10px;
}

/* selectbox */
div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.06);
    border: 1px solid #a875c9;
    border-radius: 12px;
    color: white;
}

div[data-baseweb="select"] span {
    color: #f5e9f8;
}

/* 타로 카드 */
.tarot-card {
    position: relative;
    margin-top: 35px;
    padding: 42px 35px;
    border-radius: 22px;
    background:
        radial-gradient(circle at 50% 30%, rgba(125, 74, 176, 0.25), transparent 40%),
        linear-gradient(145deg, #211332, #120b1e);
    border: 1px solid #c69b54;
    box-shadow:
        0 0 0 5px rgba(198,155,84,0.07),
        0 0 30px rgba(155, 94, 218, 0.25),
        inset 0 0 35px rgba(0,0,0,0.35);
}

/* 카드 장식 */
.card-symbol {
    text-align: center;
    font-size: 60px;
    margin-bottom: 8px;
    filter: drop-shadow(0 0 12px rgba(245,217,139,0.45));
}

.card-small {
    text-align: center;
    color: #c9a45e;
    font-family: 'Cinzel', serif;
    font-size: 12px;
    letter-spacing: 4px;
}

.card-place {
    text-align: center;
    color: #f5d98b;
    font-family: 'Cinzel', serif;
    font-size: 30px;
    font-weight: 700;
    margin-top: 10px;
    text-shadow: 0 0 15px rgba(245,217,139,0.25);
}

.card-type {
    text-align: center;
    color: #d9c8e5;
    margin-top: 8px;
    font-size: 15px;
}

.divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #c69b54,
        transparent
    );
    margin: 25px 0;
}

/* 내용 박스 */
.info-title {
    color: #f5d98b;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 8px;
}

.info-text {
    color: #ded2e5;
    font-size: 14px;
    line-height: 1.8;
}

/* 키워드 */
.keyword-area {
    text-align: center;
    margin-top: 25px;
}

.keyword {
    display: inline-block;
    padding: 7px 14px;
    margin: 4px;
    border-radius: 20px;
    border: 1px solid #8e67a8;
    background: rgba(142,103,168,0.12);
    color: #e8d6ef;
    font-size: 13px;
}

/* 하단 문구 */
.footer {
    text-align: center;
    color: #897597;
    font-size: 12px;
    margin-top: 35px;
    letter-spacing: 1px;
}

/* 버튼 */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #c69b54;
    background: rgba(198,155,84,0.08);
    color: #f5d98b;
    height: 45px;
    font-size: 14px;
}

.stButton > button:hover {
    border-color: #f5d98b;
    color: white;
    background: rgba(198,155,84,0.15);
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# MBTI 데이터
# ==========================================

mbti_data = {

    "ISTJ": {
        "symbol": "⚖️",
        "name": "THE DEVOTED",
        "type": "신뢰를 쌓아가는 사랑",
        "style": "쉽게 마음을 열지는 않지만 한번 마음을 주면 오래도록 관계를 지키려는 편이에요.",
        "love": "말보다 행동으로 마음을 표현하는 경우가 많아요. 상대방의 약속을 기억하고 필요한 것을 챙겨주는 식으로 애정을 보여줘요.",
        "attraction": "상대방에게 안정감과 신뢰가 느껴질 때 천천히 호감이 깊어져요.",
        "date": "조용한 카페에서 이야기하기 · 계획적인 여행 · 함께 맛있는 식사하기",
        "keywords": ["#신뢰", "#안정감", "#꾸준함", "#책임감"]
    },

    "ISFJ": {
        "symbol": "🌙",
        "name": "THE TENDER HEART",
        "type": "따뜻하게 감싸주는 사랑",
        "style": "상대방의 작은 변화도 알아차리고 세심하게 챙겨주는 다정한 연애를 하는 편이에요.",
        "love": "상대가 좋아하는 음식이나 사소한 취향을 기억해두었다가 챙겨주는 식으로 마음을 표현해요.",
        "attraction": "자신을 편안하게 해주고 진심으로 배려해주는 사람에게 마음이 가기 쉬워요.",
        "date": "예쁜 카페 · 맛집 탐방 · 함께 영화 보기 · 소소한 산책",
        "keywords": ["#다정함", "#배려", "#안정", "#세심함"]
    },

    "INFJ": {
        "symbol": "🌌",
        "name": "THE MYSTIC",
        "type": "깊은 마음을 나누는 사랑",
        "style": "겉으로는 차분해 보여도 마음속에서는 상대방과의 관계를 깊게 생각하는 편이에요.",
        "love": "상대방의 말에 담긴 의미를 세심하게 살피고 진솔한 대화를 통해 애정을 표현해요.",
        "attraction": "겉모습보다 자신의 가치관이나 생각을 이해해주는 사람에게 끌리는 편이에요.",
        "date": "밤 산책 · 조용한 카페 · 전시회 · 오래 이야기할 수 있는 장소",
        "keywords": ["#깊은대화", "#공감", "#낭만", "#진심"]
    },

    "INTJ": {
        "symbol": "🔮",
        "name": "THE STRATEGIST",
        "type": "천천히 깊어지는 사랑",
        "style": "누군가를 좋아한다고 바로 표현하기보다 상대방을 충분히 알아가는 시간을 갖는 편이에요.",
        "love": "상대방의 목표를 응원하거나 문제를 함께 해결해주는 방식으로 마음을 표현해요.",
        "attraction": "자신만의 생각과 목표가 있고 지적인 대화를 할 수 있는 사람에게 매력을 느끼기 쉬워요.",
        "date": "전시회 · 여행 계획 세우기 · 서점 데이트 · 깊은 대화",
        "keywords": ["#신중함", "#지적대화", "#독립적", "#깊이"]
    },

    "ISTP": {
        "symbol": "🗡️",
        "name": "THE FREE SOUL",
        "type": "자유롭고 솔직한 사랑",
        "style": "서로의 자유를 존중하면서 부담 없이 자연스럽게 가까워지는 연애를 선호하는 편이에요.",
        "love": "말보다는 함께 무언가를 하면서 자연스럽게 애정을 표현해요.",
        "attraction": "간섭이 적고 서로의 개성을 존중해주는 사람에게 편안함을 느끼기 쉬워요.",
        "date": "드라이브 · 액티비티 · 맛집 탐방 · 즉흥 여행",
        "keywords": ["#자유", "#솔직함", "#즉흥", "#편안함"]
    },

    "ISFP": {
        "symbol": "🌹",
        "name": "THE ROMANTIC",
        "type": "감각적인 낭만을 즐기는 사랑",
        "style": "연애의 순간순간에서 느껴지는 감정과 분위기를 중요하게 생각하는 편이에요.",
        "love": "작은 선물이나 예쁜 장소, 함께하는 특별한 순간으로 마음을 표현하는 경우가 많아요.",
        "attraction": "따뜻하고 부드러운 분위기를 가진 사람에게 자연스럽게 끌릴 수 있어요.",
        "date": "미술관 · 예쁜 카페 · 공원 산책 · 사진 찍기",
        "keywords": ["#감성", "#낭만", "#예술", "#순수함"]
    },

    "INFP": {
        "symbol": "🪽",
        "name": "THE DREAMER",
        "type": "동화 같은 사랑",
        "style": "사랑에 대한 이상과 자신만의 낭만을 중요하게 생각하는 편이에요.",
        "love": "상대방의 이야기를 오래 들어주고 감정을 깊이 공감하면서 마음을 표현해요.",
        "attraction": "자신의 내면을 이해해주고 진심으로 공감해주는 사람에게 마음이 깊어지기 쉬워요.",
        "date": "별 보기 · 밤 산책 · 감성 카페 · 여행",
        "keywords": ["#낭만", "#공감", "#순수", "#감성"]
    },

    "INTP": {
        "symbol": "⭐",
        "name": "THE OBSERVER",
        "type": "호기심에서 시작되는 사랑",
        "style": "상대방을 알아가는 과정 자체를 흥미롭게 느끼며 천천히 가까워지는 편이에요.",
        "love": "관심 있는 주제로 이야기를 나누거나 상대방의 궁금증을 함께 해결하면서 친밀감을 표현해요.",
        "attraction": "독특한 생각을 가지고 있고 대화가 잘 통하는 사람에게 관심이 생기기 쉬워요.",
        "date": "서점 · 박물관 · 보드게임 · 새로운 장소 탐방",
        "keywords": ["#호기심", "#대화", "#독특함", "#지적매력"]
    },

    "ESTP": {
        "symbol": "🔥",
        "name": "THE ADVENTURER",
        "type": "짜릿하고 생생한 사랑",
        "style": "좋아하는 사람과 직접 다양한 경험을 하면서 관계를 만들어가는 편이에요.",
        "love": "재미있는 데이트를 계획하거나 즉흥적으로 새로운 경험을 함께 하며 마음을 표현해요.",
        "attraction": "자신감 있고 함께 있을 때 즐거운 에너지를 주는 사람에게 끌리기 쉬워요.",
        "date": "놀이공원 · 스포츠 · 여행 · 맛집 투어",
        "keywords": ["#열정", "#모험", "#즉흥", "#즐거움"]
    },

    "ESFP": {
        "symbol": "☀️",
        "name": "THE SUN",
        "type": "행복을 나누는 사랑",
        "style": "좋아하는 사람과 함께하는 순간 자체를 즐기며 밝고 표현력 있는 연애를 하는 편이에요.",
        "love": "칭찬이나 애정 표현을 직접적으로 하고 함께 재미있는 추억을 만드는 것을 좋아해요.",
        "attraction": "자신의 모습을 편하게 보여줄 수 있고 함께 웃을 수 있는 사람에게 끌리기 쉬워요.",
        "date": "축제 · 맛집 · 놀이공원 · 여행",
        "keywords": ["#행복", "#표현력", "#활발함", "#추억"]
    },

    "ENFP": {
        "symbol": "✨",
        "name": "THE SPARK",
        "type": "설렘이 가득한 사랑",
        "style": "좋아하는 사람이 생기면 관계의 가능성을 상상하며 빠르게 설렘을 느낄 수 있어요.",
        "love": "재미있는 이야기와 장난, 깜짝 이벤트 등 다양한 방법으로 마음을 표현해요.",
        "attraction": "자신의 개성을 존중하면서 함께 새로운 것을 경험할 수 있는 사람에게 끌리기 쉬워요.",
        "date": "즉흥 여행 · 새로운 맛집 · 전시 · 야경",
        "keywords": ["#설렘", "#호기심", "#자유", "#열정"]
    },

    "ENTP": {
        "symbol": "☄️",
        "name": "THE WILDCARD",
        "type": "예측할 수 없는 두근거림",
        "style": "연애에서도 새로운 자극과 재미있는 대화를 중요하게 생각하는 편이에요.",
        "love": "장난과 토론, 재미있는 아이디어를 공유하면서 자연스럽게 호감을 표현해요.",
        "attraction": "자신만의 생각이 뚜렷하고 대화가 흥미로운 사람에게 관심이 생기기 쉬워요.",
        "date": "새로운 맛집 · 전시회 · 여행 · 이색 체험",
        "keywords": ["#재치", "#토론", "#자극", "#호기심"]
    },

    "ESTJ": {
        "symbol": "👑",
        "name": "THE LEADER",
        "type": "확실하고 책임감 있는 사랑",
        "style": "관계에서도 자신의 마음과 의도를 비교적 명확하게 표현하는 편이에요.",
        "love": "상대방에게 필요한 것을 직접 해결해주거나 계획을 세우며 마음을 표현해요.",
        "attraction": "자신의 삶을 책임감 있게 살아가며 서로 약속을 지킬 수 있는 사람에게 끌리기 쉬워요.",
        "date": "맛집 · 여행 · 쇼핑 · 계획적인 데이트",
        "keywords": ["#책임감", "#확실함", "#추진력", "#신뢰"]
    },

    "ESFJ": {
        "symbol": "💐",
        "name": "THE LOVER",
        "type": "마음을 아낌없이 나누는 사랑",
        "style": "상대방과 함께하는 시간을 소중하게 생각하고 애정을 적극적으로 표현하는 편이에요.",
        "love": "상대방의 기념일이나 취향을 기억하고 작은 이벤트를 준비하는 식으로 사랑을 표현해요.",
        "attraction": "따뜻하고 예의 바르며 자신의 마음을 솔직하게 표현하는 사람에게 끌리기 쉬워요.",
        "date": "맛집 · 카페 · 쇼핑 · 기념일 데이트",
        "keywords": ["#애정표현", "#배려", "#다정함", "#추억"]
    },

    "ENFJ": {
        "symbol": "💫",
        "name": "THE GUIDE",
        "type": "서로를 성장시키는 사랑",
        "style": "상대방의 감정과 상황을 세심하게 살피면서 관계를 발전시켜 나가는 편이에요.",
        "love": "상대방의 꿈이나 고민을 진심으로 들어주고 응원하며 애정을 표현해요.",
        "attraction": "진솔한 대화를 할 수 있고 서로에게 긍정적인 영향을 줄 수 있는 사람에게 끌리기 쉬워요.",
        "date": "전시회 · 여행 · 카페 · 함께하는 취미",
        "keywords": ["#공감", "#응원", "#성장", "#진심"]
    },

    "ENTJ": {
        "symbol": "🌟",
        "name": "THE COMMANDER",
        "type": "열정적으로 이끄는 사랑",
        "style": "좋아하는 사람에게 적극적으로 다가가고 관계를 발전시키기 위해 행동하는 편이에요.",
        "love": "상대방의 목표를 지원하고 함께 미래를 계획하면서 마음을 표현해요.",
        "attraction": "자신의 의견과 목표가 분명하고 함께 성장할 수 있는 사람에게 끌리기 쉬워요.",
        "date": "여행 · 새로운 레스토랑 · 전시 · 특별한 이벤트",
        "keywords": ["#열정", "#목표", "#추진력", "#성장"]
    }
}


# ==========================================
# 제목
# ==========================================

st.markdown('<div class="moon">☾</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="title">LOVE TAROT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">YOUR MBTI · YOUR LOVE STORY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="select-title">✦ 당신의 MBTI를 선택해주세요 ✦</div>',
    unsafe_allow_html=True
)


# ==========================================
# MBTI 선택
# ==========================================

mbti = st.selectbox(
    "MBTI",
    list(mbti_data.keys()),
    index=None,
    placeholder="카드를 뽑기 전에 MBTI를 골라주세요",
    label_visibility="collapsed"
)


# ==========================================
# 결과
# ==========================================

if mbti:

    data = mbti_data[mbti]

    keywords = ""

    for keyword in data["keywords"]:
        keywords += f'<span class="keyword">{keyword}</span>'

    st.markdown(
        f"""
<div class="tarot-card">

    <div class="card-small">✦ THE LOVE CARD ✦</div>

    <div class="card-symbol">
        {data["symbol"]}
    </div>

    <div class="card-place">
        {data["name"]}
    </div>

    <div class="card-type">
        {mbti} · {data["type"]}
    </div>

    <div class="divider"></div>

    <div class="info-title">
        ♡ 당신의 연애 스타일
    </div>

    <div class="info-text">
        {data["style"]}
    </div>

    <div class="divider"></div>

    <div class="info-title">
        ✦ 사랑할 때의 모습
    </div>

    <div class="info-text">
        {data["love"]}
    </div>

    <br>

    <div class="info-title">
        ☾ 이런 사람에게 끌릴 수 있어요
    </div>

    <div class="info-text">
        {data["attraction"]}
    </div>

    <br>

    <div class="info-title">
        ♧ 추천 데이트
    </div>

    <div class="info-text">
        {data["date"]}
    </div>

    <div class="keyword-area">
        {keywords}
    </div>

</div>
""",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🔮 다시 카드를 확인하기", use_container_width=True):
        st.rerun()


else:

    st.markdown(
        """
<div class="tarot-card">

    <div class="card-small">✦ MYSTIC LOVE ✦</div>

    <div class="card-symbol">
        🔮
    </div>

    <div class="card-place">
        YOUR LOVE STORY
    </div>

    <div class="card-type">
        아직 당신의 사랑 카드는 닫혀 있어요.
    </div>

    <div class="divider"></div>

    <div class="info-text" style="text-align:center;">
        MBTI를 선택하면<br>
        당신의 연애 스타일을 담은<br>
        <b style="color:#f5d98b;">LOVE CARD</b>가 나타납니다.
        <br><br>
        ✦ 운명은 선택에서 시작됩니다 ✦
    </div>

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================
# 하단
# ==========================================

st.markdown(
    '<div class="footer">'
    '✦ MBTI 특성을 바탕으로 한 재미있는 연애 콘텐츠입니다 ✦'
    '</div>',
    unsafe_allow_html=True
)
