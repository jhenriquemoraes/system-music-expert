from dataclasses import dataclass


@dataclass(frozen=True)
class Progression:
    id: str
    degrees: tuple[str, ...]
    context: str
    characteristic: str


PROGRESSIONS = {
    "P1": Progression(
        id="P1",
        degrees=("I", "V", "vi", "IV"),
        context="major",
        characteristic="simple_pop"
    ),

    "P2": Progression(
        id="P2",
        degrees=("vi", "IV", "I", "V"),
        context="major",
        characteristic="relative_minor"
    ),

    "P3": Progression(
        id="P3",
        degrees=("I", "IV", "V", "I"),
        context="major",
        characteristic="stability_resolution"
    ),

    "P4": Progression(
        id="P4",
        degrees=("ii", "V", "I"),
        context="major",
        characteristic="preparation_tension_resolution"
    ),

    "P5": Progression(
        id="P5",
        degrees=("I", "bVII", "IV", "I"),
        context="mixolydian",
        characteristic="modal"
    ),

    "P6": Progression(
        id="P6",
        degrees=("i", "VI", "III", "VII"),
        context="minor",
        characteristic="minor_simple"
    ),

    "P7": Progression(
        id="P7",
        degrees=("i", "iv", "V", "i"),
        context="minor",
        characteristic="tension_resolution"
    ),

    "P8": Progression(
        id="P8",
        degrees=("I", "II", "I", "II"),
        context="lydian",
        characteristic="modal"
    ),
}