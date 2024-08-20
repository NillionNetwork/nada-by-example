# Deploying Streamlit Apps

Deployed Streamlit apps live here in the demo_apps folder.

## How to add a new Streamlit App

### 1. Create an app file in the demo_apps folder

Check out the addition app file example:

`app_addition.py`

### 2. Copy the compiled Nada program file from the target/ folder into the demo_apps/compiled_nada_programs folder

Check out the compiled Nada program file for addition:

`addition.nada.bin`

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
streamlit run demo_apps/[app_file_name].py
```

For example to make sure the addition app will work when deployed, run

```
streamlit run demo_apps/app_addition.py
```
