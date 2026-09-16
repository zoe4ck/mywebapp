import streamlit as st
from datetime import date

# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="나의 사주팔자",
    page_icon="🌙",
    layout="centered"
)

# =========================================================
# 디자인
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 8% 8%, rgba(255, 215, 232, .85), transparent 25%),
        radial-gradient(circle at 92% 15%, rgba(226, 216, 255, .85), transparent 27%),
        radial-gradient(circle at 50% 90%, rgba(255, 236, 244, .8), transparent 30%),
        linear-gradient(180deg, #fffafd 0%, #f8f4ff 100%);
    color: #55495b;
}

.block-container {
    max-width: 900px;
    padding-top: 40px;
    padding-bottom: 70px;
}

/* 제목 */

.moon {
    text-align: center;
    font-size: 58px;
    margin-bottom: 3px;
}

.title {
    text-align: center;
    color: #9876b8;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: 3px;
}

.subtitle {
    text-align: center;
    color: #aaa0b1;
    font-size: 14px;
    margin-top: 9px;
    margin-bottom: 35px;
}

/* 입력 카드 */

.input-card {
    background: rgba(255,255,255,.9);
    border: 2px solid #eadbed;
    border-radius: 26px;
    padding: 27px 30px 20px 30px;
    box-shadow: 0 12px 35px rgba(160,130,180,.12);
}

.input-title {
    text-align: center;
    color: #8f70ae;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 20px;
}

div[data-testid="stDateInput"] input {
    height: 48px !important;
    font-size: 15px !important;
    border-radius: 13px !important;
}

div[data-testid="stSelectbox"] > div {
    border-radius: 13px;
}

/* 결과 카드 */

.saju-card {
    background: rgba(255,255,255,.95);
    border: 2px solid #ead8ef;
    border-radius: 30px;
    padding: 34px 28px;
    margin-top: 30px;
    box-shadow: 0 14px 38px rgba(150,120,175,.14);
}

.card-symbol {
    text-align: center;
    font-size: 50px;
}

.card-title {
    text-align: center;
    color: #9270b0;
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

.card-subtitle {
    text-align: center;
    color: #aaa0b0;
    font-size: 13px;
    margin-top: 8px;
}

/* 사주 네 기둥 */

.pillars {
    display: flex;
    justify-content: center;
    gap: 13px;
    margin-top: 30px;
    flex-wrap: wrap;
}

.pillar {
    width: 165px;
    min-height: 220px;
    background: linear-gradient(180deg, #fffaff, #f8f0fb);
    border: 1.5px solid #decbe8;
    border-radius: 23px;
    text-align: center;
    padding: 18px 10px;
    box-sizing: border-box;
}

.pillar-name {
    color: #a184b8;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 15px;
}

.heaven {
    font-size: 38px;
    font-weight: 800;
    color: #66546f;
}

.earth {
    font-size: 38px;
    font-weight: 800;
    color: #9b6e9e;
    margin-top: 8px;
}

.korean {
    font-size: 11px;
    color: #aaa0ad;
    margin-top: 8px;
}

/* 팔자 */

.eight-title {
    text-align: center;
    color: #9270b0;
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 10px;
}

.eight-text {
    text-align: center;
    color: #6e6075;
    font-size: 25px;
    letter-spacing: 8px;
    font-weight: 700;
}

/* 구분선 */

.divider {
    width: 90%;
    height: 1px;
    margin: 30px auto;
    background: linear-gradient(
        90deg,
        transparent,
        #dfc8e7,
        transparent
    );
}

/* 섹션 */

.section-title {
    text-align: center;
    color: #9270b0;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 20px;
}

.section-grid {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.little-card {
    flex: 1;
    min-width: 230px;
    background: #fff8fb;
    border: 1px solid #f0dce8;
    border-radius: 21px;
    padding: 20px;
}

.little-title {
    color: #d17c9d;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 9px;
}

.little-text {
    color: #685c6d;
    font-size: 13px;
    line-height: 1.85;
}

/* 오행 */

.element-area {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
}

.element {
    padding: 10px 16px;
    border-radius: 20px;
    background: #fbf4fc;
    border: 1px solid #e3d4ea;
    color: #75627d;
    font-size: 13px;
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
    background: #fff1f7;
    border: 1px solid #f0cfde;
    color: #d27498;
    font-size: 12px;
}

/* 안내 */

.notice {
    text-align: center;
    color: #aaa0ae;
    font-size: 11px;
    line-height: 1.8;
    margin-top: 28px;
}

.footer {
    text-align: center;
    color: #b5a8ba;
    font-size: 11px;
    margin-top: 38px;
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
        "emoji": "🌱",
        "name": "목(木)",
        "keyword": "성장 · 창조 · 발전",

        "personality":
            "새로운 것을 배우고 성장하려는 성향이 강한 편으로 해석할 수 있어요. "
            "아이디어를 발전시키고 새로운 가능성을 찾아가는 것을 좋아하는 타입이에요.",

        "love":
            "연애에서도 서로에게 좋은 영향을 주고 함께 성장하는 관계를 중요하게 생각하는 편이에요.",

        "money":
            "새로운 기회나 아이디어를 활용하는 데 관심을 가질 수 있어요. "
            "계획을 세우고 꾸준히 관리하는 습관이 도움이 돼요.",

        "study":
            "새로운 내용을 배우고 직접 응용해보는 공부 방식이 잘 맞을 수 있어요.",

        "career":
            "디자인, 기획, 교육, 콘텐츠, 연구처럼 새로운 것을 만들어내고 발전시키는 분야와 연결해볼 수 있어요."
    },

    "화": {
        "emoji": "🔥",
        "name": "화(火)",
        "keyword": "열정 · 표현 · 에너지",

        "personality":
            "자신의 생각과 감정을 표현하는 힘이 강한 편으로 볼 수 있어요. "
            "관심이 생긴 일에는 적극적으로 에너지를 쏟는 타입이에요.",

        "love":
            "좋아하는 사람에게 애정을 비교적 적극적으로 표현하고 "
            "함께 즐거운 경험을 만드는 것을 좋아하는 편이에요.",

        "money":
            "자신이 관심을 가지는 분야에는 적극적으로 투자하고 싶어질 수 있어요. "
            "충동적인 소비를 관리하면 좋아요.",

        "study":
            "목표가 뚜렷할수록 집중력이 올라가기 쉬워요. "
            "짧은 목표를 정해 성취감을 얻는 방식이 잘 맞을 수 있어요.",

        "career":
            "마케팅, 공연, 콘텐츠, 미디어, 영업처럼 표현력과 활동성을 활용하는 분야와 연결할 수 있어요."
    },

    "토": {
        "emoji": "🌷",
        "name": "토(土)",
        "keyword": "안정 · 균형 · 꾸준함",

        "personality":
            "주변 상황을 안정적으로 살피고 꾸준하게 자신의 일을 해나가는 성향으로 볼 수 있어요.",

        "love":
            "빠르게 가까워지기보다는 신뢰를 쌓으면서 오래 유지되는 관계에서 편안함을 느끼기 쉬워요.",

        "money":
            "한 번에 큰 변화를 만들기보다 계획적으로 관리하고 차근차근 쌓아가는 방식과 잘 맞을 수 있어요.",

        "study":
            "규칙적인 생활과 일정한 공부 루틴을 만드는 것이 도움이 될 수 있어요.",

        "career":
            "경영, 행정, 건축, 기획, 관리처럼 안정성과 체계적인 사고를 활용하는 분야와 연결할 수 있어요."
    },

    "금": {
        "emoji": "✨",
        "name": "금(金)",
        "keyword": "집중 · 기준 · 결단력",

        "personality":
            "자신만의 기준이 비교적 뚜렷하고 중요한 순간에 결정을 내리는 힘을 가진 성향으로 볼 수 있어요.",

        "love":
            "쉽게 마음을 주기보다는 상대방을 충분히 알아간 뒤 진지한 관계를 만들어가는 편으로 볼 수 있어요.",

        "money":
            "돈을 사용할 때 나름의 기준을 세우고 효율을 중요하게 생각하는 성향과 연결할 수 있어요.",

        "study":
            "목표와 결과가 명확할 때 집중하기 좋아요. "
            "공부할 내용을 구체적으로 나누면 도움이 될 수 있어요.",

        "career":
            "법률, 금융, 공학, 디자인, 분석처럼 정확성과 판단력을 활용하는 분야와 연결할 수 있어요."
    },

    "수": {
        "emoji": "💧",
        "name": "수(水)",
        "keyword": "유연함 · 지혜 · 감성",

        "personality":
            "상황을 관찰하고 유연하게 생각하는 성향으로 볼 수 있어요. "
            "혼자 생각을 정리하는 시간도 중요하게 여기는 편이에요.",

        "love":
            "상대방의 감정을 세심하게 살피며 편안하게 이야기를 나눌 수 있는 관계를 중요하게 생각하는 편이에요.",

        "money":
            "상황에 따라 유연하게 판단하는 편이지만, "
            "감정에 따른 소비와 계획 없는 지출을 구분하는 것이 도움이 될 수 있어요.",

        "study":
            "조용한 환경에서 자신의 속도로 생각하고 정리하는 공부 방식이 잘 맞을 수 있어요.",

        "career":
            "연구, 글쓰기, 콘텐츠, 상담, 예술, 데이터처럼 관찰력과 사고력을 활용하는 분야와 연결할 수 있어요."
    }
}


# =========================================================
# 계산 함수
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

    # 간단한 입춘 기준
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

    stem_hanja, stem_korean, stem_element = HEAVENLY[stem_index]

    branch_hanja, branch_korean, branch_element, animal = \
        EARTHLY[branch_index]

    return f"""
    <div class="pillar">

        <div class="pillar-name">
            {name}
        </div>

        <div class="heaven">
            {stem_hanja}
        </div>

        <div class="korean">
            {stem_korean} · {stem_element}
        </div>

        <div class="earth">
            {branch_hanja}
        </div>

        <div class="korean">
            {branch_korean} · {branch_element}
        </div>

        <div class="korean">
            {animal}띠
        </div>

    </div>
    """


# =========================================================
# 제목
# =========================================================

st.markdown(
    '<div class="moon">🌙</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">나의 사주팔자</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '생년월일과 태어난 시간으로 알아보는 나만의 四柱八字'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 출생 정보 입력
# =========================================================

st.markdown(
    '<div class="input-card">'
    '<div class="input-title">'
    '🌷 나의 출생 정보를 입력해주세요'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# 1900년 ~ 2020년
birth_date = st.date_input(
    "생년월일",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date(2020, 12, 31),
    format="YYYY-MM-DD"
)


# =========================================================
# 태어난 시각
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
# 날짜
# =========================================================

y = birth_date.year
m = birth_date.month
d = birth_date.day


# =========================================================
# 년주 / 월주 / 일주
# =========================================================

year_stem, year_branch = year_pillar(y, m, d)

month_stem, month_branch_index = month_pillar(y, m, d)

day_stem, day_branch = day_pillar(y, m, d)


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
# 오행 계산
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
# 오행 표시
# =========================================================

element_emoji = {
    "목": "🌱",
    "화": "🔥",
    "토": "🌷",
    "금": "✨",
    "수": "💧"
}

element_html = ""

for element in ["목", "화", "토", "금", "수"]:

    element_html += f"""
    <div class="element">
        {element_emoji[element]}
        {element} {element_count[element]}
    </div>
    """


# =========================================================
# 사주 기둥
# =========================================================

if has_hour:

    pillars = (
        pillar_html("년주 年柱", year_stem, year_branch)
        + pillar_html(
            "월주 月柱",
            month_stem,
            month_branch_index
        )
        + pillar_html(
            "일주 日柱",
            day_stem,
            day_branch
        )
        + pillar_html(
            "시주 時柱",
            hour_stem,
            hour_branch_index
        )
    )

else:

    pillars = (
        pillar_html(
            "년주 年柱",
            year_stem,
            year_branch
        )
        + pillar_html(
            "월주 月柱",
            month_stem,
            month_branch_index
        )
        + pillar_html(
            "일주 日柱",
            day_stem,
            day_branch
        )
        + """
        <div class="pillar">

            <div class="pillar-name">
                시주 時柱
            </div>

            <div class="heaven">
                —
            </div>

            <div class="korean">
                출생 시각 모름
            </div>

            <div class="earth">
                —
            </div>

            <div class="korean">
                확인할 수 없음
            </div>

        </div>
        """
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
# 사주팔자 결과
# =========================================================

st.markdown(
    f"""
    <div class="saju-card">

        <div class="card-symbol">
            {info["emoji"]}
        </div>

        <div class="card-title">
            나의 사주팔자
        </div>

        <div class="card-subtitle">
            {y}년 {m}월 {d}일 ·
            {"출생 시각 확인" if has_hour else "출생 시각 모름"}
        </div>

        <div class="pillars">
            {pillars}
        </div>

        <div class="divider"></div>

        <div class="eight-title">
            ✦ 나의 사주팔자 여덟 글자 ✦
        </div>

        <div class="eight-text">
            {eight_chars}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 오행
# =========================================================

st.markdown(
    f"""
    <div class="saju-card">

        <div class="section-title">
            ☯️ 오행의 구성
        </div>

        <div class="element-area">
            {element_html}
        </div>

        <div class="keyword-area">

            <span class="keyword">
                {info["emoji"]}
                중심 오행 · {info["name"]}
            </span>

            <span class="keyword">
                ✦ {info["keyword"]}
            </span>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 기본 성향
# =========================================================

st.markdown(
    f"""
    <div class="saju-card">

        <div class="section-title">
            🌷 나의 기본 성향
        </div>

        <div class="little-card">

            <div class="little-title">
                {info["emoji"]} {info["keyword"]}
            </div>

            <div class="little-text">
                {info["personality"]}
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 연애 / 금전 / 학업 / 진로
# =========================================================

st.markdown(
    f"""
    <div class="saju-card">

        <div class="section-title">
            💗 나의 생활 스타일
        </div>

        <div class="section-grid">

            <div class="little-card">

                <div class="little-title">
                    💗 연애
                </div>

                <div class="little-text">
                    {info["love"]}
                </div>

            </div>

            <div class="little-card">

                <div class="little-title">
                    💰 금전
                </div>

                <div class="little-text">
                    {info["money"]}
                </div>

            </div>

        </div>

        <br>

        <div class="section-grid">

            <div class="little-card">

                <div class="little-title">
                    📚 학업
                </div>

                <div class="little-text">
                    {info["study"]}
                </div>

            </div>

            <div class="little-card">

                <div class="little-title">
                    🎨 진로 · 적성
                </div>

                <div class="little-text">
                    {info["career"]}
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 인간관계 / 강점 / 주의점
# =========================================================

relationship_text = {
    "목":
        "사람들과 함께 성장하고 서로의 생각을 나누는 관계를 편하게 느낄 수 있어요.",

    "화":
        "밝고 적극적인 관계를 만들기 쉬우며 주변에 활기를 더하는 역할을 할 수 있어요.",

    "토":
        "오래 알고 지낸 사람들과의 안정적인 관계를 중요하게 생각하는 편으로 볼 수 있어요.",

    "금":
        "사람을 대할 때 자신만의 기준이 있으며 믿을 수 있는 관계를 중요하게 생각할 수 있어요.",

    "수":
        "상대방의 감정을 세심하게 살피며 깊이 있는 관계를 만들어가는 편으로 볼 수 있어요."
}

strength_text = {
    "목":
        "새로운 가능성을 발견하고 꾸준히 발전시키는 힘",

    "화":
        "자신의 에너지와 생각을 적극적으로 표현하는 힘",

    "토":
        "쉽게 흔들리지 않고 꾸준하게 해내는 힘",

    "금":
        "중요한 순간에 판단하고 집중하는 힘",

    "수":
        "상황을 관찰하고 유연하게 대처하는 힘"
}

caution_text = {
    "목":
        "새로운 것을 너무 많이 시작하기보다 하나씩 끝까지 완성하는 습관을 만들어보세요.",

    "화":
        "하고 싶은 마음이 생겼을 때 속도를 조금 늦추고 한 번 더 생각해보는 것도 좋아요.",

    "토":
        "안정적인 것을 중요하게 생각하더라도 새로운 경험을 지나치게 피하지 않는 것이 좋아요.",

    "금":
        "자신의 기준만큼 다른 사람의 방식도 존중해주면 관계가 더욱 편안해질 수 있어요.",

    "수":
        "생각이 너무 많아지지 않도록 혼자 고민하기보다 주변 사람에게 이야기해보는 것도 좋아요."
}


st.markdown(
    f"""
    <div class="saju-card">

        <div class="section-title">
            🫶 관계와 나의 특징
        </div>

        <div class="section-grid">

            <div class="little-card">

                <div class="little-title">
                    🫶 인간관계
                </div>

                <div class="little-text">
                    {relationship_text[main_element]}
                </div>

            </div>

            <div class="little-card">

                <div class="little-title">
                    ✨ 나의 강점
                </div>

                <div class="little-text">
                    {strength_text[main_element]}
                </div>

            </div>

        </div>

        <div class="little-card" style="margin-top:14px;">

            <div class="little-title">
                🌙 알아두면 좋은 점
            </div>

            <div class="little-text">
                {caution_text[main_element]}
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 출생 시각을 모른 경우
# =========================================================

if not has_hour:

    st.markdown(
        """
        <div class="notice">

            🌙 태어난 시각을 모르는 경우에는
            년주 · 월주 · 일주를 기준으로 표시했어요.<br>

            시주는 출생 시간이 있어야 계산할 수 있기 때문에
            임의로 추정하지 않았어요.

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 하단
# =========================================================

st.markdown(
    """
    <div class="notice">
        ※ 이 웹앱의 해석은 전통적인 사주 개념을 바탕으로 한
        재미·참고용 콘텐츠예요.
    </div>

    <div class="footer">
        🌙 四柱八字 · 나만의 작은 우주를 들여다보기 ♡
    </div>
    """,
    unsafe_allow_html=True
)
