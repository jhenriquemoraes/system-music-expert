from models.facts import Facts
from knowledge.rules import Rule


class InferenceEngine:

    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def run(self, facts: Facts) -> Facts:

        fired_once = set()

        changed = True

        while changed:
            changed = False

            for rule in self.rules:

                # R22 é uma regra de seleção e pode
                # precisar ser reavaliada.
                repeatable = rule.id == "R22"

                if not repeatable and rule.id in fired_once:
                    continue

                if rule.condition(facts):

                    before = self._snapshot(facts)

                    rule.action(facts)

                    after = self._snapshot(facts)

                    if before != after:

                        if rule.id not in facts.fired_rules:
                            facts.fired_rules.append(rule.id)

                        changed = True

                    if not repeatable:
                        fired_once.add(rule.id)

        return facts

    @staticmethod
    def _snapshot(facts: Facts):
        return (
            facts.context,
            facts.favored_character,
            facts.needs_resolution,
            facts.needs_stability,
            facts.needs_tension,
            facts.needs_preparation,
            facts.emotional_contrast,
            facts.relative_minor_available,
            facts.major_dominant_allowed,
            facts.modal_characteristic_required,
            facts.needs_more_information,
            facts.message,
            frozenset(facts.desired_functions),
            frozenset(facts.candidate_progressions),
            tuple(facts.selected_progressions),
        )