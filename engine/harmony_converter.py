from knowledge.harmony import build_harmonic_field
from knowledge.progressions import PROGRESSIONS


DEGREE_INDEXES = {
    "I": 0,
    "i": 0,

    "II": 1,
    "ii": 1,
    "ii°": 1,

    "III": 2,
    "iii": 2,

    "IV": 3,
    "iv": 3,

    "V": 4,
    "v": 4,

    "VI": 5,
    "vi": 5,

    "VII": 6,
    "vii°": 6,

    "bVII": 6,
}


def convert_progression(
    root: str,
    context: str,
    progression_id: str
) -> list[str]:

    progression = PROGRESSIONS[progression_id]

    harmonic_field = build_harmonic_field(root, context)

    chords = []

    for degree in progression.degrees:

        degree_index = DEGREE_INDEXES[degree]

        chord = harmonic_field[degree_index]

        # P7 utiliza V maior no contexto menor.
        if (
            progression_id == "P7"
            and degree == "V"
            and context == "minor"
        ):
            note = chord.removesuffix("m")
            chord = note

        chords.append(chord)

    return chords