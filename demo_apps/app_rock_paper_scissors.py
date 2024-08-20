import sys
import os
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit_app  

def main():
    streamlit_app.main('rock_paper_scissors_paper')

if __name__ == "__main__":
    main()