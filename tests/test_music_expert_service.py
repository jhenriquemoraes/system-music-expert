from engine.music_expert_service import MusicExpertService


def test_recommend_major_happy_beginner():
    service = MusicExpertService()

    result = service.recommend(
        note="C",
        base_character="major",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    assert result.context == "major"
    assert result.progression_id == "P1"
    assert result.degrees == ["I", "V", "vi", "IV"]
    assert result.chords == ["C", "G", "Am", "F"]
    assert result.message == "Progressão recomendada com sucesso."
    assert result.explanation is not None
    assert len(result.explanation) > 0
    
    
def test_recommend_minor_melancholic_beginner():
    service = MusicExpertService()

    result = service.recommend(
        note="A",
        base_character="minor",
        intention="melancholic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    assert result.context == "minor"
    assert result.progression_id == "P6"
    assert result.degrees == ["i", "VI", "III", "VII"]
    assert result.chords == ["Am", "F", "C", "G"]


def test_recommend_minor_with_tension_and_resolution():
    service = MusicExpertService()

    result = service.recommend(
        note="A",
        base_character="minor",
        intention="tension",
        level="beginner",
        accepts_modal=False,
        wants_resolution=True
    )

    assert result.context == "minor"
    assert result.progression_id == "P7"
    assert result.degrees == ["i", "iv", "V", "i"]
    assert result.chords == ["Am", "Dm", "E", "Am"]


def test_recommend_unknown_happy_infers_major():
    service = MusicExpertService()

    result = service.recommend(
        note="C",
        base_character="unknown",
        intention="happy",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    assert result.context == "major"
    assert result.progression_id == "P1"
    assert result.chords == ["C", "G", "Am", "F"]


def test_unknown_tension_requires_more_information():
    service = MusicExpertService()

    result = service.recommend(
        note="C",
        base_character="unknown",
        intention="tension",
        level="beginner",
        accepts_modal=False,
        wants_resolution=True
    )

    assert result.context is None
    assert result.progression_id is None
    assert result.degrees == []
    assert result.chords == []
    assert result.message is not None
    
def test_recommend_energetic_as_mixolydian():
    service = MusicExpertService()

    result = service.recommend(
        note="G",
        base_character="major",
        intention="energetic",
        level="beginner",
        accepts_modal=True,
        wants_resolution=False
    )

    assert result.context == "mixolydian"
    assert result.progression_id == "P5"
    assert result.degrees == ["I", "bVII", "IV", "I"]
    assert result.chords == ["G", "F", "C", "G"]
    assert result.explanation is not None
    assert "Mixolídio" in result.explanation
    
def test_recommend_contemplative_as_lydian():
    service = MusicExpertService()

    result = service.recommend(
        note="C",
        base_character="major",
        intention="contemplative",
        level="beginner",
        accepts_modal=True,
        wants_resolution=False
    )

    assert result.context == "lydian"
    assert result.progression_id == "P8"
    assert result.degrees == ["I", "II", "I", "II"]
    assert result.chords == ["C", "D", "C", "D"]
    assert result.explanation is not None
    assert "Lídio" in result.explanation    

def test_recommend_major_happy_intermediate():
    service = MusicExpertService()

    result = service.recommend(
        note="C",
        base_character="major",
        intention="happy",
        level="intermediate",
        accepts_modal=False,
        wants_resolution=False
    )

    assert result.context == "major"
    assert result.progression_id == "P1"
    assert result.degrees == ["I", "V", "vi", "IV"]
    assert result.chords == [
        "Cmaj7",
        "G7",
        "Am7",
        "Fmaj7"
    ]
    
def test_recommend_minor_tension_intermediate():
    service = MusicExpertService()

    result = service.recommend(
        note="A",
        base_character="minor",
        intention="tension",
        level="intermediate",
        accepts_modal=False,
        wants_resolution=True
    )

    assert result.context == "minor"
    assert result.progression_id == "P7"
    assert result.degrees == ["i", "iv", "V", "i"]
    assert result.chords == [
        "Am7",
        "Dm7",
        "E7",
        "Am7"
    ]