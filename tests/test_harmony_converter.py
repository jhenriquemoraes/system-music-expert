from engine.harmony_converter import convert_progression
from knowledge.progressions import PROGRESSIONS

def test_p1_c_major():

    chords = convert_progression(
        root="C",
        context="major",
        progression_id="P1"
    )

    assert chords == [
        "C",
        "G",
        "Am",
        "F"
    ]
    
def test_p2_d_major():

    chords = convert_progression(
        root="D",
        context="major",
        progression_id="P2"
    )

    assert chords == [
        "Bm",
        "G",
        "D",
        "A"
    ]
    
def test_p6_a_minor():

    chords = convert_progression(
        root="A",
        context="minor",
        progression_id="P6"
    )

    assert chords == [
        "Am",
        "F",
        "C",
        "G"
    ]
    
def test_p7_a_minor_with_major_dominant():

    chords = convert_progression(
        root="A",
        context="minor",
        progression_id="P7"
    )

    assert chords == [
        "Am",
        "Dm",
        "E",
        "Am"
    ]
    
def test_p5_g_mixolydian():

    chords = convert_progression(
        root="G",
        context="mixolydian",
        progression_id="P5"
    )

    assert chords == [
        "G",
        "F",
        "C",
        "G"
    ]
    
def test_p8_c_lydian():

    chords = convert_progression(
        root="C",
        context="lydian",
        progression_id="P8"
    )

    assert chords == [
        "C",
        "D",
        "C",
        "D"
    ]

def test_p1_c_major_intermediate():
    assert convert_progression(
        "C",
        "major",
        "P1",
        level="intermediate"
    ) == [
        "Cmaj7",
        "G7",
        "Am7",
        "Fmaj7"
    ]


def test_p4_c_major_intermediate():
    assert convert_progression(
        "C",
        "major",
        "P4",
        level="intermediate"
    ) == [
        "Dm7",
        "G7",
        "Cmaj7"
    ]


def test_p7_a_minor_intermediate_with_major_dominant():
    assert convert_progression(
        "A",
        "minor",
        "P7",
        level="intermediate"
    ) == [
        "Am7",
        "Dm7",
        "E7",
        "Am7"
    ]