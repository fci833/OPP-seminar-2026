import html
import random

import streamlit as st


# ============================================================
# OPSÆTNING
# ============================================================

st.set_page_config(
    page_title="OPP Seminar 2026",
    page_icon="🔵",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# ARRANGEMENTSOPLYSNINGER
# Ret tider, adresser og tekster her.
# ============================================================

EVENT = {
    "title": "OPP Seminar 2026",
    "tagline": (
        "En dag med ny viden, fælles oplevelser "
        "og gode samtaler."
    ),
    "goboat_address": (
        "Islands Brygge 10, 2300 København S"
    ),
    "goboat_url": (
        "https://www.google.com/maps/search/"
        "?api=1&query=Islands+Brygge+10+2300+København+S"
    ),
    "dinner_location": "Vestauranten",
    "dinner_address": (
        "Tietgensgade 65, 1704 København V"
    ),
    "dinner_url": (
        "https://www.google.com/maps/search/"
        "?api=1&query=Tietgensgade+65+1704+København+V"
    ),
}


# ============================================================
# DELTAGERE
#
# Erstat denne liste, når du kender den endelige deltagerliste.
# Grupperne dannes automatisk og stabilt.
# ============================================================

PARTICIPANTS_TEXT = """
ABVH AETI AGSF AHQS AHVI ANEC ANLH BEHO BMET BNYS
BTEN BTNL CDJA CITK CNQU COVE CRYE CWO DSMV EAKL
EAOJ EEHF EENM EJJN EMFT FCI FDKO FHAZ FMU GJHN
GJN GKLU HEPI HHAQ HNCR HSEZ HUEI HVLC IAOD IEPE
IMLE INGC ISFI JDMV JKBR JNVJ JOFQ JVGK KBNP KDUH
KHDY KJUS KKTD KPKV KTEQ KUQA LCXS LHOB LIAB LLHR
LNBF LSHS LVPM LWLA MCEN MDU MEBG MEDL MJKL MJRI
MMTX MNXH MOVI MZBC NHPS NJSQ NOCB NOEZ NRBL NRDI
NVPO OLYE OSCF PCW PNKF PTSM QMBG QRAA RCUM RJQN
RMTE RQBK RQOC RSVJ SDCZ SEEZ SFWT SHUC SIGL SNGJ
SPQF SQRF SWQE SXJM SZYI TGJJ TKGR TRMG UATS UHKH
UNBG VCTE VMKT WADS YSIK ZJHH ZLBK ZSLU ZSQN
"""

participants = sorted(
    {
        value.strip().upper()
        for value in PARTICIPANTS_TEXT.split()
        if value.strip()
    }
)


# ============================================================
# AUTOMATISK GRUPPEFORDELING
#
# Seed-værdierne betyder, at grupperne forbliver de samme,
# når siden genindlæses.
# ============================================================

def make_balanced_groups(
    participant_list,
    number_of_groups,
    seed,
):
    shuffled = list(participant_list)

    random_generator = random.Random(seed)
    random_generator.shuffle(shuffled)

    generated_groups = [
        [] for _ in range(number_of_groups)
    ]

    for index, participant in enumerate(shuffled):
        group_index = index % number_of_groups
        generated_groups[group_index].append(participant)

    for group in generated_groups:
        group.sort()

    return generated_groups


groups = {
    "evolve": make_balanced_groups(
        participants,
        6,
        "OPP-EVOLVE-2026",
    ),
    "ai": make_balanced_groups(
        participants,
        4,
        "OPP-AI-2026",
    ),
    "goboat": make_balanced_groups(
        participants,
        8,
        "OPP-GOBOAT-2026",
    ),
    "dinner": make_balanced_groups(
        participants,
        12,
        "OPP-DINNER-2026",
    ),
}


# ============================================================
# LOKALER OG ROTATIONER
# ============================================================

EVOLVE_ROOMS = [
    "Vesterbro Torv",
    "Enghave Plads",
    "Foye",
    "Kødbyen",
    "Tagterrassen",
    "Tivoli",
]

AI_ROTATIONS = [
    [
        "Escape Room",
        "Private Room",
        "Prompt Heaven",
        "Dating Lounge",
    ],
    [
        "Private Room",
        "Prompt Heaven",
        "Dating Lounge",
        "Escape Room",
    ],
    [
        "Prompt Heaven",
        "Dating Lounge",
        "Escape Room",
        "Private Room",
    ],
    [
        "Dating Lounge",
        "Escape Room",
        "Private Room",
        "Prompt Heaven",
    ],
]

AGENDA = [
    {
        "number": 1,
        "time": "08:00–09:00",
        "title": "Morgenmad",
        "description": "Morgenmad er valgfri.",
    },
    {
        "number": 2,
        "time": "09:00–09:30",
        "title": "Velkomst",
        "description": (
            "Velkommen og introduktion til dagens program."
        ),
    },
    {
        "number": 3,
        "time": "09:30–12:00",
        "title": "eVolve Workshop",
        "description": (
            "Workshop og samarbejde i egne teams."
        ),
        "page": "eVolve",
    },
    {
        "number": 4,
        "time": "12:00–13:00",
        "title": "Frokost",
        "description": (
            "Frokost og mulighed for networking."
        ),
    },
    {
        "number": 5,
        "time": "13:00–15:00",
        "title": "AI Speed Dating – oplev AI",
        "description": (
            "Fire rotationer med forskellige AI-oplevelser."
        ),
        "page": "AI Speed Dating",
    },
    {
        "number": 6,
        "time": "15:00–15:15",
        "title": "Pause",
        "description": "Kort pause.",
    },
    {
        "number": 7,
        "time": "15:15–15:45",
        "title": "Gåtur til GoBoat",
        "description": "Vi går samlet til GoBoat.",
    },
    {
        "number": 8,
        "time": "15:45–17:30",
        "title": "GoBoat",
        "description": (
            "Se din gruppe og praktisk information."
        ),
        "page": "GoBoat",
    },
    {
        "number": 9,
        "time": "17:30–18:00",
        "title": "Transport til middag",
        "description": (
            "Vi går samlet videre til middagen."
        ),
    },
    {
        "number": 10,
        "time": "18:00–",
        "title": "Middag, networking og fest",
        "description": (
            "Se dit bord og information om lokationen."
        ),
        "page": "Middag",
    },
]


# ============================================================
# DESIGN
# Novo Nordisk-inspirerede farver.
# ============================================================

st.html(
    """
    <style>
        :root {
            --opp-navy: #001965;
            --opp-dark-navy: #00113f;
            --opp-blue: #005ad2;
            --opp-medium-blue: #0075c9;
            --opp-cyan: #00b8de;
            --opp-light-blue: #dff4fb;
            --opp-pale-blue: #eef8fc;
            --opp-text: #071a33;
            --opp-muted: #536a80;
            --opp-border: #b9dff2;
            --opp-white: #ffffff;
            --opp-shadow:
                0 18px 45px rgba(0, 49, 92, 0.12),
                0 4px 12px rgba(0, 49, 92, 0.06);
        }

        html {
            scroll-behavior: smooth;
        }

        body,
        [class*="css"] {
            font-family:
                Aptos,
                "Segoe UI",
                Arial,
                Helvetica,
                sans-serif;
        }

        .stApp {
            color: var(--opp-text);
            background:
                radial-gradient(
                    circle at 8% 20%,
                    rgba(0, 184, 222, 0.09),
                    transparent 25rem
                ),
                radial-gradient(
                    circle at 92% 75%,
                    rgba(0, 90, 210, 0.08),
                    transparent 30rem
                ),
                linear-gradient(
                    180deg,
                    #f8fcfe 0%,
                    #eef8fc 55%,
                    #e5f4fa 100%
                );
        }

        .stMainBlockContainer,
        .block-container {
            width: min(1120px, calc(100% - 24px));
            max-width: 1120px;
            padding-top: 1.2rem;
            padding-bottom: 4rem;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header[data-testid="stHeader"] {
            background: rgba(255, 255, 255, 0.92);
        }

        /* Navigation */

        div[role="radiogroup"] {
            display: flex;
            width: 100%;
            align-items: center;
            justify-content: center;
            gap: 0.25rem;
            margin-bottom: 1.6rem;
            padding: 0.45rem;
            overflow-x: auto;
            background: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(0, 25, 101, 0.08);
            border-radius: 17px;
            box-shadow:
                0 8px 24px rgba(0, 49, 92, 0.07);
        }

        div[role="radiogroup"] label {
            padding: 0.55rem 0.7rem;
            color: var(--opp-dark-navy);
            border-radius: 10px;
            white-space: nowrap;
            font-size: 0.86rem;
            font-weight: 800;
        }

        div[role="radiogroup"] label:hover {
            background: var(--opp-light-blue);
        }

        /* Hero */

        .opp-hero {
            position: relative;
            overflow: hidden;
            margin: 0 0 2rem;
            padding: 2.8rem 3rem;
            color: white;
            background:
                linear-gradient(
                    135deg,
                    #00113f 0%,
                    #001965 58%,
                    #003c89 100%
                );
            border-radius: 28px;
            box-shadow: var(--opp-shadow);
        }

        .opp-hero::before {
            position: absolute;
            width: 165px;
            height: 165px;
            top: -110px;
            right: -50px;
            content: "";
            border: 30px solid rgba(79, 220, 244, 0.15);
            border-radius: 50%;
        }

        .opp-hero::after {
            position: absolute;
            width: 190px;
            height: 190px;
            right: 55px;
            bottom: -170px;
            content: "";
            background: rgba(0, 184, 222, 0.08);
            border-radius: 50%;
        }

        .opp-hero-light {
            color: var(--opp-text);
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(0, 90, 210, 0.09);
        }

        .opp-eyebrow {
            position: relative;
            z-index: 1;
            margin: 0 0 0.7rem;
            color: #4fdcf4;
            font-size: 0.76rem;
            font-weight: 900;
            letter-spacing: 0.18em;
            text-transform: uppercase;
        }

        .opp-eyebrow-blue {
            color: var(--opp-blue);
        }

        .opp-hero-light .opp-eyebrow {
            color: var(--opp-blue);
        }

        .opp-hero h1 {
            position: relative;
            z-index: 1;
            margin: 0 0 0.8rem;
            color: inherit;
            font-size: clamp(2.3rem, 6vw, 4rem);
            line-height: 1.04;
            letter-spacing: -0.045em;
        }

        .opp-highlight {
            color: #4fdcf4;
        }

        .opp-lead {
            position: relative;
            z-index: 1;
            max-width: 760px;
            margin: 0;
            color: rgba(255, 255, 255, 0.86);
            font-size: 1.08rem;
            line-height: 1.65;
        }

        .opp-hero-light .opp-lead {
            color: var(--opp-muted);
        }

        /* Overskrifter */

        .opp-section-heading {
            margin: 2.2rem 0 1rem;
            color: var(--opp-dark-navy);
            font-size: clamp(1.55rem, 4vw, 2rem);
            font-weight: 850;
            letter-spacing: -0.025em;
        }

        .opp-intro {
            max-width: 780px;
            margin: -0.45rem 0 1.4rem;
            color: var(--opp-muted);
            line-height: 1.65;
        }

        /* Agenda */

        .agenda-list {
            overflow: hidden;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.09);
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .agenda-row {
            display: grid;
            min-height: 92px;
            grid-template-columns: 45px 135px 1fr 30px;
            align-items: center;
            gap: 1rem;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid var(--opp-border);
        }

        .agenda-row:last-child {
            border-bottom: 0;
        }

        .agenda-row:hover {
            background: #f7fbfd;
        }

        .agenda-number {
            display: grid;
            width: 38px;
            height: 38px;
            place-items: center;
            color: var(--opp-navy);
            background: #bfe6fa;
            border-radius: 50%;
            font-size: 0.85rem;
            font-weight: 900;
        }

        .agenda-number.active {
            color: white;
            background: var(--opp-navy);
        }

        .agenda-time {
            color: var(--opp-navy);
            font-size: 0.92rem;
            font-weight: 900;
        }

        .agenda-title {
            margin-bottom: 0.25rem;
            color: var(--opp-text);
            font-size: 1.05rem;
            font-weight: 900;
        }

        .agenda-description {
            color: var(--opp-muted);
            font-size: 0.9rem;
            line-height: 1.45;
        }

        .agenda-arrow {
            color: var(--opp-blue);
            font-size: 1.6rem;
            font-weight: 900;
        }

        /* Generelle kort */

        .info-card {
            margin: 1rem 0;
            padding: 1.6rem;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.09);
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .info-card h3 {
            margin: 0 0 0.5rem;
            color: var(--opp-dark-navy);
            font-size: 1.35rem;
        }

        .info-card p {
            margin: 0;
            color: var(--opp-muted);
            line-height: 1.65;
        }

        .location-card {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            margin: 1rem 0 2rem;
            padding: 1.6rem;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.09);
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .location-card h3 {
            margin: 0.25rem 0 0.4rem;
            color: var(--opp-dark-navy);
            font-size: 1.25rem;
        }

        .location-card p {
            margin: 0;
            color: var(--opp-muted);
        }

        .map-button {
            display: inline-flex;
            min-height: 48px;
            align-items: center;
            justify-content: center;
            padding: 0.75rem 1.25rem;
            color: white !important;
            background: var(--opp-navy);
            border-radius: 12px;
            box-shadow:
                0 8px 18px rgba(0, 25, 101, 0.20);
            text-decoration: none !important;
            white-space: nowrap;
            font-weight: 850;
        }

        .map-button:hover {
            background: var(--opp-blue);
        }

        /* Gruppekort */

        .group-card {
            overflow: hidden;
            min-height: 280px;
            margin-bottom: 1.3rem;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.09);
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .group-header {
            position: relative;
            overflow: hidden;
            display: flex;
            min-height: 74px;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 1.1rem 1.3rem;
            color: white;
            background:
                linear-gradient(
                    135deg,
                    #00113f,
                    #001965
                );
        }

        .group-header::after {
            position: absolute;
            width: 110px;
            height: 110px;
            top: -67px;
            right: -30px;
            content: "";
            background: rgba(0, 184, 222, 0.13);
            border-radius: 50%;
        }

        .group-title {
            position: relative;
            z-index: 1;
            font-size: 1.05rem;
            font-weight: 900;
        }

        .group-room {
            position: relative;
            z-index: 1;
            color: #bdefff;
            font-size: 0.78rem;
            font-weight: 800;
            text-align: right;
        }

        .member-list {
            margin: 0;
            padding: 0 1.3rem 1rem;
            list-style: none;
        }

        .member {
            padding: 0.76rem 0 0.65rem;
            color: var(--opp-text);
            border-bottom: 1px solid var(--opp-border);
            font-size: 0.9rem;
            font-weight: 800;
        }

        .member:last-child {
            border-bottom: 0;
        }

        /* Find mig */

        .person-card {
            overflow: hidden;
            margin-top: 1.4rem;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.09);
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .person-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 1.35rem 1.5rem;
            color: white;
            background:
                linear-gradient(
                    135deg,
                    var(--opp-navy),
                    var(--opp-blue)
                );
        }

        .person-initials {
            font-size: 1.5rem;
            font-weight: 900;
        }

        .person-subtitle {
            color: #c7efff;
            font-weight: 700;
        }

        .person-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
        }

        .person-item {
            min-height: 120px;
            padding: 1.3rem;
            border-right: 1px solid var(--opp-border);
        }

        .person-item:last-child {
            border-right: 0;
        }

        .person-label {
            margin-bottom: 0.55rem;
            color: var(--opp-muted);
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.07em;
            text-transform: uppercase;
        }

        .person-value {
            color: var(--opp-dark-navy);
            font-size: 1.02rem;
            font-weight: 900;
            line-height: 1.5;
        }

        /* Tabel */

        .table-wrapper {
            overflow-x: auto;
            margin-bottom: 2rem;
            background: white;
            border: 1px solid rgba(0, 90, 210, 0.10);
            border-radius: 18px;
            box-shadow: var(--opp-shadow);
        }

        .opp-table {
            width: 100%;
            min-width: 760px;
            border-collapse: collapse;
        }

        .opp-table th {
            padding: 1rem;
            color: white;
            background: var(--opp-navy);
            text-align: left;
            font-size: 0.84rem;
            vertical-align: top;
        }

        .opp-table th small {
            display: block;
            margin-top: 0.2rem;
            color: #bdefff;
            font-size: 0.7rem;
        }

        .opp-table td {
            padding: 1rem;
            color: var(--opp-text);
            border-bottom: 1px solid var(--opp-border);
            font-size: 0.9rem;
            font-weight: 750;
        }

        .opp-table tbody tr:nth-child(even) {
            background: #f7fbfd;
        }

        .opp-table tbody tr:last-child td {
            border-bottom: 0;
        }

        /* Rumoversigt */

        .room-map {
            display: grid;
            min-height: 480px;
            grid-template-columns: repeat(4, 1fr);
            grid-template-rows: repeat(4, 1fr);
            gap: 8px;
            margin: 1rem 0 2rem;
            padding: 1rem;
            background: #e5ecef;
            border: 1px solid #cbdde7;
            border-radius: 20px;
            box-shadow: var(--opp-shadow);
        }

        .room {
            display: flex;
            min-height: 100px;
            align-items: center;
            justify-content: center;
            padding: 1rem;
            color: white;
            border: 3px solid white;
            border-radius: 15px;
            text-align: center;
            font-weight: 900;
            line-height: 1.4;
        }

        .room-terrace {
            color: var(--opp-dark-navy);
            background:
                repeating-linear-gradient(
                    45deg,
                    #d8f3df,
                    #d8f3df 20px,
                    #c9ecd4 20px,
                    #c9ecd4 40px
                );
        }

        .room-orange {
            color: #351400;
            background: #ff9d35;
        }

        .room-teal {
            background: #008b99;
        }

        .room-cyan {
            color: var(--opp-dark-navy);
            background: #69ddec;
        }

        .room-blue {
            background: var(--opp-blue);
        }

        .room-purple {
            background: #7050a0;
        }

        .room-navy {
            background: var(--opp-navy);
        }

        .room-grey {
            color: var(--opp-dark-navy);
            background: #eef2f5;
        }

        /* Streamlit-elementer */

        div[data-testid="stTextInput"] input {
            min-height: 58px;
            color: var(--opp-text);
            background: white;
            border: 2px solid #a8dcf5;
            border-radius: 14px;
            font-weight: 800;
            text-transform: uppercase;
        }

        div[data-testid="stTextInput"] input:focus {
            border-color: var(--opp-blue);
            box-shadow:
                0 0 0 2px rgba(0, 90, 210, 0.12);
        }

        div[data-testid="stButton"] button {
            min-height: 48px;
            color: white;
            background: var(--opp-navy);
            border: 0;
            border-radius: 12px;
            font-weight: 850;
        }

        div[data-testid="stButton"] button:hover {
            color: white;
            background: var(--opp-blue);
            border: 0;
        }

        /* Footer */

        .opp-footer {
            margin-top: 4rem;
            padding: 2rem 1rem 0.5rem;
            color: var(--opp-dark-navy);
            border-top:
                1px solid rgba(0, 25, 101, 0.09);
            text-align: center;
            font-size: 0.86rem;
            font-weight: 800;
        }

        .footer-dot {
            color: var(--opp-cyan);
        }

        @media (max-width: 800px) {
            .stMainBlockContainer,
            .block-container {
                width: calc(100% - 14px);
                padding-right: 0.4rem;
                padding-left: 0.4rem;
            }

            .opp-hero {
                padding: 2rem 1.5rem;
                border-radius: 22px;
            }

            .agenda-row {
                grid-template-columns: 38px 1fr 24px;
                gap: 0.7rem;
                padding: 1rem;
            }

            .agenda-number {
                grid-row: 1 / span 2;
            }

            .agenda-time,
            .agenda-content {
                grid-column: 2;
            }

            .agenda-arrow {
                grid-column: 3;
                grid-row: 1 / span 2;
            }

            .person-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .person-item:nth-child(2) {
                border-right: 0;
            }

            .person-item:nth-child(-n + 2) {
                border-bottom:
                    1px solid var(--opp-border);
            }

            .location-card {
                align-items: flex-start;
                flex-direction: column;
            }

            .room-map {
                min-height: auto;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: auto;
            }

            .room {
                grid-column: auto !important;
                grid-row: auto !important;
                min-height: 130px;
            }
        }

        @media (max-width: 520px) {
            div[role="radiogroup"] {
                justify-content: flex-start;
            }

            div[role="radiogroup"] label {
                font-size: 0.72rem;
            }

            .person-grid {
                grid-template-columns: 1fr;
            }

            .person-item,
            .person-item:nth-child(2) {
                border-right: 0;
                border-bottom:
                    1px solid var(--opp-border);
            }

            .person-item:last-child {
                border-bottom: 0;
            }

            .room-map {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """
)


# ============================================================
# HJÆLPEFUNKTIONER
# ============================================================

def safe(value):
    """Beskytter tekst, der indsættes i HTML."""
    return html.escape(str(value))


def hero(
    eyebrow,
    title,
    description,
    light=False,
):
    light_class = " opp-hero-light" if light else ""

    st.html(
        f"""
        <section class="opp-hero{light_class}">
            <div class="opp-eyebrow">
                {safe(eyebrow)}
            </div>

            <h1>{title}</h1>

            <p class="opp-lead">
                {safe(description)}
            </p>
        </section>
        """
    )


def section_heading(title, intro=None):
    st.html(
        f"""
        <div class="opp-section-heading">
            {safe(title)}
        </div>
        """
    )

    if intro:
        st.html(
            f"""
            <div class="opp-intro">
                {safe(intro)}
            </div>
            """
        )


def find_group_number(collection, initials):
    for group_number, members in enumerate(
        collection,
        start=1,
    ):
        if initials in members:
            return group_number

    return None


def group_card(title, members, room=None):
    room_html = ""

    if room:
        room_html = (
            '<div class="group-room">'
            f"{safe(room)}"
            "</div>"
        )

    member_html = "".join(
        f'<li class="member">{safe(member)}</li>'
        for member in members
    )

    st.html(
        f"""
        <article class="group-card">
            <header class="group-header">
                <div class="group-title">
                    ◉ &nbsp; {safe(title)}
                </div>

                {room_html}
            </header>

            <ul class="member-list">
                {member_html}
            </ul>
        </article>
        """
    )


def render_group_grid(
    collection,
    title_prefix,
    rooms=None,
):
    rooms = rooms or []

    for start_index in range(
        0,
        len(collection),
        2,
    ):
        columns = st.columns(2, gap="medium")

        for offset in range(2):
            group_index = start_index + offset

            if group_index >= len(collection):
                continue

            room = None

            if group_index < len(rooms):
                room = rooms[group_index]

            with columns[offset]:
                group_card(
                    title=(
                        f"{title_prefix} "
                        f"{group_index + 1}"
                    ),
                    members=collection[group_index],
                    room=room,
                )


def location_card(
    label,
    title,
    description,
    url,
):
    st.html(
        f"""
        <section class="location-card">
            <div>
                <div class="opp-eyebrow opp-eyebrow-blue">
                    {safe(label)}
                </div>

                <h3>{safe(title)}</h3>
                <p>{safe(description)}</p>
            </div>

            <a
                class="map-button"
                href="{safe(url)}"
                target="_blank"
                rel="noopener noreferrer"
            >
                Åbn adresse i kort →
            </a>
        </section>
        """
    )


def create_table(headers, rows):
    header_html = "".join(
        f"<th>{header}</th>"
        for header in headers
    )

    body_html = ""

    for row in rows:
        cells = "".join(
            f"<td>{safe(cell)}</td>"
            for cell in row
        )

        body_html += f"<tr>{cells}</tr>"

    st.html(
        f"""
        <div class="table-wrapper">
            <table class="opp-table">
                <thead>
                    <tr>{header_html}</tr>
                </thead>

                <tbody>
                    {body_html}
                </tbody>
            </table>
        </div>
        """
    )


def change_page(page_name):
    st.session_state["navigation"] = page_name


# ============================================================
# NAVIGATION
# ============================================================

PAGES = [
    "Agenda",
    "Find mig",
    "eVolve",
    "AI Speed Dating",
    "GoBoat",
    "Middag",
]

if "navigation" not in st.session_state:
    st.session_state["navigation"] = "Agenda"

selected_page = st.radio(
    "Navigation",
    PAGES,
    key="navigation",
    horizontal=True,
    label_visibility="collapsed",
)


# ============================================================
# AGENDA
# ============================================================

def render_agenda():
    hero(
        eyebrow="Sammen om fremtiden",
        title=(
            'OPP Seminar '
            '<span class="opp-highlight">2026</span>'
        ),
        description=EVENT["tagline"],
        light=False,
    )

    st.html(
        """
        <div class="opp-eyebrow opp-eyebrow-blue">
            Dagens program
        </div>
        """
    )

    section_heading("Agenda")

    rows = []

    for item in AGENDA:
        active_class = (
            " active" if item.get("page") else ""
        )

        arrow = "→" if item.get("page") else ""

        rows.append(
            f"""
            <div class="agenda-row">
                <div class="agenda-number{active_class}">
                    {item["number"]}
                </div>

                <div class="agenda-time">
                    {safe(item["time"])}
                </div>

                <div class="agenda-content">
                    <div class="agenda-title">
                        {safe(item["title"])}
                    </div>

                    <div class="agenda-description">
                        {safe(item["description"])}
                    </div>
                </div>

                <div class="agenda-arrow">
                    {arrow}
                </div>
            </div>
            """
        )

    st.html(
        '<div class="agenda-list">'
        + "".join(rows)
        + "</div>"
    )

    section_heading("Gå direkte til")

    first_row = st.columns(3, gap="small")

    with first_row[0]:
        st.button(
            "Find mig",
            use_container_width=True,
            on_click=change_page,
            args=("Find mig",),
        )

    with first_row[1]:
        st.button(
            "eVolve Workshop",
            use_container_width=True,
            on_click=change_page,
            args=("eVolve",),
        )

    with first_row[2]:
        st.button(
            "AI Speed Dating",
            use_container_width=True,
            on_click=change_page,
            args=("AI Speed Dating",),
        )

    second_row = st.columns(2, gap="small")

    with second_row[0]:
        st.button(
            "GoBoat",
            use_container_width=True,
            on_click=change_page,
            args=("GoBoat",),
        )

    with second_row[1]:
        st.button(
            "Middag",
            use_container_width=True,
            on_click=change_page,
            args=("Middag",),
        )

    st.html(
        """
        <section class="info-card"
                 style="margin-top:2rem;">
            <div class="opp-eyebrow opp-eyebrow-blue">
                Din personlige oversigt
            </div>

            <h3>Find mig</h3>

            <p>
                Søg på dine initialer og se dit
                eVolve-team, din AI-gruppe,
                dit GoBoat-hold og dit middagsbord.
            </p>
        </section>
        """
    )

    st.button(
        "Søg efter mine initialer →",
        on_click=change_page,
        args=("Find mig",),
    )


# ============================================================
# FIND MIG
# ============================================================

def render_find_me():
    hero(
        eyebrow="Din personlige oversigt",
        title="Find mig",
        description=(
            "Søg på dine initialer og få din personlige "
            "oversigt over dagen."
        ),
        light=True,
    )

    initials = st.text_input(
        "Skriv dine initialer",
        placeholder="For eksempel FCI eller KUQA",
        max_chars=10,
    )

    initials = initials.strip().upper()

    st.caption(
        "Indtast initialerne præcist som de står "
        "på deltagerlisten."
    )

    if not initials:
        st.info(
            "Indtast dine initialer ovenfor for at "
            "se din personlige oversigt."
        )
        return

    if initials not in participants:
        st.warning(
            f"Vi kunne ikke finde '{initials}'. "
            "Kontrollér initialerne og prøv igen."
        )

        suggestions = [
            participant
            for participant in participants
            if (
                initials in participant
                or participant.startswith(initials[:1])
            )
        ][:10]

        if suggestions:
            st.write(
                "Mulige initialer: "
                + ", ".join(suggestions)
            )

        return

    evolve_group = find_group_number(
        groups["evolve"],
        initials,
    )

    ai_group = find_group_number(
        groups["ai"],
        initials,
    )

    goboat_group = find_group_number(
        groups["goboat"],
        initials,
    )

    dinner_table = find_group_number(
        groups["dinner"],
        initials,
    )

    evolve_room = EVOLVE_ROOMS[
        evolve_group - 1
    ]

    st.html(
        f"""
        <article class="person-card">
            <header class="person-header">
                <div class="person-initials">
                    {safe(initials)}
                </div>

                <div class="person-subtitle">
                    Personlig oversigt
                </div>
            </header>

            <div class="person-grid">
                <div class="person-item">
                    <div class="person-label">
                        eVolve Workshop
                    </div>

                    <div class="person-value">
                        Team {evolve_group}<br>
                        {safe(evolve_room)}
                    </div>
                </div>

                <div class="person-item">
                    <div class="person-label">
                        AI Speed Dating
                    </div>

                    <div class="person-value">
                        AI-gruppe {ai_group}
                    </div>
                </div>

                <div class="person-item">
                    <div class="person-label">
                        GoBoat
                    </div>

                    <div class="person-value">
                        GoBoat-gruppe {goboat_group}
                    </div>
                </div>

                <div class="person-item">
                    <div class="person-label">
                        Middag
                    </div>

                    <div class="person-value">
                        Bord {dinner_table}
                    </div>
                </div>
            </div>
        </article>
        """
    )


# ============================================================
# EVOLVE WORKSHOP
# ============================================================

def render_evolve():
    hero(
        eyebrow="09:30–12:00",
        title="eVolve Workshop",
        description=(
            "Find dit team og det lokale, hvor "
            "workshoppen afholdes."
        ),
        light=True,
    )

    section_heading("Teams og rum")

    table_rows = []

    for index, group in enumerate(
        groups["evolve"]
    ):
        table_rows.append(
            [
                f"Team {index + 1}",
                EVOLVE_ROOMS[index],
                len(group),
            ]
        )

    create_table(
        headers=[
            "Team",
            "Lokale",
            "Antal deltagere",
        ],
        rows=table_rows,
    )

    section_heading(
        "Rumoversigt",
        (
            "Dette er en skematisk oversigt. "
            "Den kan senere erstattes med "
            "den endelige plantegning."
        ),
    )

    st.html(
        """
        <div class="room-map">
            <div
                class="room room-terrace"
                style="
                    grid-column:1 / 3;
                    grid-row:1 / 5;
                "
            >
                Tagterrassen<br>
                Team 5
            </div>

            <div
                class="room room-orange"
                style="
                    grid-column:3;
                    grid-row:1;
                "
            >
                Tivoli<br>
                Team 6
            </div>

            <div
                class="room room-teal"
                style="
                    grid-column:3;
                    grid-row:2;
                "
            >
                Vesterbro Torv<br>
                Team 1
            </div>

            <div
                class="room room-cyan"
                style="
                    grid-column:3;
                    grid-row:3;
                "
            >
                Enghave Plads<br>
                Team 2
            </div>

            <div
                class="room room-blue"
                style="
                    grid-column:3;
                    grid-row:4;
                "
            >
                Kødbyen<br>
                Team 4
            </div>

            <div
                class="room room-grey"
                style="
                    grid-column:4;
                    grid-row:1 / 4;
                "
            >
                Foye<br>
                Team 3
            </div>

            <div
                class="room room-navy"
                style="
                    grid-column:4;
                    grid-row:4;
                "
            >
                Trappe og elevator
            </div>
        </div>
        """
    )

    section_heading("Teamoversigt")

    render_group_grid(
        collection=groups["evolve"],
        title_prefix="Team",
        rooms=EVOLVE_ROOMS,
    )


# ============================================================
# AI SPEED DATING
# ============================================================

def render_ai():
    hero(
        eyebrow="13:00–15:00",
        title="AI Speed Dating – oplev AI",
        description=(
            "Følg din AI-gruppe gennem fire runder. "
            "Der er rotation mellem hver runde."
        ),
        light=True,
    )

    section_heading(
        "Rotationsskema",
        (
            "Hver gruppe besøger alle fire "
            "AI-oplevelser."
        ),
    )

    rotation_rows = []

    for index, rotation in enumerate(
        AI_ROTATIONS
    ):
        rotation_rows.append(
            [
                f"AI-gruppe {index + 1}",
                rotation[0],
                rotation[1],
                rotation[2],
                rotation[3],
            ]
        )

    create_table(
        headers=[
            "Gruppe",
            "Runde 1<br><small>13:25–13:40</small>",
            "Runde 2<br><small>13:45–14:00</small>",
            "Runde 3<br><small>14:05–14:20</small>",
            "Runde 4<br><small>14:25–14:40</small>",
        ],
        rows=rotation_rows,
    )

    section_heading("Rumoversigt")

    st.html(
        """
        <div class="room-map">
            <div
                class="room room-terrace"
                style="
                    grid-column:1 / 3;
                    grid-row:1 / 5;
                "
            >
                Tagterrasse
            </div>

            <div
                class="room room-orange"
                style="
                    grid-column:3;
                    grid-row:1;
                "
            >
                Dating Lounge
            </div>

            <div
                class="room room-teal"
                style="
                    grid-column:3;
                    grid-row:2;
                "
            >
                Prompt Heaven
            </div>

            <div
                class="room room-purple"
                style="
                    grid-column:3;
                    grid-row:3;
                "
            >
                Private Room
            </div>

            <div
                class="room room-blue"
                style="
                    grid-column:3;
                    grid-row:4;
                "
            >
                Escape Room
            </div>

            <div
                class="room room-grey"
                style="
                    grid-column:4;
                    grid-row:1 / 5;
                "
            >
                Fællesområde<br>
                Elevator og toiletter
            </div>
        </div>
        """
    )

    section_heading("AI-grupper")

    render_group_grid(
        collection=groups["ai"],
        title_prefix="AI-gruppe",
    )


# ============================================================
# GOBOAT
# ============================================================

def render_goboat():
    hero(
        eyebrow="15:45–17:30",
        title="GoBoat",
        description=(
            "Find din gruppe og se adressen "
            "for aktiviteten."
        ),
        light=True,
    )

    location_card(
        label="Mødested",
        title=EVENT["goboat_address"],
        description=(
            "Åbn adressen i kort på din telefon "
            "eller computer."
        ),
        url=EVENT["goboat_url"],
    )

    st.html(
        """
        <section class="info-card">
            <h3>Praktisk information</h3>

            <p>
                Mød op i god tid og følg
                arrangørernes instruktioner ved kajen.
            </p>
        </section>
        """
    )

    section_heading("GoBoat-grupper")

    render_group_grid(
        collection=groups["goboat"],
        title_prefix="GoBoat-gruppe",
    )


# ============================================================
# MIDDAG
# ============================================================

def render_dinner():
    hero(
        eyebrow="18:00–",
        title="Middag, networking og fest",
        description=(
            "Find dit middagsbord og praktisk "
            "information om lokationen."
        ),
        light=True,
    )

    location_card(
        label="Middag",
        title=EVENT["dinner_location"],
        description=EVENT["dinner_address"],
        url=EVENT["dinner_url"],
    )

    section_heading("Lokationsoversigt")

    st.html(
        f"""
        <div class="room-map">
            <div
                class="room room-navy"
                style="
                    grid-column:1 / 3;
                    grid-row:1 / 5;
                "
            >
                Konference- og festområde
            </div>

            <div
                class="room room-blue"
                style="
                    grid-column:3 / 5;
                    grid-row:1 / 4;
                "
            >
                {safe(EVENT["dinner_location"])}
            </div>

            <div
                class="room room-cyan"
                style="
                    grid-column:3;
                    grid-row:4;
                "
            >
                Hovedindgang
            </div>

            <div
                class="room room-grey"
                style="
                    grid-column:4;
                    grid-row:4;
                "
            >
                Parkering
            </div>
        </div>
        """
    )

    section_heading("Middagsborde")

    render_group_grid(
        collection=groups["dinner"],
        title_prefix="Bord",
    )


# ============================================================
# VIS DEN VALGTE SIDE
# ============================================================

if selected_page == "Agenda":
    render_agenda()

elif selected_page == "Find mig":
    render_find_me()

elif selected_page == "eVolve":
    render_evolve()

elif selected_page == "AI Speed Dating":
    render_ai()

elif selected_page == "GoBoat":
    render_goboat()

elif selected_page == "Middag":
    render_dinner()


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <footer class="opp-footer">
        <div>
            <span class="footer-dot">●</span>
            OPP Seminar
        </div>

        <div>
            Made By af FCI & KUQA
        </div>
    </footer>
    """
)
