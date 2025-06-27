from spellchecker import SpellChecker
import language_tool_python

# Initialize tools
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')

def correct_spelling(text):
    words = text.split()
    corrected_words = []
    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)
    return ' '.join(corrected_words)

def correct_grammar(text):
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected

def full_corrector(text):
    spell_corrected = correct_spelling(text)
    grammar_corrected = correct_grammar(spell_corrected)
    return spell_corrected, grammar_corrected

# ---------- CLI Test ----------
if __name__ == "__main__":
    input_text = input("Enter your sentence:\n> ")
    spell_fixed, grammar_fixed = full_corrector(input_text)

    print("\n🔧 After Spell Correction:")
    print(spell_fixed)
    print("\n✅ Final Grammar-Corrected Text:")
    print(grammar_fixed)
