from knowledge.harmony import build_scale
from knowledge.harmony import build_scale, build_harmonic_field, build_seventh_harmonic_field

def test_c_major_scale():

    scale = build_scale("C", "major")

    assert scale == [
        "C", "D", "E", "F", "G", "A", "B"
    ]


def test_a_minor_scale():

    scale = build_scale("A", "minor")

    assert scale == [
        "A", "B", "C", "D", "E", "F", "G"
    ]


def test_g_mixolydian_scale():

    scale = build_scale("G", "mixolydian")

    assert scale == [
        "G", "A", "B", "C", "D", "E", "F"
    ]


def test_c_lydian_scale():

    scale = build_scale("C", "lydian")

    assert scale == [
        "C", "D", "E", "F#", "G", "A", "B"
    ]
    
def test_c_major_harmonic_field():

    field = build_harmonic_field("C", "major")

    assert field == [
        "C",
        "Dm",
        "Em",
        "F",
        "G",
        "Am",
        "Bdim"
    ]

def test_a_minor_harmonic_field():

    field = build_harmonic_field("A", "minor")

    assert field == [
        "Am",
        "Bdim",
        "C",
        "Dm",
        "Em",
        "F",
        "G"
    ]
    

def test_c_major_seventh_harmonic_field():
    field = build_seventh_harmonic_field("C", "major")

    assert field == [
        "Cmaj7",
        "Dm7",
        "Em7",
        "Fmaj7",
        "G7",
        "Am7",
        "Bm7b5"
    ]


def test_a_minor_seventh_harmonic_field():
    field = build_seventh_harmonic_field("A", "minor")

    assert field == [
        "Am7",
        "Bm7b5",
        "Cmaj7",
        "Dm7",
        "Em7",
        "Fmaj7",
        "G7"
    ]