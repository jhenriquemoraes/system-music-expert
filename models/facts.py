from dataclasses import dataclass, field


@dataclass
class Facts:
    # =====================================================
    # FATOS INFORMADOS PELO USUÁRIO
    # =====================================================

    note: str
    base_character: str
    intention: str
    level: str
    accepts_modal: bool
    wants_resolution: bool

    # =====================================================
    # FATOS INFERIDOS PELO SISTEMA
    # =====================================================

    context: str | None = None
    favored_character: str | None = None

    needs_resolution: bool = False
    needs_stability: bool = False
    needs_tension: bool = False
    needs_preparation: bool = False
    emotional_contrast: bool = False
    relative_minor_available: bool = False
    major_dominant_allowed: bool = False
    modal_characteristic_required: bool = False

    needs_more_information: bool = False
    message: str | None = None
    
    desired_functions: set[str] = field(default_factory=set)

    candidate_progressions: set[str] = field(default_factory=set)

    selected_progressions: list[str] = field(default_factory=list)

    # =====================================================
    # RASTREABILIDADE
    # =====================================================

    fired_rules: list[str] = field(default_factory=list)