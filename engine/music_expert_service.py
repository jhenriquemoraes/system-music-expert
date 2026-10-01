from engine.inference_engine import InferenceEngine
from engine.harmony_converter import convert_progression
from knowledge.progressions import PROGRESSIONS
from knowledge.rules import RULES
from models.facts import Facts
from models.recommendation_result import RecommendationResult


class MusicExpertService:
    def __init__(self):
        self.engine = InferenceEngine(RULES)

    def recommend(
        self,
        note: str,
        base_character: str,
        intention: str,
        level: str,
        accepts_modal: bool,
        wants_resolution: bool
    ) -> RecommendationResult:

        facts = Facts(
            note=note,
            base_character=base_character,
            intention=intention,
            level=level,
            accepts_modal=accepts_modal,
            wants_resolution=wants_resolution
        )

        facts = self.engine.run(facts)

        # O sistema pode não possuir informações suficientes
        # para produzir uma recomendação.
        if facts.needs_more_information:
            return RecommendationResult(
                context=facts.context,
                progression_id=None,
                fired_rules=facts.fired_rules,
                message=facts.message
            )

        # Nenhuma progressão foi selecionada pelas regras.
        if not facts.selected_progressions:
            return RecommendationResult(
                context=facts.context,
                progression_id=None,
                fired_rules=facts.fired_rules,
                message="Nenhuma progressão compatível foi encontrada."
            )

        progression_id = facts.selected_progressions[0]
        progression = PROGRESSIONS[progression_id]

        chords = convert_progression(
        root=note,
        context=facts.context,
        progression_id=progression_id,
        level=facts.level
        )
        
        explanation = self._build_explanation(
            facts,
            progression_id
        )
        
        return RecommendationResult(
            context=facts.context,
            progression_id=progression_id,
            degrees=list(progression.degrees),
            chords=chords,
            fired_rules=facts.fired_rules,
            message="Progressão recomendada com sucesso.",
            explanation=explanation
        )
        
        
    def _build_explanation(
        self,
        facts: Facts,
        progression_id: str
    ) -> str:

        if facts.context == "mixolydian":
            return (
                "A sensação energética e aberta, combinada com a preferência "
                "por uma sonoridade menos convencional, levou o sistema a "
                "utilizar o contexto Mixolídio. A progressão escolhida destaca "
                "a característica desse contexto."
            )

        if facts.context == "lydian":
            return (
                "A sensação contemplativa e aberta, combinada com a preferência "
                "por uma sonoridade menos convencional, levou o sistema a "
                "utilizar o contexto Lídio. A progressão escolhida reforça "
                "a sonoridade característica desse contexto."
            )

        if progression_id == "P6":
            return (
                "A intenção melancólica e emocional favoreceu um contexto "
                "menor. O sistema escolheu uma progressão recorrente nesse "
                "contexto, preservando o caráter introspectivo desejado."
            )

        if progression_id == "P7":
            return (
                "A intenção de criar tensão com resolução favoreceu uma "
                "progressão em contexto menor que conduz à dominante e retorna "
                "à tônica, produzindo uma sensação mais clara de resolução."
            )

        if progression_id == "P4":
            return (
                "O sistema identificou a necessidade de preparação, tensão "
                "e resolução. Por isso, selecionou uma progressão que conduz "
                "da função predominante para a dominante e retorna à tônica."
            )

        if progression_id == "P3":
            return (
                "A preferência por estabilidade e resolução levou o sistema "
                "a escolher uma progressão que parte da tônica, cria movimento "
                "harmônico e retorna ao ponto de estabilidade."
            )

        if progression_id == "P2":
            return (
                "A intenção emocional favoreceu o destaque do relativo menor "
                "dentro do contexto maior, criando maior contraste emocional "
                "sem abandonar o campo harmônico principal."
            )

        if progression_id == "P1":
            return (
                "O sistema selecionou uma progressão simples e recorrente no "
                "contexto maior, adequada para criar uma base harmônica clara "
                "e acessível."
            )

        return (
            "A progressão foi selecionada por ser compatível com o contexto "
            "harmônico e com as preferências informadas."
        )