import sys
import os
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit_app  

def main():
    program_name = 'rock_paper_scissors'
    program_test_name = 'rock_paper_scissors_tie'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    compiled_nada_program_path = os.path.join(current_dir, "compiled_nada_programs", f"{program_name}.nada.bin")
    if not os.path.exists(compiled_nada_program_path):
        raise FileNotFoundError(f"Add `{program_name}.nada.bin` to the compiled_nada_programs folder.")

    streamlit_app.main(program_test_name, compiled_nada_program_path)

if __name__ == "__main__":
    main()