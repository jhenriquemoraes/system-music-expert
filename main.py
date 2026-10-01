from models.facts import Facts
from knowledge.rules import RULES
from knowledge.progressions import PROGRESSIONS
from engine.inference_engine import InferenceEngine


def main():

    facts = Facts(
        note="C",
        base_character="major",
        intention="melancholic",
        level="beginner",
        accepts_modal=False,
        wants_resolution=False
    )

    engine = InferenceEngine(RULES)

    result = engine.run(facts)

    print("\n=== SISTEMA ESPECIALISTA MUSICAL ===")

    print(f"\nNota de referência: {result.note}")
    print(f"Contexto: {result.context}")
    print(f"Intenção: {result.intention}")
    print(f"Nível: {result.level}")

    print("\nFunções inferidas:")

    for function in sorted(result.desired_functions):
        print(f"- {function}")

    print("\nProgressões candidatas:")

    for progression_id in sorted(result.candidate_progressions):

        progression = PROGRESSIONS[progression_id]

        degrees = " - ".join(progression.degrees)

        print(f"- {progression.id}: {degrees}")

    print("\nProgressão selecionada:")

    for progression_id in result.selected_progressions:

        progression = PROGRESSIONS[progression_id]

        degrees = " - ".join(progression.degrees)

        print(f"{progression.id}: {degrees}")

    print("\nRegras disparadas:")

    for rule_id in result.fired_rules:
        print(f"- {rule_id}")


if __name__ == "__main__":
    main()