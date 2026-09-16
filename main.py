import streamlit as st
from datetime import date, datetime
import random

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="MYSTIC SAJU",
    page_icon="🔮",
    layout="centered"
)


# =========================================================
# 타로 / 신비로운 디자인
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(116, 77, 150, 0.30), transparent 35%),
        radial-gradient(circle at 10% 30%, rgba(55, 42, 92, 0.35), transparent 30%),
        radial-gradient(circle at 90% 70%, rgba(72, 48, 105, 0.30), transparent 35%),
        linear-gradient(145deg, #100b20 0%, #17102d 45%, #0b0815 100%);
    color: #eee8f7;
    font-family: 'Noto Sans KR', sans-serif;
}

.block-container {
    max-width: 900px;
    padding-top: 45px;
    padding-bottom: 80px;
}

/* 별 */

.stars {
    text-align: center;
    color: #cdb8e8;
    font-size: 13px;
    letter-spacing: 12px;
    margin-bottom: 12px;
}

/* 메인 제목 */

.moon {
    text-align: center;
    font-size: 65px;
    margin-bottom: 4px;
    filter: drop-shadow(0 0 15px rgba(220,190,255,.45));
}

.main-title {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 39px;
    letter-spacing: 7px;
    color: #eee4ff;
    text-shadow: 0 0 20px rgba(200,170,255,.45);
}

.subtitle {
    text-align: center;
    color: #a99abf;
    font-size: 12px;
    letter-spacing: 2px;
    margin-top: 13px;
    margin-bottom: 38px;
}

/* 입력 카드 */

.input-box {
    background: linear-gradient(
        145deg,
        rgba(42,29,67,.95),
        rgba(24,17,42,.95)
    );
    border: 1px solid rgba(192,159,232,.35);
    border-radius: 25px;
    padding: 26px;
    box-shadow:
        0 0 35px rgba(88,55,130,.18),
        inset 0 0 25px rgba(190,150,230,.03);
}

.input-title {
    text-align: center;
    color: #d6c2ef;
    font-family: 'Cinzel', serif;
    font-size: 17px;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

/* Streamlit 입력창 */

div[data-testid="stDateInput"] label,
div[data-testid="stSelectbox"] label {
    color: #b9abc9 !important;
    font-size: 13px !important;
}

div[data-testid="stDateInput"] input {
    background: #201735 !important;
    color: #eee8f7 !important;
    border: 1px solid #5c4778 !important;
    border-radius: 12px !important;
}

div[data-testid="stSelectbox"] > div {
    background: #201735 !important;
    color: #eee8f7 !important;
    border-radius: 12px !important;
}

/* 결과 카드 */

.result-card {
    position: relative;
    background:
        radial-gradient(circle at 50% 0%, rgba(150,105,190,.12), transparent 40%),
        linear-gradient(145deg, rgba(35,24,56,.97), rgba(19,14,33,.98));
    border: 1px solid rgba(193,157,232,.35);
    border-radius: 28px;
    padding: 32px 27px;
    margin-top: 28px;
    box-shadow:
        0 18px 45px rgba(0,0,0,.30),
        inset 0 0 35px rgba(180,140,220,.025);
}

/* 카드 위 장식 */

.card-symbol {
    text-align: center;
    font-size: 48px;
    filter: drop-shadow(0 0 13px rgba(220,190,255,.4));
}

.card-title {
    text-align: center;
    font-family: 'Cinzel', serif;
    color: #eadcff;
    font-size: 27px;
    letter-spacing: 4px;
    margin-top: 7px;
}

.card-subtitle {
    text-align: center;
    color: #9182a5;
    font-size: 12px;
    margin-top: 10px;
}

/* 구분선 */

.divider {
    width: 85%;
    height: 1px;
    margin: 31px auto;
    background: linear-gradient(
        90deg,
        transparent,
        #80649d,
        #c2a6d8,
        #80649d,
        transparent
    );
}

/* 사주 기둥 */

.pillars {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 30px;
}

.pillar {
    width: 155px;
    min-height: 215px;
    background:
        radial-gradient(circle at 50% 10%, rgba(172,132,210,.13), transparent 40%),
        linear-gradient(180deg, #281b3c, #171125);
    border: 1px solid #5b4774;
    border-radius: 17px;
    text-align: center;
    padding: 18px 8px;
    box-shadow: inset 0 0 20px rgba(150,110,190,.04);
}

.pillar-name {
    color: #b9a3ce;
    font-family: 'Cinzel', serif;
    font-size: 12px;
    letter-spacing: 1px;
    margin-bottom: 13px;
}

.heaven {
    font-family: serif;
    font-size: 40px;
    color: #eee1fa;
    text-shadow: 0 0 12px rgba(210,180,245,.3);
}

.earth {
    font-family: serif;
    font-size: 40px;
    color: #c5a7da;
    margin-top: 8px;
    text-shadow: 0 0 12px rgba(210,180,245,.25);
}

.pillar-info {
    color: #897a99;
    font-size: 10px;
    margin-top: 7px;
}

/* 팔자 */

.eight-title {
    text-align: center;
    color: #bda5d3;
    font-family: 'Cinzel', serif;
    font-size: 14px;
    letter-spacing: 2px;
    margin-bottom: 13px;
}

.eight-text {
    text-align: center;
    color: #f0e4fa;
    font-family: serif;
    font-size: 29px;
    letter-spacing: 10px;
    text-shadow: 0 0 15px rgba(215,180,245,.3);
}

/* 섹션 제목 */

.section-title {
    text-align: center;
    color: #dfcaef;
    font-family: 'Cinzel', serif;
    font-size: 19px;
    letter-spacing: 3px;
    margin-bottom: 22px;
}

/* 오행 */

.element-area {
    display: flex;
    justify-content: center;
    gap: 9px;
    flex-wrap: wrap;
}

.element {
    padding: 10px 16px;
    border-radius: 20px;
    background: #211633;
    border: 1px solid #554067;
    color: #c9b7d8;
    font-size: 12px;
}

/* 키워드 */

.keyword-area {
    text-align: center;
    margin-top: 17px;
}

.keyword {
    display: inline-block;
    padding: 7px 13px;
    margin: 4px;
    border-radius: 18px;
    background: #2a1b3c;
    border: 1px solid #654b7d;
    color: #c9aee0;
    font-size: 11px;
}

/* 정보 카드 */

.info-grid {
    display: flex;
    gap: 13px;
    flex-wrap: wrap;
}

.info-card {
    flex: 1;
    min-width: 230px;
    background: rgba(30,21,47,.9);
    border: 1px solid #49375c;
    border-radius: 18px;
    padding: 20px;
}

.info-title {
    color: #c7a8dc;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-text {
    color: #a99daf;
    font-size: 12px;
    line-height: 1.9;
}

/* 오하아사 */

.ohasa-card {
    background:
        radial-gradient(circle at 50% 0%, rgba(192,145,225,.15), transparent 45%),
        linear-gradient(145deg, #28183c, #130d24);
    border: 1px solid rgba(205,168,235,.45);
    border-radius: 25px;
    padding: 28px 22px;
    margin-top: 28px;
    box-shadow:
        0 15px 40px rgba(0,0,0,.3),
        inset 0 0 30px rgba(190,140,220,.03);
}

.ohasa-title {
    text-align: center;
    font-family: 'Cinzel', serif;
    color: #eedfff;
    font-size: 24px;
    letter-spacing: 4px;
}

.ohasa-date {
    text-align: center;
    color: #93819f;
    font-size: 11px;
    margin-top: 8px;
    margin-bottom: 25px;
}

.rank-card {
    display: flex;
    align-items: center;
    background: rgba(255,255,255,.035);
    border: 1px solid #49365c;
    border-radius: 15px;
    padding: 13px 15px;
    margin-bottom: 8px;
}

.rank-number {
    width: 35px;
    font-family: 'Cinzel', serif;
    font-size: 17px;
    color: #cdb4e2;
}

.zodiac {
    width: 75px;
    color: #d9c5e7;
    font-size: 13px;
    font-weight: 600;
}

.rank-fortune {
    flex: 1;
    color: #94879d;
    font-size: 11px;
    line-height: 1.6;
}

.lucky {
    width: 45px;
    text-align: center;
    color: #bfa2d4;
    font-size: 10px;
}

/* 주의사항 */

.notice {
    text-align: center;
    color: #796c85;
    font-size: 10px;
    line-height: 1.8;
    margin-top: 25px;
}

.footer {
    text-align: center;
    color: #695c74;
    font-size: 10px;
    margin-top: 35px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 천간
# =========================================================

HEAVENLY = [
    ("甲", "갑", "목"),
    ("乙", "을", "목"),
    ("丙", "병", "화"),
    ("丁", "정", "화"),
    ("戊", "무", "토"),
    ("己", "기", "토"),
    ("庚", "경", "금"),
    ("辛", "신", "금"),
    ("壬", "임", "수"),
    ("癸", "계", "수")
]


# =========================================================
# 지지
# =========================================================

EARTHLY = [
    ("子", "자", "수", "쥐"),
    ("丑", "축", "토", "소"),
    ("寅", "인", "목", "호랑이"),
    ("卯", "묘", "목", "토끼"),
    ("辰", "진", "토", "용"),
    ("巳", "사", "화", "뱀"),
    ("午", "오", "화", "말"),
    ("未", "미", "토", "양"),
    ("申", "신", "금", "원숭이"),
    ("酉", "유", "금", "닭"),
    ("戌", "술", "토", "개"),
    ("亥", "해", "수", "돼지")
]


# =========================================================
# 오행 해석
# =========================================================

ELEMENT_INFO = {
    "목": {
        "emoji": "🌿",
        "name": "목(木)",
        "keyword": "성장 · 창조 · 발전",
        "personality": "새로운 것을 배우고 성장하려는 성향이 강한 편으로 해석할 수 있어요. 아이디어를 발전시키고 새로운 가능성을 찾아가는 타입이에요.",
        "love": "서로에게 좋은 영향을 주고 함께 성장하는 관계를 중요하게 생각하는 편이에요.",
        "money": "새로운 기회나 아이디어에 관심을 가질 수 있어요. 계획적으로 관리하는 습관이 도움이 돼요.",
        "study": "새로운 내용을 배우고 직접 응용해보는 공부 방식이 잘 맞을 수 있어요.",
        "career": "디자인, 기획, 교육, 콘텐츠, 연구처럼 새로운 것을 만들어내는 분야와 연결해볼 수 있어요."
    },

    "화": {
        "emoji": "🔥",
        "name": "화(火)",
        "keyword": "열정 · 표현 · 에너지",
        "personality": "자신의 생각과 감정을 표현하는 힘이 강한 편으로 볼 수 있어요. 관심이 생긴 일에는 적극적으로 에너지를 쏟는 타입이에요.",
        "love": "좋아하는 사람에게 애정을 적극적으로 표현하고 함께 즐거운 경험을 만드는 것을 좋아할 수 있어요.",
        "money": "관심 분야에는 적극적으로 돈을 쓰고 싶어질 수 있어요. 충동적인 소비를 관리하면 좋아요.",
        "study": "목표가 뚜렷할수록 집중하기 쉬워요. 짧은 목표를 정해 성취감을 얻는 방식이 잘 맞을 수 있어요.",
        "career": "마케팅, 콘텐츠, 미디어, 공연, 영업처럼 표현력을 활용하는 분야와 연결할 수 있어요."
    },

    "토": {
        "emoji": "🌙",
        "name": "토(土)",
        "keyword": "안정 · 균형 · 꾸준함",
        "personality": "주변 상황을 안정적으로 살피고 자신의 일을 꾸준하게 해나가는 성향으로 볼 수 있어요.",
        "love": "빠르게 가까워지기보다는 신뢰를 쌓으며 오래 유지되는 관계에서 편안함을 느끼기 쉬워요.",
        "money": "계획적으로 관리하고 차근차근 쌓아가는 방식과 잘 맞을 수 있어요.",
        "study": "규칙적인 생활과 일정한 공부 루틴을 만드는 것이 도움이 될 수 있어요.",
        "career": "경영, 행정, 건축, 기획, 관리처럼 체계적인 사고를 활용하는 분야와 연결할 수 있어요."
    },

    "금": {
        "emoji": "✦",
        "name": "금(金)",
        "keyword": "집중 · 기준 · 결단력",
        "personality": "자신만의 기준이 비교적 뚜렷하고 중요한 순간에 결정을 내리는 힘을 가진 성향으로 볼 수 있어요.",
        "love": "쉽게 마음을 주기보다는 상대를 충분히 알아간 뒤 진지한 관계를 만들어가는 편으로 볼 수 있어요.",
        "money": "돈을 사용할 때 효율과 자신만의 기준을 중요하게 생각하는 성향과 연결할 수 있어요.",
        "study": "목표와 결과가 명확할 때 집중하기 좋아요.",
        "career": "법률, 금융, 공학, 디자인, 분석처럼 정확성과 판단력을 활용하는 분야와 연결할 수 있어요."
    },

    "수": {
        "emoji": "💧",
        "name": "수(水)",
        "keyword": "유연함 · 지혜 · 감성",
        "personality": "상황을 관찰하고 유연하게 생각하는 성향으로 볼 수 있어요. 혼자 생각을 정리하는 시간도 중요하게 여기는 편이에요.",
        "love": "상대의 감정을 세심하게 살피며 편안하게 이야기를 나눌 수 있는 관계를 중요하게 생각할 수 있어요.",
        "money": "상황에 따라 유연하게 판단하지만 감정에 따른 소비를 관리하는 것이 도움이 될 수 있어요.",
        "study": "조용한 환경에서 자신의 속도로 생각하고 정리하는 공부 방식이 잘 맞을 수 있어요.",
        "career": "연구, 글쓰기, 콘텐츠, 상담, 예술, 데이터처럼 관찰력과 사고력을 활용하는 분야와 연결할 수 있어요."
    }
}


# =========================================================
# 사주 계산
# =========================================================

def julian_day(y, m, d):

    if m <= 2:
        y -= 1
        m += 12

    a = y // 100
    b = 2 - a + a // 4

    return (
        int(365.25 * (y + 4716))
        + int(30.6001 * (m + 1))
        + d
        + b
        - 1524
    )


def year_pillar(y, m, d):

    if m < 2 or (m == 2 and d < 4):
        y -= 1

    stem = (y - 4) % 10
    branch = (y - 4) % 12

    return stem, branch


def day_pillar(y, m, d):

    jd = julian_day(y, m, d)

    cycle = (jd + 49) % 60

    stem = cycle % 10
    branch = cycle % 12

    return stem, branch


def month_branch(m, d):

    md = m * 100 + d

    if md >= 1207 or md < 105:
        return 0
    elif md < 206:
        return 1
    elif md < 306:
        return 2
    elif md < 405:
        return 3
    elif md < 506:
        return 4
    elif md < 606:
        return 5
    elif md < 707:
        return 6
    elif md < 807:
        return 7
    elif md < 907:
        return 8
    elif md < 1008:
        return 9
    elif md < 1107:
        return 10
    else:
        return 11


def month_pillar(y, m, d):

    year_stem, _ = year_pillar(y, m, d)

    branch = month_branch(m, d)

    month_order = (branch - 2) % 12

    starting_stem = {
        0: 2,
        1: 4,
        2: 6,
        3: 8,
        4: 0
    }

    stem_start = starting_stem[year_stem % 5]

    stem = (stem_start + month_order) % 10

    return stem, branch


def hour_branch(hour):

    if hour >= 23 or hour < 1:
        return 0

    return ((hour + 1) // 2) % 12


def hour_pillar(day_stem, hour):

    branch = hour_branch(hour)

    starting_stem = {
        0: 0,
        1: 2,
        2: 4,
        3: 6,
        4: 8
    }

    stem = (
        starting_stem[day_stem % 5]
        + branch
    ) % 10

    return stem, branch


# =========================================================
# 사주 기둥 HTML
# =========================================================

def pillar_html(name, stem_index, branch_index):

    stem_hanja = HEAVENLY[stem_index][0]
    stem_korean = HEAVENLY[stem_index][1]
    stem_element = HEAVENLY[stem_index][2]

    branch_hanja = EARTHLY[branch_index][0]
    branch_korean = EARTHLY[branch_index][1]
    branch_element = EARTHLY[branch_index][2]
    animal = EARTHLY[branch_index][3]

    return (
        '<div class="pillar">'
        f'<div class="pillar-name">{name}</div>'
        f'<div class="heaven">{stem_hanja}</div>'
        f'<div class="pillar-info">{stem_korean} · {stem_element}</div>'
        f'<div class="earth">{branch_hanja}</div>'
        f'<div class="pillar-info">{branch_korean} · {branch_element}</div>'
        f'<div class="pillar-info">{animal}띠</div>'
        '</div>'
    )


# =========================================================
# 별자리 정보
# =========================================================

ZODIAC = [
    ("♈", "양자리"),
    ("♉", "황소자리"),
    ("♊", "쌍둥이자리"),
    ("♋", "게자리"),
    ("♌", "사자자리"),
    ("♍", "처녀자리"),
    ("♎", "천칭자리"),
    ("♏", "전갈자리"),
    ("♐", "사수자리"),
    ("♑", "염소자리"),
    ("♒", "물병자리"),
    ("♓", "물고기자리")
]


# =========================================================
# 오늘의 오하아사 운세 데이터
# =========================================================

OHASA_FORTUNES = [
    "작은 행운이 연달아 찾아오는 날이에요.",
    "평소 지나쳤던 곳에서 좋은 기회를 발견할 수 있어요.",
    "오늘은 먼저 말을 걸어보면 좋은 일이 생길 수 있어요.",
    "집중력이 좋아지는 날. 미뤄둔 일을 시작해보세요.",
    "새로운 아이디어가 빛을 발하는 날이에요.",
    "친구나 주변 사람에게서 뜻밖의 도움을 받을 수 있어요.",
    "오늘은 서두르기보다 천천히 결정하는 것이 좋아요.",
    "오랫동안 고민했던 일이 의외로 쉽게 풀릴 수 있어요.",
    "자신감을 가지고 행동하면 분위기가 달라질 수 있어요.",
    "작은 실수가 오히려 새로운 기회로 이어질 수 있어요.",
    "오늘은 자신의 취향과 감각을 믿어보세요.",
    "좋아하는 일에 시간을 쓰면 기분 좋은 에너지가 생겨요."
]


LUCKY_ITEMS = [
    "보라색 소품",
    "작은 액세서리",
    "이어폰",
    "향수",
    "노트",
    "실버 아이템",
    "헤어 액세서리",
    "책",
    "립밤",
    "반지",
    "키링",
    "작은 거울"
]


def get_ohasa():

    today = date.today()

    # 날짜를 seed로 사용해 하루 동안은 같은 결과
    seed = (
        today.year * 10000
        + today.month * 100
        + today.day
    )

    rng = random.Random(seed)

    ranking = list(range(12))
    rng.shuffle(ranking)

    results = []

    for rank, zodiac_index in enumerate(ranking, start=1):

        fortune = OHASA_FORTUNES[
            rng.randrange(len(OHASA_FORTUNES))
        ]

        lucky = LUCKY_ITEMS[
            rng.randrange(len(LUCKY_ITEMS))
        ]

        results.append({
            "rank": rank,
            "symbol": ZODIAC[zodiac_index][0],
            "name": ZODIAC[zodiac_index][1],
            "fortune": fortune,
            "lucky": lucky
        })

    return results


# =========================================================
# 제목
# =========================================================

st.markdown(
    '<div class="stars">✦　✧　✦　✧　✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="moon">☾</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">MYSTIC SAJU</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">YOUR DESTINY · YOUR LITTLE UNIVERSE</div>',
    unsafe_allow_html=True
)


# =========================================================
# 출생 정보
# =========================================================

st.markdown(
    '<div class="input-box">'
    '<div class="input-title">✦ ENTER YOUR BIRTH INFORMATION ✦</div>'
    '</div>',
    unsafe_allow_html=True
)

birth_date = st.date_input(
    "생년월일",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date(2020, 12, 31),
    format="YYYY-MM-DD"
)


# =========================================================
# 출생 시간
# =========================================================

time_options = [
    "모름",
    "00:00 ~ 00:59",
    "01:00 ~ 02:59",
    "03:00 ~ 04:59",
    "05:00 ~ 06:59",
    "07:00 ~ 08:59",
    "09:00 ~ 10:59",
    "11:00 ~ 12:59",
    "13:00 ~ 14:59",
    "15:00 ~ 16:59",
    "17:00 ~ 18:59",
    "19:00 ~ 20:59",
    "21:00 ~ 22:59",
    "23:00 ~ 23:59"
]

birth_time = st.selectbox(
    "태어난 시각",
    time_options
)


# =========================================================
# 날짜 변수
# =========================================================

y = birth_date.year
m = birth_date.month
d = birth_date.day


# =========================================================
# 사주 계산
# =========================================================

year_stem, year_branch = year_pillar(y, m, d)

month_stem, month_branch_index = month_pillar(
    y, m, d
)

day_stem, day_branch = day_pillar(
    y, m, d
)


# =========================================================
# 시주
# =========================================================

has_hour = birth_time != "모름"

if has_hour:

    if birth_time == "00:00 ~ 00:59":
        hour = 0
    elif birth_time == "01:00 ~ 02:59":
        hour = 1
    elif birth_time == "03:00 ~ 04:59":
        hour = 3
    elif birth_time == "05:00 ~ 06:59":
        hour = 5
    elif birth_time == "07:00 ~ 08:59":
        hour = 7
    elif birth_time == "09:00 ~ 10:59":
        hour = 9
    elif birth_time == "11:00 ~ 12:59":
        hour = 11
    elif birth_time == "13:00 ~ 14:59":
        hour = 13
    elif birth_time == "15:00 ~ 16:59":
        hour = 15
    elif birth_time == "17:00 ~ 18:59":
        hour = 17
    elif birth_time == "19:00 ~ 20:59":
        hour = 19
    elif birth_time == "21:00 ~ 22:59":
        hour = 21
    else:
        hour = 23

    hour_stem, hour_branch_index = hour_pillar(
        day_stem,
        hour
    )

else:

    hour_stem = None
    hour_branch_index = None


# =========================================================
# 오행
# =========================================================

elements = [
    HEAVENLY[year_stem][2],
    EARTHLY[year_branch][2],
    HEAVENLY[month_stem][2],
    EARTHLY[month_branch_index][2],
    HEAVENLY[day_stem][2],
    EARTHLY[day_branch][2]
]

if has_hour:

    elements.append(
        HEAVENLY[hour_stem][2]
    )

    elements.append(
        EARTHLY[hour_branch_index][2]
    )


element_count = {}

for element in ["목", "화", "토", "금", "수"]:
    element_count[element] = elements.count(element)


# =========================================================
# 중심 오행
# =========================================================

main_element = HEAVENLY[day_stem][2]

info = ELEMENT_INFO[main_element]


# =========================================================
# 오행 HTML
# =========================================================

element_emoji = {
    "목": "🌿",
    "화": "🔥",
    "토": "🌙",
    "금": "✦",
    "수": "💧"
}

element_html = ""

for element in ["목", "화", "토", "금", "수"]:

    element_html += (
        '<div class="element">'
        f'{element_emoji[element]} '
        f'{element} {element_count[element]}'
        '</div>'
    )


# =========================================================
# 사주 기둥
# =========================================================

pillars = ""

pillars += pillar_html(
    "년주 年柱",
    year_stem,
    year_branch
)

pillars += pillar_html(
    "월주 月柱",
    month_stem,
    month_branch_index
)

pillars += pillar_html(
    "일주 日柱",
    day_stem,
    day_branch
)

if has_hour:

    pillars += pillar_html(
        "시주 時柱",
        hour_stem,
        hour_branch_index
    )

else:

    pillars += (
        '<div class="pillar">'
        '<div class="pillar-name">시주 時柱</div>'
        '<div class="heaven">—</div>'
        '<div class="pillar-info">출생 시각 모름</div>'
        '<div class="earth">—</div>'
        '<div class="pillar-info">확인할 수 없음</div>'
        '</div>'
    )


# =========================================================
# 사주팔자 8글자
# =========================================================

eight_chars = (
    HEAVENLY[year_stem][0]
    + HEAVENLY[month_stem][0]
    + HEAVENLY[day_stem][0]
    + (
        HEAVENLY[hour_stem][0]
        if has_hour else "?"
    )
    + EARTHLY[year_branch][0]
    + EARTHLY[month_branch_index][0]
    + EARTHLY[day_branch][0]
    + (
        EARTHLY[hour_branch_index][0]
        if has_hour else "?"
    )
)


# =========================================================
# 사주 결과
# =========================================================

st.markdown(
    '<div class="result-card">'
    '<div class="card-symbol">☯</div>'
    '<div class="card-title">YOUR FOUR PILLARS</div>'
    f'<div class="card-subtitle">'
    f'{y}년 {m}월 {d}일 · '
    f'{"출생 시각 확인" if has_hour else "출생 시각 모름"}'
    '</div>'
    f'<div class="pillars">{pillars}</div>'
    '<div class="divider"></div>'
    '<div class="eight-title">✦ THE EIGHT CHARACTERS ✦</div>'
    f'<div class="eight-text">{eight_chars}</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 오행
# =========================================================

st.markdown(
    '<div class="result-card">'
    '<div class="section-title">☯ THE FIVE ELEMENTS</div>'
    f'<div class="element-area">{element_html}</div>'
    '<div class="keyword-area">'
    f'<span class="keyword">'
    f'{info["emoji"]} 중심 오행 · {info["name"]}'
    '</span>'
    f'<span class="keyword">'
    f'✦ {info["keyword"]}'
    '</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 기본 성향
# =========================================================

st.markdown(
    '<div class="result-card">'
    '<div class="section-title">☾ YOUR NATURE</div>'
    '<div class="info-card">'
    f'<div class="info-title">'
    f'{info["emoji"]} {info["keyword"]}'
    '</div>'
    f'<div class="info-text">'
    f'{info["personality"]}'
    '</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 연애 / 금전
# =========================================================

st.markdown(
    '<div class="result-card">'
    '<div class="section-title">♡ LOVE & MONEY</div>'
    '<div class="info-grid">'

    '<div class="info-card">'
    '<div class="info-title">♡ 연애운</div>'
    f'<div class="info-text">{info["love"]}</div>'
    '</div>'

    '<div class="info-card">'
    '<div class="info-title">✦ 금전운</div>'
    f'<div class="info-text">{info["money"]}</div>'
    '</div>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 학업 / 진로
# =========================================================

st.markdown(
    '<div class="result-card">'
    '<div class="section-title">✧ STUDY & DESTINY</div>'
    '<div class="info-grid">'

    '<div class="info-card">'
    '<div class="info-title">📖 학업운</div>'
    f'<div class="info-text">{info["study"]}</div>'
    '</div>'

    '<div class="info-card">'
    '<div class="info-title">✦ 진로 · 적성</div>'
    f'<div class="info-text">{info["career"]}</div>'
    '</div>'

    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 인간관계 / 강점 / 주의점
# =========================================================

relationship_text = {
    "목": "사람들과 함께 성장하고 서로의 생각을 나누는 관계를 편하게 느낄 수 있어요.",
    "화": "밝고 적극적인 관계를 만들기 쉬우며 주변에 활기를 더하는 역할을 할 수 있어요.",
    "토": "오래 알고 지낸 사람들과의 안정적인 관계를 중요하게 생각하는 편으로 볼 수 있어요.",
    "금": "사람을 대할 때 자신만의 기준이 있으며 믿을 수 있는 관계를 중요하게 생각할 수 있어요.",
    "수": "상대방의 감정을 세심하게 살피며 깊이 있는 관계를 만들어가는 편으로 볼 수 있어요."
}

strength_text = {
    "목": "새로운 가능성을 발견하고 꾸준히 발전시키는 힘",
    "화": "자신의 에너지와 생각을 적극적으로 표현하는 힘",
    "토": "쉽게 흔들리지 않고 꾸준하게 해내는 힘",
    "금": "중요한 순간에 판단하고 집중하는 힘",
    "수": "상황을 관찰하고 유연하게 대처하는 힘"
}

caution_text = {
    "목": "새로운 것을 너무 많이 시작하기보다 하나씩 끝까지 완성하는 습관을 만들어보세요.",
    "화": "하고 싶은 마음이 생겼을 때 속도를 조금 늦추고 한 번 더 생각해보는 것도 좋아요.",
    "토": "안정적인 것을 중요하게 생각하더라도 새로운 경험을 지나치게 피하지 않는 것이 좋아요.",
    "금": "자신의 기준만큼 다른 사람의 방식도 존중해주면 관계가 더욱 편안해질 수 있어요.",
    "수": "생각이 너무 많아지지 않도록 혼자 고민하기보다 주변 사람에게 이야기해보는 것도 좋아요."
}


st.markdown(
    '<div class="result-card">'
    '<div class="section-title">✦ YOUR INNER WORLD</div>'

    '<div class="info-grid">'

    '<div class="info-card">'
    '<div class="info-title">♡ 인간관계</div>'
    f'<div class="info-text">'
    f'{relationship_text[main_element]}'
    '</div>'
    '</div>'

    '<div class="info-card">'
    '<div class="info-title">✦ 나의 강점</div>'
    f'<div class="info-text">'
    f'{strength_text[main_element]}'
    '</div>'
    '</div>'

    '</div>'

    '<br>'

    '<div class="info-card">'
    '<div class="info-title">☾ 알아두면 좋은 점</div>'
    f'<div class="info-text">'
    f'{caution_text[main_element]}'
    '</div>'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 오늘의 오하아사
# =========================================================

ohasa_results = get_ohasa()

rank_html = ""

for result in ohasa_results:

    rank_html += (
        '<div class="rank-card">'

        f'<div class="rank-number">'
        f'{result["rank"]}'
        '</div>'

        f'<div class="zodiac">'
        f'{result["symbol"]} {result["name"]}'
        '</div>'

        f'<div class="rank-fortune">'
        f'{result["fortune"]}'
        '</div>'

        f'<div class="lucky">'
        f'🍀<br>{result["lucky"]}'
        '</div>'

        '</div>'
    )


st.markdown(
    '<div class="ohasa-card">'

    '<div class="ohasa-title">'
    'TODAY\'S OHASA'
    '</div>'

    f'<div class="ohasa-date">'
    f'{date.today().strftime("%Y.%m.%d")} · 오늘의 별자리 운세'
    '</div>'

    f'{rank_html}'

    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 출생 시각 안내
# =========================================================

if not has_hour:

    st.markdown(
        '<div class="notice">'
        '☾ 태어난 시각을 모르는 경우에는 년주 · 월주 · 일주를 기준으로 표시했어요.<br>'
        '시주는 출생 시간이 있어야 계산할 수 있기 때문에 임의로 추정하지 않았어요.'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 주의사항
# =========================================================

st.markdown(
    '<div class="notice">'
    '※ 사주와 오늘의 오하아사는 전통적인 개념을 바탕으로 만든 '
    '재미·참고용 콘텐츠예요.<br>'
    '※ 사주 계산은 절기 시각 등을 단순화한 방식이므로 실제 만세력과 차이가 있을 수 있어요.<br>'
    '※ 오늘의 오하아사는 이 앱에서 생성한 오리지널 별자리 운세입니다.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 푸터
# =========================================================

st.markdown(
    '<div class="footer">'
    '✦ ☾ ✧ MYSTIC SAJU ✧ ☽ ✦'
    '</div>',
    unsafe_allow_html=True
)