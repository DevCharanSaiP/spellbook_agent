import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import gradio as gr
from style import CSS   # <-- important: import the CSS string

# ------------ Load token and set up client ------------

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

client = InferenceClient(
    "meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN,
)

# ------------ Core spell-generation function ------------

def generate_spell(magic_type, difficulty, mood, extra_idea):
    prompt = f"""
You are a creative fantasy spell designer.

Create ONE original spell with:
- Magic type: {magic_type}
- Difficulty: {difficulty}
- Mood: {mood}
- Extra idea from user: {extra_idea}

Return it in this format:
Name:
Ingredients:
Incantation:
Effect:
"""

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=400,
        temperature=1.0,
    )

    return response.choices[0].message["content"]


# ------------ Gradio UI using external CSS ------------

with gr.Blocks() as demo:
    # inject CSS and title
    gr.HTML(
        CSS
        + """
        <div id="title-wrap">
          <h1>📖 Ancient Mystic Tome</h1>
          <p>Choose your magic and inscribe a new spell into the grimoire.</p>
        </div>
        """
    )

    with gr.Column(elem_classes=["spellbook-panel"]):
        with gr.Row():
            magic_type = gr.Dropdown(
                ["Fire", "Water", "Earth", "Air", "Shadow", "Light", "Arcane"],
                label="Magic Type",
                value="Fire",
            )
            difficulty = gr.Radio(
                ["Easy", "Medium", "Hard"],
                label="Difficulty",
                value="Medium",
            )
            mood = gr.Dropdown(
                ["Cheerful", "Mysterious", "Dark", "Epic"],
                label="Mood",
                value="Mysterious",
            )

        extra_idea = gr.Textbox(
            label="Extra idea (optional)",
            placeholder="e.g., Works only under a blood moon, powered by dragon scales...",
            lines=2,
        )

        generate_button = gr.Button("✒️ Inscribe Spell", variant="primary")

        # initial placeholder card
        output = gr.HTML(
            value="<div class='spell-card'><em>Your spell will appear here.</em></div>"
        )

        # wrapper to format raw text inside parchment card
        def generate_spell_html(magic_type, difficulty, mood, extra_idea):
            raw = generate_spell(magic_type, difficulty, mood, extra_idea)

            accent_map = {
                "Fire": "accent-fire",
                "Water": "accent-water",
                "Earth": "accent-earth",
                "Air": "accent-air",
                "Shadow": "accent-shadow",
                "Light": "accent-light",
                "Arcane": "accent-arcane",
            }
            accent_class = accent_map.get(magic_type, "accent-arcane")

            html = f"""
            <div class="spell-card">
              <h2 class="{accent_class}">{magic_type} Spell</h2>
              <pre>{raw.strip()}</pre>
            </div>
            """
            return html

        generate_button.click(
            fn=generate_spell_html,
            inputs=[magic_type, difficulty, mood, extra_idea],
            outputs=output,
        )


if __name__ == "__main__":
    demo.launch()