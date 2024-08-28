import sys
import os
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit_app  

def main():
    # compiled with nucleus latest-experimental nillion -V 
    # tools-config 668efb7426c02c0e7c037d84157d08a524871fbd
    program_name = 'multiplication'
    program_test_name = 'multiplication_test'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    compiled_nada_program_path = os.path.join(current_dir, "compiled_nada_programs", f"{program_name}.nada.bin")
    if not os.path.exists(compiled_nada_program_path):
        raise FileNotFoundError(f"Add `{program_name}.nada.bin` to the compiled_nada_programs folder.")
    streamlit_app.main(program_test_name, compiled_nada_program_path)

if __name__ == "__main__":
    main()
    