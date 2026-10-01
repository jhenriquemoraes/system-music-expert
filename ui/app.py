import tkinter as tk
from tkinter import ttk

from engine.music_expert_service import MusicExpertService


class MusicExpertApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Assistente de Composição Musical")
        self.root.geometry("720x680")
        self.root.minsize(650, 600)

        self.service = MusicExpertService()

        self.notes = [
            "C", "C#", "D", "D#", "E", "F",
            "F#", "G", "G#", "A", "A#", "B"
        ]

        self.intentions = {
            "Alegre e leve": "happy",
            "Melancólica e emocional": "melancholic",
            "Tensa, buscando resolução": "tension",
            "Energética e aberta": "energetic",
            "Contemplativa e aberta": "contemplative",
        }

        self.base_characters = {
            "Claro / aberto": "major",
            "Introspectivo / escuro": "minor",
            "Não sei / quero que o sistema escolha": "unknown",
        }

        self.sonorities = {
            "Mais familiar": False,
            "Pode ser um pouco diferente": True,
        }

        self.levels = {
            "Simples, com poucos acordes": "beginner",
            "Um pouco mais elaborado": "intermediate",
        }

        self.context_names = {
            "major": "Maior",
            "minor": "Menor",
            "mixolydian": "Mixolídio",
            "lydian": "Lídio",
        }

        self._build_interface()

    def _build_interface(self):
        main_frame = ttk.Frame(
            self.root,
            padding=30
        )
        main_frame.pack(
            fill="both",
            expand=True
        )

        # Título
        title = ttk.Label(
            main_frame,
            text="Assistente de Composição Musical",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=(0, 5))

        subtitle = ttk.Label(
            main_frame,
            text=(
                "Escolha as características da música "
                "que você deseja criar."
            ),
            font=("Segoe UI", 10)
        )
        subtitle.pack(pady=(0, 25))

        # =====================================================
        # FORMULÁRIO
        # =====================================================

        form = ttk.Frame(main_frame)
        form.pack(fill="x")

        # Nota
        ttk.Label(
            form,
            text="Nota inicial:"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8
        )

        self.note_var = tk.StringVar(value="C")

        self.note_combo = ttk.Combobox(
            form,
            textvariable=self.note_var,
            values=self.notes,
            state="readonly",
            width=35
        )
        self.note_combo.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=8
        )

        # Sensação
        ttk.Label(
            form,
            text="Sensação desejada:"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8
        )

        self.intention_var = tk.StringVar(
            value="Alegre e leve"
        )

        self.intention_combo = ttk.Combobox(
            form,
            textvariable=self.intention_var,
            values=list(self.intentions.keys()),
            state="readonly",
            width=35
        )
        self.intention_combo.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=8
        )

        # Caráter
        ttk.Label(
            form,
            text="Caráter:"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=8
        )

        self.character_var = tk.StringVar(
            value="Claro / aberto"
        )

        self.character_combo = ttk.Combobox(
            form,
            textvariable=self.character_var,
            values=list(self.base_characters.keys()),
            state="readonly",
            width=35
        )
        self.character_combo.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=8
        )

        # Sonoridade
        ttk.Label(
            form,
            text="Sonoridade:"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=8
        )

        self.sonority_var = tk.StringVar(
            value="Mais familiar"
        )

        self.sonority_combo = ttk.Combobox(
            form,
            textvariable=self.sonority_var,
            values=list(self.sonorities.keys()),
            state="readonly",
            width=35
        )
        self.sonority_combo.grid(
            row=3,
            column=1,
            sticky="ew",
            pady=8
        )

        # Complexidade
        ttk.Label(
            form,
            text="Complexidade:"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=8
        )

        self.level_var = tk.StringVar(
            value="Simples, com poucos acordes"
        )

        self.level_combo = ttk.Combobox(
            form,
            textvariable=self.level_var,
            values=list(self.levels.keys()),
            state="readonly",
            width=35
        )
        self.level_combo.grid(
            row=4,
            column=1,
            sticky="ew",
            pady=8
        )

        form.columnconfigure(1, weight=1)

        # =====================================================
        # BOTÃO
        # =====================================================

        generate_button = ttk.Button(
            main_frame,
            text="Gerar sugestão",
            command=self._generate_recommendation
        )
        generate_button.pack(pady=25)

        # =====================================================
        # RESULTADO
        # =====================================================

        result_frame = ttk.LabelFrame(
            main_frame,
            text="Recomendação",
            padding=20
        )
        result_frame.pack(
            fill="both",
            expand=True
        )

        # Contexto harmônico
        self.context_label = ttk.Label(
            result_frame,
            text="Contexto harmônico: —"
        )
        self.context_label.pack(
            anchor="w",
            pady=4
        )

        # Complexidade
        self.level_label = ttk.Label(
            result_frame,
            text="Complexidade: —"
        )
        self.level_label.pack(
            anchor="w",
            pady=4
        )

        # Progressão
        self.progression_label = ttk.Label(
            result_frame,
            text="Progressão: —"
        )
        self.progression_label.pack(
            anchor="w",
            pady=4
        )

        # Acordes
        self.chords_label = ttk.Label(
            result_frame,
            text="Acordes sugeridos: —",
            font=("Segoe UI", 12, "bold")
        )
        self.chords_label.pack(
            anchor="w",
            pady=4
        )

        ttk.Separator(
            result_frame,
            orient="horizontal"
        ).pack(
            fill="x",
            pady=15
        )

        # Explicação
        ttk.Label(
            result_frame,
            text="Por que esta sugestão?",
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.explanation_label = ttk.Label(
            result_frame,
            text=(
                "Escolha as características acima "
                "e clique em Gerar sugestão."
            ),
            wraplength=580,
            justify="left"
        )
        self.explanation_label.pack(
            anchor="w",
            pady=(8, 0)
        )

    def _generate_recommendation(self):
        intention = self.intentions[
            self.intention_var.get()
        ]

        base_character = self.base_characters[
            self.character_var.get()
        ]

        accepts_modal = self.sonorities[
            self.sonority_var.get()
        ]

        level = self.levels[
            self.level_var.get()
        ]

        wants_resolution = intention == "tension"

        result = self.service.recommend(
            note=self.note_var.get(),
            base_character=base_character,
            intention=intention,
            level=level,
            accepts_modal=accepts_modal,
            wants_resolution=wants_resolution
        )

        # Traduz o nível técnico para uma descrição
        # compreensível ao usuário.
        level_name = (
            "Simples"
            if level == "beginner"
            else "Intermediária"
        )

        self._show_result(
            result,
            level_name
        )

    def _show_result(self, result, level_name):
        # Caso o sistema não consiga produzir
        # uma recomendação.
        if result.progression_id is None:
            self.context_label.config(
                text="Contexto harmônico: —"
            )

            self.level_label.config(
                text="Complexidade: —"
            )

            self.progression_label.config(
                text="Progressão: —"
            )

            self.chords_label.config(
                text="Acordes sugeridos: —"
            )

            self.explanation_label.config(
                text=result.message
            )

            return

        # Traduz o nome interno do contexto.
        context_name = self.context_names.get(
            result.context,
            result.context
        )

        self.context_label.config(
            text=f"Contexto harmônico: {context_name}"
        )

        self.level_label.config(
            text=f"Complexidade: {level_name}"
        )

        self.progression_label.config(
            text=(
                "Progressão: "
                + " – ".join(result.degrees)
            )
        )

        self.chords_label.config(
            text=(
                "Acordes sugeridos: "
                + " – ".join(result.chords)
            )
        )

        self.explanation_label.config(
            text=(
                result.explanation
                or result.message
                or ""
            )
        )

    def run(self):
        self.root.mainloop()