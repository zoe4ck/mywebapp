import streamlit as st
from datetime import date

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="오늘의 사주 한 스푼",
    page_icon="🌷",
    layout="centered"
)

# ==========================================
# 귀여운 디자인
# ==========================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffe7f0 0%, transparent 25%),
        radial-gradient(circle at 90% 20%, #eee5ff 0%, transparent 25%),
        linear-gradient(180deg, #fff9fc 0%, #faf7ff 100%);
    color: #594d5d;
}

.block-container {
    max-width: 760px;
    padding-top: 45px;
    padding-bottom: 60px;
}

/* 제목 */

.mini {
    text-align: center;
    font-size: 45px;
    margin-bottom: 5px;
}

.title {
    text-align: center;
    color: #e982a6;
    font-size: 36px;
    font-weight: 800;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: #a99aaa;
    font-size: 14px;
    margin-top: 8px;
    margin-bottom: 30px;
}

/* 날짜 선택 영역 */

.select-card {
    background: rgba(255,255,255,0.85);
    border: 2px solid #f7dce8;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 8px 25px rgba(190,160,190,0.12);
}

.select-title {
    text-align: center;
    color: #d8759c;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 15px;
}

/* 날짜 입력 */

div[data-testid="stDateInput"] label {
    color: #8d7d91 !important;
}

/* 결과 카드 */

.result-card {
    background: rgba(255,255,255,0.95);
    border: 2px solid #f4d8e6;
    border-radius: 28px;
    padding: 32px 28px;
    margin-top: 28px;
    box-shadow: 0 10px 30px rgba(180,150,180,0.14);
}

/* 결과 상단 */

.result-emoji {
    text-align: center;
    font-size: 60px;
}

.result-title {
    text-align: center;
    color: #df769d;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.result-subtitle {
    text-align: center;
    color: #a99aaa;
    font-size: 14px;
    margin-top: 7px;
}

/* 띠 / 오행 */

.badge-area {
    text-align: center;
    margin-top: 20px;
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 4px;
    border-radius: 20px;
    background: #fff0f6;
    border: 1px solid #f3cddd;
    color: #d96f98;
    font-size: 13px;
    font-weight: 600;
}

/* 섹션 */

.section {
    background: #fff8fb;
    border-radius: 19px;
    padding: 18px 20px;
    margin-top: 15px;
}

.section-title {
    color: #d8759c;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 8px;
}

.section-text {
    color: #685c6b;
    font-size: 14px;
    line-height: 1.8;
}

/* 행운 */

.lucky {
    background: linear-gradient(
        135deg,
        #fff0f6,
        #f5efff
    );
    border-radius: 20px;
    padding: 20px;
    margin-top: 18px;
    text-align: center;
}

.lucky-title {
    color: #b47bc0;
    font-weight: 800;
    margin-bottom: 12px;
}

.lucky-item {
    color: #756579;
    font-size: 14px;
    line-height: 2;
}

/* 버튼 */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid #efb9cf;
    background: #fff5f9;
    color: #d56f98;
    height: 45px;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #df8eae;
    background: #ffeaf2;
    color: #c75d87;
}

/* 하단 */

.footer {
    text-align: center;
    color: #b9aaba;
    font-size: 12px;
    margin-top: 30px;
}

</style>
""",
    unsafe_allow_html=True
)


# ==========================================
# 데이터
# ==========================================

animal_data = [
    ("쥐", "🐭"),
    ("소", "🐮"),
    ("호랑이", "🐯"),
    ("토끼", "🐰"),
    ("용", "🐲"),
    ("뱀", "🐍"),
    ("말", "🐴"),
    ("양", "🐑"),
    ("원숭이", "🐵"),
    ("닭", "🐔"),
    ("개", "🐶"),
    ("돼지", "🐷")
]

element_data = {
    "목": {
        "emoji": "🌱",
        "color": "초록",
        "keyword": "성장과 새로운 시작",
        "personality": "새로운 것을 배우고 성장하려는 마음이 강한 편이에요. 호기심이 많고 자신의 가능성을 넓혀가는 과정에서 에너지를 얻는 타입으로 볼 수 있어요.",
        "love": "연애에서도 함께 성장할 수 있는 관계를 중요하게 생각하는 편이에요. 상대방의 생각과 가능성을 존중하면서 천천히 가까워지는 모습이 잘 어울려요.",
        "study": "한 가지를 오래 붙잡기보다 새로운 내용을 배우고 직접 응용해보는 방식이 잘 맞을 수 있어요."
    },

    "화": {
        "emoji": "🔥",
        "color": "빨강",
        "keyword": "열정과 표현",
        "personality": "감정과 에너지를 비교적 적극적으로 표현하는 성향으로 볼 수 있어요. 좋아하는 일에는 집중력이 높아지고 주변에 활기를 주는 타입이에요.",
        "love": "마음이 생기면 상대방에게 따뜻한 관심을 표현하는 편이에요. 함께 재미있는 경험을 만들면서 관계가 깊어지는 스타일과 잘 어울려요.",
        "study": "목표가 분명할 때 집중력이 올라가기 쉬워요. 작은 목표를 정하고 달성하는 방식이 도움이 될 수 있어요."
    },

    "토": {
        "emoji": "🌷",
        "color": "노랑",
        "keyword": "안정과 균형",
        "personality": "차분하게 상황을 살피고 주변 사람들과 균형을 맞추려는 성향으로 볼 수 있어요. 꾸준함과 안정적인 환경에서 장점을 발휘하기 좋아요.",
        "love": "가볍게 시작하기보다 신뢰를 쌓으면서 안정적인 관계를 만들어가는 것을 편하게 느끼는 스타일이에요.",
        "study": "일정한 루틴을 만들어 꾸준하게 공부하는 방식과 잘 맞을 수 있어요."
    },

    "금": {
        "emoji": "⭐",
        "color": "하양",
        "keyword": "기준과 집중",
        "personality": "자신만의 기준이 뚜렷하고 하고 싶은 일을 명확하게 정하는 성향으로 볼 수 있어요. 집중해야 할 때 몰입하는 힘을 중요하게 생각하는 타입이에요.",
        "love": "상대방에게 쉽게 휩쓸리기보다 자신이 정말 좋아하는 사람인지 천천히 확인하는 편으로 볼 수 있어요.",
        "study": "목표와 결과가 명확할수록 집중하기 쉬워요. 공부할 내용을 구체적인 단위로 나누면 좋아요."
    },

    "수": {
        "emoji": "💧",
        "color": "파랑",
        "keyword": "유연함과 감성",
        "personality": "상황에 따라 유연하게 생각하고 주변의 분위기를 세심하게 느끼는 성향으로 볼 수 있어요. 혼자 생각을 정리하는 시간도 중요하게 여기는 편이에요.",
        "love": "상대방의 감정을 중요하게 생각하고 서로 편안하게 이야기할 수 있는 관계에서 애정을 느끼기 쉬워요.",
        "study": "조용하고 편안한 환경에서 자신만의 속도로 집중하는 방식이 잘 맞을 수 있어요."
    }
}


# ==========================================
# 함수
# ==========================================

def get_animal(year):
    index = (year - 4) % 12
    return animal_data[index]


def get_element(year):
    # 재미용 오행 계산
    index = year % 5
    elements = ["목", "화", "토", "금", "수"]
    return elements[index]


def get_season(month):
    if month in [3, 4, 5]:
        return "봄"
    elif month in [6, 7, 8]:
        return "여름"
    elif month in [9, 10, 11]:
        return "가을"
    else:
        return "겨울"


def get_lucky(month, element):
    lucky_colors = {
        "목": ["초록", "연두", "아이보리"],
        "화": ["분홍", "주황", "빨강"],
        "토": ["베이지", "노랑", "브라운"],
        "금": ["하양", "실버", "회색"],
        "수": ["하늘색", "파랑", "남색"]
    }

    lucky_items = {
        "봄": "작은 꽃 모양 소품 🌷",
        "여름": "시원한 음료 🧋",
        "가을": "향기로운 향수 🌿",
        "겨울": "포근한 니트 🧸"
    }

    colors = lucky_colors[element]

    return colors, lucky_items[get_season(month)]


# ==========================================
# 제목
# ==========================================

st.markdown(
    '<div class="mini">🌙</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">오늘의 사주 한 스푼</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">생년월일 속에 담긴 나만의 작은 이야기 ✦</div>',
    unsafe_allow_html=True
)


# ==========================================
# 날짜 선택
# ==========================================

st.markdown(
    '<div class="select-card">'
    '<div class="select-title">'
    '🌷 생년월일을 알려주세요'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

birth_date = st.date_input(
    "생년월일",
    value=None,
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="YYYY-MM-DD"
)


# ==========================================
# 결과
# ==========================================

if birth_date is not None:

    year = birth_date.year
    month = birth_date.month
    day = birth_date.day

    animal_name, animal_emoji = get_animal(year)

    element = get_element(year)
    element_info = element_data[element]

    season = get_season(month)

    lucky_colors, lucky_item = get_lucky(month, element)

    # --------------------------
    # 결과 카드
    # --------------------------

    st.markdown(
        '<div class="result-card">'
        '<div class="result-emoji">'
        + animal_emoji +
        '</div>'
        '<div class="result-title">'
        + animal_name +
        '띠의 작은 운세'
        '</div>'
        '<div class="result-subtitle">'
        + str(year) + '년 ' + str(month) + '월 ' + str(day) + '일'
        '</div>'

        '<div class="badge-area">'
        '<span class="badge">'
        + element_info["emoji"] + ' 오행 · ' + element +
        '</span>'

        '<span class="badge">'
        + '🌸 ' + season +
        '</span>'

        '<span class="badge">'
        + '🐾 ' + animal_name + '띠' +
        '</span>'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------
    # 기본 성향
    # --------------------------

    st.markdown(
        '<div class="section">'
        '<div class="section-title">'
        + element_info["emoji"] +
        ' 나의 기본 성향'
        '</div>'

        '<div class="section-text">'
        + element_info["personality"] +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------
    # 연애운
    # --------------------------

    st.markdown(
        '<div class="section">'
        '<div class="section-title">'
        '💗 나의 연애 이야기'
        '</div>'

        '<div class="section-text">'
        + element_info["love"] +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------
    # 공부 / 진로
    # --------------------------

    st.markdown(
        '<div class="section">'
        '<div class="section-title">'
        '📚 공부와 진로'
        '</div>'

        '<div class="section-text">'
        + element_info["study"] +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # --------------------------
    # 행운
    # --------------------------

    lucky_color_text = " · ".join(lucky_colors)

    st.markdown(
        '<div class="lucky">'
        '<div class="lucky-title">'
        '🍀 오늘의 작은 행운'
        '</div>'

        '<div class="lucky-item">'
        '🎨 행운의 색 · ' + lucky_color_text +
        '<br>'
        '🎁 행운의 아이템 · ' + lucky_item +
        '<br>'
        '🌷 오늘의 키워드 · ' + element_info["keyword"] +
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🌙 다시 운세 보기", use_container_width=True):
        st.rerun()

else:

    # 날짜 선택 전 화면

    st.markdown(
        '<div class="result-card">'
        '<div class="result-emoji">🐰🌙</div>'

        '<div class="result-title">'
        '아직 운세가 잠들어 있어요'
        '</div>'

        '<div class="result-subtitle">'
        '생년월일을 선택하면 작은 운세 카드가 나타나요'
        '</div>'

        '<div class="section">'
        '<div class="section-text" style="text-align:center;">'
        '두근두근… 💗<br>'
        '당신의 생년월일을 기다리고 있어요.'
        '</div>'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )


# ==========================================
# 하단
# ==========================================

st.markdown(
    '<div class="footer">'
    '🌷 재미로 가볍게 즐겨보는 생년월일 운세 콘텐츠예요 ♡'
    '</div>',
    unsafe_allow_html=True
)
