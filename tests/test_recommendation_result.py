from models.recommendation_result import RecommendationResult


def test_create_recommendation_result():
    result = RecommendationResult(
        context="major",
        progression_id="P1",
        degrees=["I", "V", "vi", "IV"],
        chords=["C", "G", "Am", "F"],
        fired_rules=["R04", "R15", "R22", "R28"],
        message="Progressão recomendada com sucesso."
    )

    assert result.context == "major"
    assert result.progression_id == "P1"
    assert result.degrees == ["I", "V", "vi", "IV"]
    assert result.chords == ["C", "G", "Am", "F"]
    assert "R15" in result.fired_rules