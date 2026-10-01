NOTES = [
    "C", "C#", "D", "D#", "E", "F",
    "F#", "G", "G#", "A", "A#", "B"
]

MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]

NATURAL_MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]

MIXOLYDIAN_SCALE = [0, 2, 4, 5, 7, 9, 10]

LYDIAN_SCALE = [0, 2, 4, 6, 7, 9, 11]

CHORD_QUALITIES = {
    "major": [
        "major",
        "minor",
        "minor",
        "major",
        "major",
        "minor",
        "diminished"
    ],

    "minor": [
        "minor",
        "diminished",
        "major",
        "minor",
        "minor",
        "major",
        "major"
    ],

    "mixolydian": [
        "major",
        "minor",
        "diminished",
        "major",
        "minor",
        "minor",
        "major"
    ],

    "lydian": [
        "major",
        "major",
        "minor",
        "diminished",
        "major",
        "minor",
        "minor"
    ]
}

SEVENTH_CHORD_QUALITIES = {
    "major": [
        "major7",
        "minor7",
        "minor7",
        "major7",
        "dominant7",
        "minor7",
        "half_diminished7"
    ],

    "minor": [
        "minor7",
        "half_diminished7",
        "major7",
        "minor7",
        "minor7",
        "major7",
        "dominant7"
    ],

    "mixolydian": [
        "dominant7",
        "minor7",
        "half_diminished7",
        "major7",
        "minor7",
        "minor7",
        "major7"
    ],

    "lydian": [
        "major7",
        "dominant7",
        "minor7",
        "half_diminished7",
        "major7",
        "minor7",
        "minor7"
    ],
}

SCALES = {
    "major": MAJOR_SCALE,
    "minor": NATURAL_MINOR_SCALE,
    "mixolydian": MIXOLYDIAN_SCALE,
    "lydian": LYDIAN_SCALE
}

def build_scale(root: str, context: str) -> list[str]:

    root_index = NOTES.index(root)

    intervals = SCALES[context]

    scale = []

    for interval in intervals:
        note_index = (root_index + interval) % 12
        scale.append(NOTES[note_index])

    return scale

def build_chord(note: str, quality: str) -> str:
    if quality == "major":
        return note

    if quality == "minor":
        return f"{note}m"

    if quality == "diminished":
        return f"{note}dim"

    if quality == "major7":
        return f"{note}maj7"

    if quality == "minor7":
        return f"{note}m7"

    if quality == "dominant7":
        return f"{note}7"

    if quality == "half_diminished7":
        return f"{note}m7b5"

    raise ValueError(f"Qualidade de acorde desconhecida: {quality}")

def build_seventh_harmonic_field(
    root: str,
    context: str
) -> list[str]:

    scale = build_scale(root, context)
    qualities = SEVENTH_CHORD_QUALITIES[context]

    harmonic_field = []

    for note, quality in zip(scale, qualities):
        harmonic_field.append(
            build_chord(note, quality)
        )

    return harmonic_field

def build_harmonic_field(root: str, context: str) -> list[str]:

    scale = build_scale(root, context)

    qualities = CHORD_QUALITIES[context]

    harmonic_field = []

    for note, quality in zip(scale, qualities):
        chord = build_chord(note, quality)
        harmonic_field.append(chord)

    return harmonic_field