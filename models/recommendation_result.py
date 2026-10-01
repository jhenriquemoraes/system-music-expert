from dataclasses import dataclass, field


@dataclass
class RecommendationResult:
    context: str | None
    progression_id: str | None
    degrees: list[str] = field(default_factory=list)
    chords: list[str] = field(default_factory=list)
    fired_rules: list[str] = field(default_factory=list)
    message: str | None = None
    explanation: str | None = None