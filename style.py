# style.py
# Theme / CSS for Ancient Mystic Tome app
# Exports a single string variable `CSS` that the app imports and injects.
CSS = """
<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=MedievalSharp&family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

<style>
:root{
  --bg-1: #efe6d3;   /* parchment base */
  --bg-2: #f7f1df;   /* parchment highlight */
  --ink: #2b2b2b;
  --muted: #6b5f4a;
  --panel-shadow: 0 10px 30px rgba(17,12,6,0.25);
  --accent-fire: #e85a2a;
  --accent-water: #1f8fe8;
  --accent-earth: #7b5e2b;
  --accent-air: #6fb1d8;
  --accent-shadow: #6c4f84;
  --accent-light: #f3d86b;
  --accent-arcane: #9b59b6;
  --radius: 14px;
}

/* Page background: aged parchment with subtle noise-like overlay using gradients */
html, body {
  height: 100%;
  background: radial-gradient(1200px 600px at 10% 10%, rgba(255,255,255,0.25), transparent),
              linear-gradient(180deg, rgba(245,238,224,0.6), rgba(237,226,201,1));
  color: var(--ink);
  font-family: 'Inter', system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  margin: 0;
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
}

/* Title block inserted by app.py (keeps decorative feel) */
#title-wrap {
  max-width: 980px;
  margin: 28px auto 18px;
  text-align: center;
  padding: 18px 26px;
  background: linear-gradient(180deg, rgba(255,255,255,0.35), rgba(255,255,255,0.0));
  border-radius: 12px;
  box-shadow: var(--panel-shadow);
  border: 1px solid rgba(0,0,0,0.04);
}
#title-wrap h1{
  margin: 0 0 6px;
  font-family: 'MedievalSharp', 'Cormorant Garamond', serif;
  font-size: 36px;
  letter-spacing: 0.6px;
  color: #2b1f10;
  text-shadow: 0 1px 0 rgba(255,255,255,0.6);
}
#title-wrap p{
  margin: 0;
  color: var(--muted);
  font-size: 14px;
}

/* Main container produced by gr.Blocks -> we target the spellbook-panel column */
.spellbook-panel {
  max-width: 980px;
  margin: 22px auto;
  padding: 22px;
  background: linear-gradient(180deg, rgba(255,255,255,0.65), rgba(255,255,255,0.35));
  border-radius: 18px;
  box-shadow: var(--panel-shadow);
  border: 1px solid rgba(0,0,0,0.06);
  display: grid;
  gap: 18px;
}

/* Row/Inputs layout (gradio will place elements; this keeps spacing neat) */
.spellbook-panel .gr-row, .spellbook-panel .gradio-row {
  gap: 12px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

/* Inputs & controls */
.spellbook-panel label, .spellbook-panel .gr-label {
  color: #3a2f22;
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 6px;
  display:block;
}
.spellbook-panel .gr-dropdown, .spellbook-panel .gr-radio, .spellbook-panel .gr-textbox {
  min-width: 180px;
}

/* Buttons - give the primary button an ink-and-gold mystic look */
button, .gr-button, .gradio-button {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  padding: 10px 16px;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  box-shadow: 0 6px 16px rgba(43,43,43,0.12);
  transition: transform .12s ease, box-shadow .12s ease;
}
button:active, .gr-button:active { transform: translateY(1px); }
.gr-button[variant="primary"], .gr-button--primary, .gradio-button--primary {
  background: linear-gradient(180deg, #b8862b, #8b5a1e);
  color: white;
  text-shadow: 0 1px 0 rgba(0,0,0,0.25);
  border: 1px solid rgba(0,0,0,0.08);
}
.gr-button[variant="secondary"], .gr-button--secondary {
  background: transparent;
  border: 1px solid rgba(60,50,40,0.06);
  color: var(--muted);
}

/* Spell card (parchment sheet) */
.spell-card {
  background: linear-gradient(180deg, var(--bg-2), rgba(245,238,224,0.6));
  border-radius: 12px;
  padding: 18px;
  border: 1px solid rgba(80,65,40,0.08);
  box-shadow: 0 18px 40px rgba(28,20,8,0.18), inset 0 1px 0 rgba(255,255,255,0.4);
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  color: #241b12;
  line-height: 1.35;
  white-space: pre-wrap;
  word-break: break-word;
}

/* Spell card header (magic type) */
.spell-card h2 {
  margin: 0 0 10px 0;
  padding-bottom: 6px;
  font-family: 'MedievalSharp', 'Cormorant Garamond', serif;
  font-size: 22px;
  letter-spacing: 0.6px;
  display: inline-block;
  border-bottom: 1px dotted rgba(0,0,0,0.06);
}

/* Raw spell text inside pre - emulate inked handwriting */
.spell-card pre {
  margin: 10px 0 0;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  font-size: 15px;
  color: #2a1f15;
  background: transparent;
  border: none;
  padding: 0;
  white-space: pre-wrap;
}

/* Accent classes for magic types — used by app.py */
.accent-fire { color: var(--accent-fire); text-shadow: 0 1px 0 rgba(0,0,0,0.15); }
.accent-water { color: var(--accent-water); text-shadow: 0 1px 0 rgba(0,0,0,0.12); }
.accent-earth { color: var(--accent-earth); text-shadow: 0 1px 0 rgba(0,0,0,0.12); }
.accent-air { color: var(--accent-air); text-shadow: 0 1px 0 rgba(0,0,0,0.12); }
.accent-shadow { color: var(--accent-shadow); text-shadow: 0 2px 8px rgba(107,79,132,0.12); }
.accent-light { color: var(--accent-light); text-shadow: 0 1px 0 rgba(0,0,0,0.08); }
.accent-arcane { color: var(--accent-arcane); text-shadow: 0 1px 0 rgba(0,0,0,0.12); }

/* Small responsive tweaks */
@media (max-width: 880px){
  #title-wrap h1 { font-size: 28px; }
  .spellbook-panel { padding: 14px; margin: 14px; border-radius: 12px; }
  .spell-card { padding: 14px; }
}

/* subtle ornament in corners for an antique look */
.spellbook-panel:before, .spellbook-panel:after {
  content: "";
  position: absolute;
  width: 120px;
  height: 120px;
  pointer-events: none;
  opacity: 0.06;
  background: radial-gradient(circle at 30% 30%, rgba(0,0,0,0.06), transparent 40%);
  transform: rotate(-12deg);
}
.spellbook-panel { position: relative; overflow: visible; }

/* Focus styles for better accessibility */
input:focus, textarea:focus, select:focus, button:focus {
  outline: 3px solid rgba(155,89,182,0.12);
  outline-offset: 2px;
  box-shadow: 0 8px 24px rgba(155,89,182,0.06);
}

/* Lightweight helper for small notes */
.small-note {
  font-size: 12px;
  color: var(--muted);
  margin-top: 6px;
}

/* Ensure Gradio's root containers blend in nicely */
.gradio-container, .gradio-html {
  background: transparent !important;
}

/* make any icons inside the title a touch larger */
#title-wrap h1 emoji, #title-wrap h1 .emoji {
  font-size: 1.15em;
}
</style>
"""