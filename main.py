import streamlit as st
from datetime import date, time

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
        radial-gradient(circle at 15% 10%, rgba(255, 214, 231, .8), transparent 25%),
        radial-gradient(circle at 85% 20%, rgba(224, 216, 255, .8), transparent 25%),
        linear-gradient(180deg, #fff9fc 0%, #f9f5ff 100%);
    color: #514757;
}

.block-container {
    max-width: 820px;
    padding-top: 40px;
    padding-bottom: 60px;
}

/* 제목 */

.moon {
    text-align: center;
    font-size: 55px;
    margin-bottom: 4px;
}

.title {
    text-align: center;
    color: #9a78bd;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: 3px;
}

.subtitle {
    text-align: center;
    color: #a99caf;
    font-size: 13px;
    margin-top: 8px;
    margin-bottom: 30px;
}

/* 입력 */

.input-card {
    background: rgba(255,255,255,.88);
    border: 1.5px solid #ead9ef;
    border-radius: 25px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(150,120,170,.12);
}

.input-title {
    text-align: center;
    color: #8f70ad;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 18px;
}

/* 사주 결과 */

.saju-card {
    background: rgba(255,255,255,.94);
    border: 2px solid #ead8ee;
    border-radius: 28px;
    padding: 30px 25px;
    margin-top: 30px;
    box-shadow: 0 12px 35px rgba(150,120,170,.13);
}

.card-title {
    text-align: center;
    color: #9270b0;
    font-size: 25px;
    font-weight: 800;
}

.card-subtitle {
    text-align: center;
    color: #aaa0b0;
    font-size: 13px;
    margin-top: 7px;
}

/* 네 기둥 */

.pillars {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 28px;
    flex-wrap: wrap;
}

.pillar {
    width: 145px;
    min-height: 205px;
    background: linear-gradient(180deg, #fffafd, #f8f1fc);
    border: 1.5px solid #dfcce8;
    border-radius: 22px;
    text-align: center;
    padding: 17px 10px;
    box-sizing: border-box;
}

.pillar-name {
    color: #a185b8;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
}

.heaven {
    font-size: 34px;
    font-weight: 800;
    color: #6e597a;
}

.earth {
    font-size: 34px;
    font-weight: 800;
    color: #9b6f9c;
    margin-top: 8px;
}

.korean {
    font-size: 11px;
    color: #aaa0ad;
    margin-top: 10px;
}

.divider {
    width: 80%;
    height: 1px;
    margin: 30px auto;
    background: linear-gradient(
        90deg,
        transparent,
        #dfc7e5,
        transparent
    );
}

/* 오행 */

.section-title {
    text-align: center;
    color: #8d6ca8;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 15px;
}

.element-area {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
}

.element {
    padding: 9px 14px;
    border-radius: 18px;
    background: #fbf4fc;
    border: 1px solid #e5d6eb;
    color: #75637c;
    font-size: 13px;
}

/* 안내 */

.notice {
    text-align: center;
    color: #aaa0ae;
    font-size: 11px;
    line-height: 1.7;
    margin-top: 25px;
}

.footer {
    text-align: center;
    color: #b4a7b9;
    font-size: 11px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 천간 / 지지
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
# 날짜 계산
# =========================================================

def julian_day(y, m, d):
    """
    Gregorian 날짜의 Julian Day 계산
    """
    if m <= 2:
        y -= 1
        m += 12

    a = y // 100
    b = 2 - a + a // 4

    return (
        int(365.25 * (y + 4716))
        + int(30.6001 * (m + 1))
        + d + b - 1524
    )


def day_pillar(y, m, d):
    """
    일주 계산.
    전통적인 60갑자 순환을 기준으로 계산.
    """

    jd = julian_day(y, m, d)

    # 갑자일 기준 보정
    cycle = (jd + 49) % 60

    stem_index = cycle % 10
    branch_index = cycle % 12

    return stem_index, branch_index


# =========================================================
# 년주
# =========================================================

def year_pillar(y, m, d):
    """
    입춘 이전 출생은 전년도 간지를 사용.
    입춘은 단순화를 위해 2월 4일 기준.
    """

    if m < 2 or (m == 2 and d < 4):
        y -= 1

    stem = (y - 4) % 10
    branch = (y - 4) % 12

    return stem, branch


# =========================================================
# 월지
# =========================================================

def month_branch(m, d):
    """
    절기 기준의 월지.
    실제 천문 절기 시각 대신 날짜 범위를 사용한 단순 계산.
    """

    md = m * 100 + d

    if md >= 1207 or md < 105:
        return 0       # 자월에 해당하는 겨울 영역
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
    """
    월간지 계산.

    인월의 천간은
    갑기년 → 병인
    을경년 → 무인
    병신년 → 경인
    정임년 → 임인
    무계년 → 갑인
    """

    year_stem, _ = year_pillar(y, m, d)

    branch = month_branch(m, d)

    # 인월을 0으로 두고 계산
    month_order = (branch - 2) % 12

    starting_stem = {
        0: 2,   # 갑
        1: 4,   # 을
        2: 6,   # 병
        3: 8,   # 정
        4: 0    # 무
    }

    stem_start = starting_stem[year_stem % 5]

    stem = (stem_start + month_order) % 10

    return stem, branch


# =========================================================
# 시주
# =========================================================

def hour_branch(hour):
    """
    2시간 단위로 지지를 계산.
    23:00~00:59 = 자시
    01:00~02:59 = 축시 ...
    """

    if hour >= 23 or hour < 1:
        return 0

    return ((hour + 1) // 2) % 12


def hour_pillar(day_stem, hour):
    """
    일간에 따른 시간의 천간 계산.
    """

    branch = hour_branch(hour)

    # 갑기일 → 갑자
    # 을경일 → 병자
    # 병신일 → 무자
    # 정임일 → 경자
    # 무계일 → 임자

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
# 표시용 함수
# =========================================================

def pillar_html(name, stem_index, branch_index):

    stem_hanja, stem_korean, stem_element = HEAVENLY[stem_index]
    branch_hanja, branch_korean, branch_element, animal = EARTHLY[branch_index]

    return (
        '<div class="pillar">'

        '<div class="pillar-name">'
        + name +
        '</div>'

        '<div class="heaven">'
        + stem_hanja +
        '</div>'

        '<div class="korean">'
        + stem_korean +
        ' · ' + stem_element +
        '</div>'

        '<div class="earth">'
        + branch_hanja +
        '</div>'

        '<div class="korean">'
        + branch_korean +
        ' · ' + branch_element +
        '</div>'

        '<div class="korean">'
        + animal +
        '띠'
        '</div>'

        '</div>'
    )


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
    '생년월일과 태어난 시간으로 알아보는 나의 四柱八字'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 입력
# =========================================================

st.markdown(
    '<div class="input-card">'
    '<div class="input-title">'
    '🌷 나의 출생 정보를 입력해주세요'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

birth_date = st.date_input(
    "생년월일",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="YYYY-MM-DD"
)

birth_time = st.time_input(
    "태어난 시간",
    value=time(12, 0)
)


# =========================================================
# 사주 계산
# =========================================================

y = birth_date.year
m = birth_date.month
d = birth_date.day
h = birth_time.hour


year_stem, year_branch = year_pillar(y, m, d)

month_stem, month_branch_index = month_pillar(y, m, d)

day_stem, day_branch = day_pillar(y, m, d)

hour_stem, hour_branch_index = hour_pillar(day_stem, h)


# =========================================================
# 결과
# =========================================================

pillars = (
    pillar_html("년주 年柱", year_stem, year_branch)
    + pillar_html("월주 月柱", month_stem, month_branch_index)
    + pillar_html("일주 日柱", day_stem, day_branch)
    + pillar_html("시주 時柱", hour_stem, hour_branch_index)
)

st.markdown(
    '<div class="saju-card">'

    '<div class="card-title">'
    '✦ 나의 사주 ✦'
    '</div>'

    '<div class="card-subtitle">'
    + str(y) + '년 ' + str(m) + '월 ' + str(d)
    + '일 · '
    + str(h) + '시'
    + '</div>'

    '<div class="pillars">'
    + pillars +
    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 오행 구성
# =========================================================

all_elements = []

for s, b in [
    (year_stem, year_branch),
    (month_stem, month_branch_index),
    (day_stem, day_branch),
    (hour_stem, hour_branch_index)
]:
    all_elements.append(HEAVENLY[s][2])
    all_elements.append(EARTHLY[b][2])


element_count = {}

for element in ["목", "화", "토", "금", "수"]:
    element_count[element] = all_elements.count(element)

element_html = ""

element_emoji = {
    "목": "🌱",
    "화": "🔥",
    "토": "🌷",
    "금": "✨",
    "수": "💧"
}

for element in ["목", "화", "토", "금", "수"]:

    element_html += (
        '<div class="element">'
        + element_emoji[element]
        + ' '
        + element
        + ' '
        + str(element_count[element])
        + '</div>'
    )


st.markdown(
    '<div class="saju-card">'

    '<div class="section-title">'
    '🌿 오행 구성'
    '</div>'

    '<div class="element-area">'
    + element_html +
    '</div>'

    '<div class="divider"></div>'

    '<div class="section-title">'
    '☯️ 사주 읽는 법'
    '</div>'

    '<div style="text-align:center; color:#817485; '
    'font-size:13px; line-height:1.8;">'

    '년주 · 나의 뿌리와 가문<br>'
    '월주 · 성장 환경과 사회적 기반<br>'
    '일주 · 나 자신을 나타내는 중심<br>'
    '시주 · 후반 인생과 미래의 흐름'

    '</div>'

    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 안내
# =========================================================

st.markdown(
    '<div class="notice">'
    '※ 양력 날짜를 기준으로 계산합니다.<br>'
    '※ 절기 전환 시각은 단순화된 날짜 기준을 사용하므로 '
    '전문 만세력과 결과가 다를 수 있습니다.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    '🌙 四柱八字 · 나만의 작은 우주를 들여다보기 ♡'
    '</div>',
    unsafe_allow_html=True
)
