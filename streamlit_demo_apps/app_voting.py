import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit_app  

program_name = 'voting'
program_test_name = 'voting_test'

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_nada_bin = os.path.join(current_dir, "compiled_nada_programs", f"{program_name}.nada.bin")
    path_nada_json = os.path.join(current_dir, "compiled_nada_programs", f"{program_name}.nada.json")
    if not os.path.exists(path_nada_bin):
        raise FileNotFoundError(f"Add `{program_name}.nada.bin` to the compiled_nada_programs folder.")
    if not os.path.exists(path_nada_json):
        raise FileNotFoundError(f"Run nada build --mir-json and add `{program_name}.nada.json` to the compiled_nada_programs folder.")
    streamlit_app.main(program_test_name, path_nada_bin, path_nada_json)

if __name__ == "__main__":
    main()
    