# Deploying Streamlit Apps

To deploy Streamlit apps, they need to be written and committed to a public Github repo.

## How to add a new Streamlit App

### 0. Create a streamlit secrets file and add your nilchain private key within `.streamlit/secrets.toml`

```
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

### 1. Create an app file in the streamlit_demo_apps folder

Check out the addition app file example:

`app_addition.py`

### 2. Copy the compiled Nada program files from the target/ folder into the streamlit_demo_apps/compiled_nada_programs folder

Check out the compiled Nada program files for addition:

nada binary `addition.nada.bin`
nada json `addition.nada.json`

### 3. Update your app file with the corresponding program name and program test name

Check out the addition app file example:

`app_addition.py`

```
program_name = 'addition'
program_test_name = 'addition_test'
```

### 4. Test your Streamlit app locally

Make sure the apps will work when deployed by testing this command from the root folder.

```
streamlit run streamlit_demo_apps/[app_file_name].py
```

For example to make sure the addition app will work when deployed, run

```
streamlit run streamlit_demo_apps/app_addition.py
```
