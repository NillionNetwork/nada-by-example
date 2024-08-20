import sys
import os
import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit_app  

def main():
    streamlit_app.main('addition_test')

if __name__ == "__main__":
    main()