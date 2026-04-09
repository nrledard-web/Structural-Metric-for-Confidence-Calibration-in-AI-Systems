class Cognition:
    def __init__(self, gnosis: float, nous: float, doxa: float):
        self.G = self.clamp(gnosis)
        self.N = self.clamp(nous)
        self.D = self.clamp(doxa)
        self.M = self.compute_mecroyance()

    @staticmethod
    def clamp(value: float, min_val: float = 0.0, max_val: float = 10.0) -> float:
        """Force la valeur à rester dans l’échelle 0–10."""
        return max(min_val, min(max_val, value))

    def compute_mecroyance(self) -> float:
        """Calcule M selon la formule qualitative : (G + N) − D."""
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

    def update(self, delta_G: float = 0.0, delta_N: float = 0.0, delta_D: float = 0.0):
        """Ajuste les variables cognitives puis recalcule M."""
        self.G = self.clamp(self.G + delta_G)
        self.N = self.clamp(self.N + delta_N)
        self.D = self.clamp(self.D + delta_D)
        self.M = self.compute_mecroyance()

    def __repr__(self) -> str:
        return (
            f"Cognition(G={self.G:.1f}, N={self.N:.1f}, "
            f"D={self.D:.1f}, M={self.M:.1f})"
        )


class CognitiveAgent(Cognition):
    def feedback(self, success: bool):
        """
        Ajuste la doxa selon le retour d’expérience :
        - succès : légère consolidation
        - échec : baisse plus forte de la certitude pour rouvrir la révision
        """
        if success:
            self.update(delta_D=0.2)
        else:
            self.update(delta_D=-0.5)

        return self.M, self.interpret()


# Exemples d'utilisation
scenarios = {
    "complotiste": Cognition(2, 2, 8),
    "professionnel_technique": Cognition(7, 8, 6),
    "scientifique_autocorrectif": Cognition(9, 9, 2),
}

for nom, c in scenarios.items():
    print(f"{nom.upper()} → M={c.M:.1f} | {c.interpret()}")
