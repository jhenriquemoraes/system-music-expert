from engine.music_expert_service import MusicExpertService


NOTES = [
    "C", "C#", "D", "D#", "E", "F",
    "F#", "G", "G#", "A", "A#", "B"
]

INTENTIONS = {
    "1": ("Alegre e leve", "happy"),
    "2": ("Melancólica e emocional", "melancholic"),
    "3": ("Tensa, buscando resolução", "tension"),
    "4": ("Energética e aberta", "energetic"),
    "5": ("Contemplativa e aberta", "contemplative"),
}

BASE_CHARACTERS = {
    "1": ("Claro / aberto", "major"),
    "2": ("Introspectivo / escuro", "minor"),
    "3": ("Não sei", "unknown"),
}

LEVELS = {
    "1": ("Simples, com poucos acordes", "beginner"),
    "2": ("Um pouco mais elaborado", "intermediate"),
}

SONORITIES = {
    "1": ("Mais familiar", False),
    "2": ("Pode ser um pouco diferente", True),
}


def choose_option(title, options):
    print(f"\n{title}")

    for key, value in options.items():
        print(f"{key} - {value[0]}")

    while True:
        choice = input("\nEscolha uma opção: ").strip()

        if choice in options:
            return options[choice][1]

        print("Opção inválida. Tente novamente.")


def choose_note():
    print("\nQual nota você gostaria de usar como ponto de partida?")

    for index, note in enumerate(NOTES, start=1):
        print(f"{index} - {note}")

    while True:
        choice = input("\nEscolha uma nota: ").strip()

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(NOTES):
                return NOTES[index]

        print("Opção inválida. Tente novamente.")


def show_result(result):
    print("\n" + "=" * 50)
    print("RECOMENDAÇÃO")
    print("=" * 50)

    if result.progression_id is None:
        print(result.message)
        return

    print(f"\nContexto harmônico: {result.context}")

    print(
        "Progressão: "
        + " - ".join(result.degrees)
    )

    print(
        "Acordes sugeridos: "
        + " - ".join(result.chords)
    )

    if result.message:
        print(f"\n{result.message}")


def main():
    print("=" * 50)
    print("ASSISTENTE DE COMPOSIÇÃO MUSICAL")
    print("=" * 50)

    print(
        "\nResponda algumas perguntas sobre a música que "
        "você deseja criar."
    )

    note = choose_note()

    intention = choose_option(
        "Qual sensação você quer transmitir?",
        INTENTIONS
    )

    base_character = choose_option(
        "Qual caráter você prefere para a música?",
        BASE_CHARACTERS
    )

    accepts_modal = choose_option(
        "Que tipo de sonoridade você prefere?",
        SONORITIES
    )

    level = choose_option(
        "Qual nível de complexidade você prefere?",
        LEVELS
    )

    wants_resolution = intention == "tension"

    service = MusicExpertService()

    result = service.recommend(
        note=note,
        base_character=base_character,
        intention=intention,
        level=level,
        accepts_modal=accepts_modal,
        wants_resolution=wants_resolution
    )

    show_result(result)
    if result.explanation:
        print("\nPor que esta sugestão?")
        print(result.explanation)

    if result.message:
        print(f"\n{result.message}")


if __name__ == "__main__":
    main()