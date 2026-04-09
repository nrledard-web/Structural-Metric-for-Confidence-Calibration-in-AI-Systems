import streamlit as st

st.set_page_config(
    page_title="Mécroyance Lab",
    page_icon="🧠",
    layout="wide"
)
st.image("banner1.png", use_container_width=True)
st.title("🧠 Mécroyance Lab")
st.caption("Spectre cognitif et dynamique de la mécroyance")
import streamlit as st
st.set_page_config(
    page_title="Mécroyance App",
    page_icon="🧠",
    layout="wide"
)

class Cognition:
    def __init__(self, gnosis: float, nous: float, doxa: float):
        self.G = self.clamp(gnosis)
        self.N = self.clamp(nous)
        self.D = self.clamp(doxa)
        self.M = self.compute_mecroyance()

    @staticmethod
    def clamp(value: float, min_val: float = 0.0, max_val: float = 10.0) -> float:
        return max(min_val, min(max_val, value))

    def compute_mecroyance(self) -> float:
        return (self.G + self.N) - self.D

    def interpret(self) -> str:
        m = self.M
        if m < 0:
            return "Zone de clôture cognitive : la certitude excède l’ancrage cognitif."
        elif 0 <= m <= 10:
            return "Zone de stabilité révisable : la mécroyance accompagne sans dominer."
        elif 10 < m <= 17:
            return "Zone de lucidité croissante : le doute structure la cognition."
        elif 17 < m < 19:
            return "Zone rare : cognition hautement intégrée et réflexive."
        elif 19 <= m < 20:
            return "Pan-sapience hypothétique : horizon limite d’une cognition presque totalement révisable."
        elif m == 20:
            return "Asymptote idéale : totalité du savoir et de l’intégration, sans rigidification."
        else:
            return "Valeur hors spectre théorique."


def get_zone_data(m: float):
    if m < 0:
        return "Clôture cognitive", "#ff4b4b"
    elif 0 <= m <= 10:
        return "Stabilité révisable", "#ff9f1c"
    elif 10 < m <= 17:
        return "Lucidité croissante", "#ffd60a"
    elif 17 < m < 19:
        return "Zone rare", "#7bd389"
    elif 19 <= m < 20:
        return "Pan-sapience hypothétique", "#4cc9f0"
    elif m == 20:
        return "Asymptote idéale", "#4361ee"
    return "Hors spectre", "#999999"


def render_spectrum(m_value: float):
    min_spectrum = -10
    max_spectrum = 20
    width_pct = ((m_value - min_spectrum) / (max_spectrum - min_spectrum)) * 100
    width_pct = max(0, min(100, width_pct))

    zone_label, zone_color = get_zone_data(m_value)

    st.markdown("### Spectre cognitif")

    st.markdown(f"""
    <div style="margin-top: 10px; margin-bottom: 8px;">
        <div style="
            position: relative;
            width: 100%;
            height: 34px;
            border-radius: 18px;
            overflow: hidden;
            background: linear-gradient(
                to right,
                #ff4b4b 0%,
                #ff4b4b 33.33%,
                #ff9f1c 33.33%,
                #ff9f1c 66.66%,
                #ffd60a 66.66%,
                #ffd60a 90%,
                #7bd389 90%,
                #7bd389 96%,
                #4cc9f0 96%,
                #4cc9f0 99%,
                #4361ee 99%,
                #4361ee 100%
            );
            box-shadow: inset 0 0 0 1px rgba(255,255,255,0.15);
        ">
            <div style="
                position: absolute;
                left: calc({width_pct}% - 10px);
                top: 2px;
                width: 20px;
                height: 30px;
                border-radius: 10px;
                background: white;
                border: 3px solid {zone_color};
                box-shadow: 0 0 10px rgba(0,0,0,0.25);
            "></div>
        </div>
        <div style="
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            margin-top: 6px;
            opacity: 0.9;
        ">
            <span>-10</span>
            <span>0</span>
            <span>10</span>
            <span>17</span>
            <span>19</span>
            <span>20</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption(f"Zone actuelle : {zone_label}")


def render_life_bar(m_value: float):
    min_spectrum = -10
    max_spectrum = 20
    normalized = (m_value - min_spectrum) / (max_spectrum - min_spectrum)
    normalized = max(0.0, min(1.0, normalized))

    zone_label, zone_color = get_zone_data(m_value)

    st.markdown("### Barre de vie cognitive")
    st.progress(normalized)

    st.markdown(f"""
    <div style="
        margin-top: 6px;
        padding: 10px 14px;
        border-left: 6px solid {zone_color};
        background: rgba(255,255,255,0.04);
        border-radius: 10px;
        font-size: 1rem;
    ">
        <strong>Énergie cognitive :</strong> {normalized * 100:.1f}%<br>
        <strong>État :</strong> {zone_label}
    </div>
    """, unsafe_allow_html=True)


st.title("🧠 Mécroyance App")
st.caption("Une petite boussole pour voir où se tient la cognition sur son fil tendu.")

col1, col2, col3 = st.columns(3)
with col1:
    g = st.slider("Gnosis (G)", 0.0, 10.0, 5.0, 0.1)
with col2:
    n = st.slider("Nous (N)", 0.0, 10.0, 5.0, 0.1)
with col3:
    d = st.slider("Doxa (D)", 0.0, 10.0, 5.0, 0.1)

c = Cognition(g, n, d)

mcol1, mcol2, mcol3, mcol4 = st.columns(4)
mcol1.metric("G", round(c.G, 2))
mcol2.metric("N", round(c.N, 2))
mcol3.metric("D", round(c.D, 2))
mcol4.metric("M", round(c.M, 2))

st.write(c.interpret())

render_spectrum(c.M)
render_life_bar(c.M)
