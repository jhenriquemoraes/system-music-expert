from models.facts import Facts
from knowledge.rules import RULES
from engine.inference_engine import InferenceEngine


def run_engine(facts: Facts) -> Facts:
    engine = InferenceEngine(RULES)
    return engine.run(facts)


def test_happy_major_beginner():

    facts = Facts(
        note="C",
        base_character="major",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "major"
    assert result.favored_character == "major"

    assert "tonic" in result.desired_functions

    assert "P1" in result.candidate_progressions

    assert result.selected_progressions == ["P1"]


def test_happy_major_with_resolution():

    facts = Facts(
        note="C",
        base_character="major",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=True
    )

    result = run_engine(facts)

    assert result.context == "major"

    assert "P1" in result.candidate_progressions
    assert "P3" in result.candidate_progressions

    assert result.selected_progressions == ["P3"]


def test_melancholic_major():

    facts = Facts(
        note="C",
        base_character="major",
        intention="melancholic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "major"

    assert result.favored_character == "minor"

    assert result.relative_minor_available is True

    assert "relative_minor" in result.desired_functions

    assert "P2" in result.candidate_progressions

    assert result.selected_progressions == ["P2"]


def test_tension_major_with_resolution():

    facts = Facts(
        note="C",
        base_character="major",
        intention="tension",
        level="intermediate",
        accepts_modal=False,
        wants_resolution=True
    )

    result = run_engine(facts)

    assert result.context == "major"

    assert result.needs_tension is True
    assert result.needs_resolution is True
    assert result.needs_preparation is True

    assert "predominant" in result.desired_functions
    assert "dominant" in result.desired_functions
    assert "tonic" in result.desired_functions

    assert "P4" in result.candidate_progressions

    assert result.selected_progressions == ["P4"]
    
def test_melancholic_minor_beginner():

    facts = Facts(
        note="A",
        base_character="minor",
        intention="melancholic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "minor"

    assert result.favored_character == "minor"

    assert "P6" in result.candidate_progressions

    assert result.selected_progressions == ["P6"]

    assert "R29" in result.fired_rules
    assert "R23" in result.fired_rules

def test_minor_tension_with_resolution():

    facts = Facts(
        note="A",
        base_character="minor",
        intention="tension",
        level="beginner",
        accepts_modal=False,
        wants_resolution=True
    )

    result = run_engine(facts)

    assert result.context == "minor"

    assert result.needs_tension is True
    assert result.needs_resolution is True

    assert result.major_dominant_allowed is True

    assert "dominant" in result.desired_functions
    assert "tonic" in result.desired_functions

    assert "P7" in result.candidate_progressions

    assert result.selected_progressions == ["P7"]

    assert "R24" in result.fired_rules
    assert "R25" in result.fired_rules
    
def test_minor_context_is_preserved_with_happy_intention():

    facts = Facts(
        note="A",
        base_character="minor",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    # O contexto explicitamente escolhido pelo usuário
    # deve ser preservado.
    assert result.context == "minor"

    # A intenção pode favorecer caráter maior,
    # mas não deve substituir o contexto escolhido.
    assert result.favored_character == "major"

    assert result.context != "major"
    
def test_mixolydian_energetic():

    facts = Facts(
        note="G",
        base_character="major",
        intention="energetic",
        level="beginner",
        accepts_modal=True,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "mixolydian"

    assert result.modal_characteristic_required is True

    assert "P5" in result.candidate_progressions

    assert result.selected_progressions == ["P5"]

    assert "R07" in result.fired_rules
    assert "R19" in result.fired_rules
    assert "R27" in result.fired_rules

def test_lydian_contemplative():

    facts = Facts(
        note="C",
        base_character="major",
        intention="contemplative",
        level="beginner",
        accepts_modal=True,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "lydian"

    assert result.modal_characteristic_required is True

    assert "P8" in result.candidate_progressions

    assert result.selected_progressions == ["P8"]

    assert "R08" in result.fired_rules
    assert "R26" in result.fired_rules
    assert "R27" in result.fired_rules

def test_energetic_without_modal_preserves_major():

    facts = Facts(
        note="G",
        base_character="major",
        intention="energetic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "major"

    assert result.modal_characteristic_required is False

    assert "P5" not in result.candidate_progressions

    assert "R07" not in result.fired_rules
    assert "R19" not in result.fired_rules
    assert "R27" not in result.fired_rules
    
def test_unknown_character_happy_infers_major():

    facts = Facts(
        note="C",
        base_character="unknown",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "major"

    assert result.needs_more_information is False

    assert "P1" in result.candidate_progressions

    assert result.selected_progressions == ["P1"]

    assert "R30" in result.fired_rules
    
def test_unknown_character_melancholic_infers_minor():

    facts = Facts(
        note="A",
        base_character="unknown",
        intention="melancholic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    result = run_engine(facts)

    assert result.context == "minor"

    assert result.needs_more_information is False

    assert "P6" in result.candidate_progressions

    assert result.selected_progressions == ["P6"]

    assert "R30" in result.fired_rules
    
def test_unknown_character_tension_requires_more_information():

    facts = Facts(
        note="A",
        base_character="unknown",
        intention="tension",
        level="beginner",
        accepts_modal=False,
        wants_resolution=True
    )

    result = run_engine(facts)

    assert result.context is None

    assert result.needs_more_information is True

    assert result.message is not None

    assert len(result.candidate_progressions) == 0

    assert len(result.selected_progressions) == 0

    assert "R30" in result.fired_rules