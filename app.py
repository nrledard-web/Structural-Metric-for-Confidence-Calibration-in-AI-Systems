import streamlit as st

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

st.title("Mécroyance App")

g = st.slider("Gnosis (G)", 0.0, 10.0, 5.0)
n = st.slider("Nous (N)", 0.0, 10.0, 5.0)
d = st.slider("Doxa (D)", 0.0, 10.0, 5.0)

c = Cognition(g, n, d)

st.metric("M", round(c.M, 2))
st.write(c.interpret())
