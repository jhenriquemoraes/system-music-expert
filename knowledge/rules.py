from dataclasses import dataclass
from typing import Callable

from models.facts import Facts


@dataclass
class Rule:
    id: str
    description: str
    condition: Callable[[Facts], bool]
    action: Callable[[Facts], None]


# =========================================================
# R01 - CONTEXTO MAIOR
# =========================================================

def r01_condition(facts: Facts) -> bool:
    return facts.context == "major"


def r01_action(facts: Facts) -> None:
    # O campo harmônico será utilizado posteriormente
    # pelo serviço responsável pela conversão dos graus.
    pass


R01 = Rule(
    id="R01",
    description="Utiliza a estrutura do campo harmônico maior.",
    condition=r01_condition,
    action=r01_action
)

# =========================================================
# R02 - CONTEXTO MENOR
# =========================================================

def r02_condition(facts: Facts) -> bool:
    return facts.context == "minor"


def r02_action(facts: Facts) -> None:
    # Utiliza inicialmente a estrutura do menor natural:
    # i - ii° - III - iv - v - VI - VII
    #
    # A alteração da dominante será tratada pela R24.
    pass


R02 = Rule(
    id="R02",
    description="Utiliza a estrutura do campo harmônico menor natural.",
    condition=r02_condition,
    action=r02_action
)

# =========================================================
# R03 - RELATIVO MENOR
# =========================================================

def r03_condition(facts: Facts) -> bool:
    return (
        facts.context == "major"
        and facts.favored_character == "minor"
    )


def r03_action(facts: Facts) -> None:
    facts.relative_minor_available = True


R03 = Rule(
    id="R03",
    description="Identifica o relativo menor no contexto maior.",
    condition=r03_condition,
    action=r03_action
)


# =========================================================
# R04 - INTENÇÃO ALEGRE
# =========================================================

def r04_condition(facts: Facts) -> bool:
    return facts.intention == "happy"


def r04_action(facts: Facts) -> None:
    facts.favored_character = "major"
    facts.needs_stability = True
    facts.desired_functions.add("tonic")


R04 = Rule(
    id="R04",
    description="Intenção alegre favorece caráter maior e estabilidade.",
    condition=r04_condition,
    action=r04_action
)


# =========================================================
# R05 - INTENÇÃO MELANCÓLICA
# =========================================================

def r05_condition(facts: Facts) -> bool:
    return facts.intention == "melancholic"


def r05_action(facts: Facts) -> None:
    facts.favored_character = "minor"
    facts.emotional_contrast = True


R05 = Rule(
    id="R05",
    description="Intenção melancólica favorece caráter menor.",
    condition=r05_condition,
    action=r05_action
)


# =========================================================
# R06 - TENSÃO
# =========================================================

def r06_condition(facts: Facts) -> bool:
    return facts.intention == "tension"


def r06_action(facts: Facts) -> None:
    facts.needs_tension = True
    facts.desired_functions.add("dominant")

    if facts.wants_resolution:
        facts.needs_resolution = True
        facts.needs_preparation = True


R06 = Rule(
    id="R06",
    description="Intenção de tensão favorece dominante e possível resolução.",
    condition=r06_condition,
    action=r06_action
)

# =========================================================
# R07 - CONTEXTO MIXOLÍDIO
# =========================================================

def r07_condition(facts: Facts) -> bool:
    return (
        facts.intention == "energetic"
        and facts.accepts_modal
        and facts.base_character == "major"
    )


def r07_action(facts: Facts) -> None:
    facts.context = "mixolydian"


R07 = Rule(
    id="R07",
    description=(
        "Intenção energética e aceitação modal "
        "permitem considerar o modo Mixolídio."
    ),
    condition=r07_condition,
    action=r07_action
)

# =========================================================
# R08 - CONTEXTO LÍDIO
# =========================================================

def r08_condition(facts: Facts) -> bool:
    return (
        facts.intention == "contemplative"
        and facts.accepts_modal
        and facts.base_character == "major"
    )


def r08_action(facts: Facts) -> None:
    facts.context = "lydian"


R08 = Rule(
    id="R08",
    description=(
        "Intenção contemplativa e aceitação modal "
        "permitem considerar o modo Lídio."
    ),
    condition=r08_condition,
    action=r08_action
)

# =========================================================
# R09 - PRIORIDADE TONAL
# =========================================================

def r09_condition(facts: Facts) -> bool:
    return (
        not facts.accepts_modal
        and facts.context in ("major", "minor")
    )


def r09_action(facts: Facts) -> None:
    # O contexto tonal já foi definido por R28/R29.
    # A regra registra a decisão de preservá-lo.
    pass


R09 = Rule(
    id="R09",
    description=(
        "Preserva o contexto tonal maior ou menor "
        "quando sonoridade modal não foi aceita."
    ),
    condition=r09_condition,
    action=r09_action
)

# =========================================================
# R10 - ESTABILIDADE
# =========================================================

def r10_condition(facts: Facts) -> bool:
    return facts.needs_stability


def r10_action(facts: Facts) -> None:
    facts.desired_functions.add("tonic")


R10 = Rule(
    id="R10",
    description="Necessidade de estabilidade prioriza função tônica.",
    condition=r10_condition,
    action=r10_action
)


# =========================================================
# R11 - PREPARAÇÃO
# =========================================================

def r11_condition(facts: Facts) -> bool:
    return facts.needs_preparation


def r11_action(facts: Facts) -> None:
    facts.desired_functions.add("predominant")


R11 = Rule(
    id="R11",
    description="Necessidade de preparação utiliza função predominante.",
    condition=r11_condition,
    action=r11_action
)


# =========================================================
# R12 - PREDOMINANTE → DOMINANTE
# =========================================================

def r12_condition(facts: Facts) -> bool:
    return (
        "predominant" in facts.desired_functions
        and facts.needs_tension
    )


def r12_action(facts: Facts) -> None:
    facts.desired_functions.add("dominant")


R12 = Rule(
    id="R12",
    description="Predominante conduz à dominante quando há tensão.",
    condition=r12_condition,
    action=r12_action
)


# =========================================================
# R13 - DOMINANTE → TÔNICA
# =========================================================

def r13_condition(facts: Facts) -> bool:
    return (
        "dominant" in facts.desired_functions
        and facts.needs_resolution
    )


def r13_action(facts: Facts) -> None:
    facts.desired_functions.add("tonic")


R13 = Rule(
    id="R13",
    description="Dominante conduz à tônica quando há resolução.",
    condition=r13_condition,
    action=r13_action
)


# =========================================================
# R14 - CONTRASTE PELO RELATIVO MENOR
# =========================================================

def r14_condition(facts: Facts) -> bool:
    return (
        facts.context == "major"
        and facts.emotional_contrast
        and facts.relative_minor_available
    )


def r14_action(facts: Facts) -> None:
    facts.desired_functions.add("relative_minor")


R14 = Rule(
    id="R14",
    description="Permite o relativo menor como região de contraste.",
    condition=r14_condition,
    action=r14_action
)


# =========================================================
# R15 - PROGRESSÃO MAIOR GERAL
# =========================================================

def r15_condition(facts: Facts) -> bool:
    return (
        facts.context == "major"
        and not facts.needs_tension
        and not facts.emotional_contrast
    )


def r15_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P1")


R15 = Rule(
    id="R15",
    description="Adiciona P1 como progressão geral do contexto maior.",
    condition=r15_condition,
    action=r15_action
)


# =========================================================
# R16 - RELATIVO MENOR
# =========================================================

def r16_condition(facts: Facts) -> bool:
    return (
        facts.intention == "melancholic"
        and facts.relative_minor_available
    )


def r16_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P2")


R16 = Rule(
    id="R16",
    description="Seleciona progressão que destaca o relativo menor.",
    condition=r16_condition,
    action=r16_action
)


# =========================================================
# R17 - ESTABILIDADE + RESOLUÇÃO
# =========================================================

def r17_condition(facts: Facts) -> bool:
    return (
        facts.context == "major"
        and facts.needs_stability
        and facts.wants_resolution
    )


def r17_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P3")


R17 = Rule(
    id="R17",
    description="Seleciona progressão maior com resolução clara.",
    condition=r17_condition,
    action=r17_action
)


# =========================================================
# R18 - PREPARAÇÃO + TENSÃO + RESOLUÇÃO
# =========================================================

def r18_condition(facts: Facts) -> bool:
    return (
        facts.context == "major"
        and facts.needs_preparation
        and facts.needs_tension
        and facts.needs_resolution
    )


def r18_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P4")


R18 = Rule(
    id="R18",
    description="Seleciona progressão de preparação, tensão e resolução.",
    condition=r18_condition,
    action=r18_action
)

# =========================================================
# R19 - PROGRESSÃO MIXOLÍDIA
# =========================================================

def r19_condition(facts: Facts) -> bool:
    return facts.context == "mixolydian"


def r19_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P5")


R19 = Rule(
    id="R19",
    description=(
        "Adiciona progressão simples que evidencia "
        "a característica do modo Mixolídio."
    ),
    condition=r19_condition,
    action=r19_action
)

# =========================================================
# R20 - INICIANTE
# =========================================================

def r20_condition(facts: Facts) -> bool:
    return facts.level == "beginner"


def r20_action(facts: Facts) -> None:
    # O filtro será relevante quando progressões com
    # complexidades diferentes forem implementadas.
    pass


R20 = Rule(
    id="R20",
    description="Prioriza progressões simples para iniciantes.",
    condition=r20_condition,
    action=r20_action
)


# =========================================================
# R21 - INTERMEDIÁRIO
# =========================================================

def r21_condition(facts: Facts) -> bool:
    return facts.level == "intermediate"


def r21_action(facts: Facts) -> None:
    # Futuramente permitirá extensões como V7, ii7 e Imaj7.
    pass


R21 = Rule(
    id="R21",
    description="Permite maior complexidade harmônica.",
    condition=r21_condition,
    action=r21_action
)


# =========================================================
# R22 - SELEÇÃO
# =========================================================

def r22_condition(facts: Facts) -> bool:
    return len(facts.candidate_progressions) > 0


def r22_action(facts: Facts) -> None:

    candidates = facts.candidate_progressions

    # =====================================================
    # CONTEXTOS MODAIS
    # =====================================================

    if (
        facts.context == "mixolydian"
        and facts.modal_characteristic_required
        and "P5" in candidates
    ):
        facts.selected_progressions = ["P5"]
        return

    if (
        facts.context == "lydian"
        and facts.modal_characteristic_required
        and "P8" in candidates
    ):
        facts.selected_progressions = ["P8"]
        return

    # =====================================================
    # CONTEXTO MENOR
    # =====================================================

    # Tensão + resolução no contexto menor.
    if (
        facts.context == "minor"
        and facts.needs_tension
        and facts.needs_resolution
        and "P7" in candidates
    ):
        facts.selected_progressions = ["P7"]
        return

    # Progressão menor simples/melancólica.
    if (
        facts.context == "minor"
        and facts.intention == "melancholic"
        and "P6" in candidates
    ):
        facts.selected_progressions = ["P6"]
        return

    # =====================================================
    # CONTEXTO MAIOR
    # =====================================================

    if (
        facts.context == "major"
        and facts.needs_tension
        and facts.needs_resolution
        and "P4" in candidates
    ):
        facts.selected_progressions = ["P4"]
        return

    if (
        facts.context == "major"
        and facts.intention == "melancholic"
        and "P2" in candidates
    ):
        facts.selected_progressions = ["P2"]
        return

    if (
        facts.context == "major"
        and facts.needs_stability
        and facts.wants_resolution
        and "P3" in candidates
    ):
        facts.selected_progressions = ["P3"]
        return

    if (
        facts.context == "major"
        and "P1" in candidates
    ):
        facts.selected_progressions = ["P1"]
        return

    # Caso nenhuma prioridade específica resolva.
    facts.selected_progressions = sorted(candidates)


R22 = Rule(
    id="R22",
    description="Seleciona a progressão mais adequada entre as candidatas.",
    condition=r22_condition,
    action=r22_action
)

# =========================================================
# R23 - PROGRESSÃO MENOR SIMPLES
# =========================================================

def r23_condition(facts: Facts) -> bool:
    return (
        facts.context == "minor"
        and facts.intention == "melancholic"
        and not facts.needs_tension
    )


def r23_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P6")


R23 = Rule(
    id="R23",
    description="Seleciona progressão menor simples e circular.",
    condition=r23_condition,
    action=r23_action
)


# =========================================================
# R24 - DOMINANTE MAIOR NO CONTEXTO MENOR
# =========================================================

def r24_condition(facts: Facts) -> bool:
    return (
        facts.context == "minor"
        and facts.needs_resolution
    )


def r24_action(facts: Facts) -> None:
    facts.major_dominant_allowed = True
    facts.desired_functions.add("dominant")


R24 = Rule(
    id="R24",
    description=(
        "Permite dominante maior no contexto menor "
        "quando uma resolução clara é necessária."
    ),
    condition=r24_condition,
    action=r24_action
)


# =========================================================
# R25 - MENOR COM TENSÃO E RESOLUÇÃO
# =========================================================

def r25_condition(facts: Facts) -> bool:
    return (
        facts.context == "minor"
        and facts.needs_tension
        and facts.needs_resolution
        and facts.major_dominant_allowed
    )


def r25_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P7")


R25 = Rule(
    id="R25",
    description="Seleciona progressão menor com tensão e resolução clara.",
    condition=r25_condition,
    action=r25_action
)

# =========================================================
# R26 - PROGRESSÃO LÍDIA
# =========================================================

def r26_condition(facts: Facts) -> bool:
    return facts.context == "lydian"


def r26_action(facts: Facts) -> None:
    facts.candidate_progressions.add("P8")


R26 = Rule(
    id="R26",
    description=(
        "Adiciona progressão simples que evidencia "
        "a sonoridade do modo Lídio."
    ),
    condition=r26_condition,
    action=r26_action
)

# =========================================================
# R27 - CARACTERÍSTICA MODAL
# =========================================================

def r27_condition(facts: Facts) -> bool:
    return facts.context in ("mixolydian", "lydian")


def r27_action(facts: Facts) -> None:
    facts.modal_characteristic_required = True


R27 = Rule(
    id="R27",
    description=(
        "Prioriza progressões que evidenciem "
        "a característica do contexto modal."
    ),
    condition=r27_condition,
    action=r27_action
)

# =========================================================
# R28 - CARÁTER BASE MAIOR
# =========================================================

def r28_condition(facts: Facts) -> bool:
    return (
        facts.base_character == "major"
        and facts.context is None
    )

def r28_action(facts: Facts) -> None:
    facts.context = "major"

R28 = Rule(
    id="R28",
    description="Define contexto maior a partir do caráter base.",
    condition=r28_condition,
    action=r28_action
)


# =========================================================
# R29 - CARÁTER BASE MENOR
# =========================================================

def r29_condition(facts: Facts) -> bool:
    return (
        facts.base_character == "minor"
        and facts.context is None
    )

def r29_action(facts: Facts) -> None:
    facts.context = "minor"

R29 = Rule(
    id="R29",
    description="Define contexto menor a partir do caráter base.",
    condition=r29_condition,
    action=r29_action
)

# =========================================================
# R30 - CARÁTER BASE DESCONHECIDO
# =========================================================

def r30_condition(facts: Facts) -> bool:
    return (
        facts.base_character == "unknown"
        and facts.context is None
    )


def r30_action(facts: Facts) -> None:

    # Intenção claramente associada ao caráter maior.
    if facts.intention == "happy":
        facts.context = "major"
        facts.needs_more_information = False
        facts.message = (
            "Contexto maior inferido a partir "
            "da intenção alegre."
        )
        return

    # Intenção claramente associada ao caráter menor.
    if facts.intention == "melancholic":
        facts.context = "minor"
        facts.needs_more_information = False
        facts.message = (
            "Contexto menor inferido a partir "
            "da intenção melancólica."
        )
        return

    # Intenções que não determinam sozinhas
    # um contexto maior ou menor.
    facts.needs_more_information = True
    facts.message = (
        "Não há informação suficiente para definir "
        "o contexto harmônico. Informe se prefere "
        "um caráter maior ou menor."
    )


R30 = Rule(
    id="R30",
    description=(
        "Infere maior ou menor quando possível ou solicita "
        "mais informação quando o caráter base é desconhecido."
    ),
    condition=r30_condition,
    action=r30_action
)

# =========================================================
# BASE DE CONHECIMENTO ATUAL
# =========================================================

RULES = [
    R15,
    R16,
    R17,
    R18,
    R19,

    R23,
    R24,
    R25,
    R26,
    R27,

    R22,

    R01,
    R02,
    R03,
    R04,
    R05,
    R06,
    R07,
    R08,
    R09,

    R10,
    R11,
    R12,
    R13,
    R14,

    R20,
    R21,

    R28,
    R29,
    R30,
]