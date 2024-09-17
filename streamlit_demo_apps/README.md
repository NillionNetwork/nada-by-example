# Deploying Streamlit Apps

To deploy Streamlit apps, they need to be written and committed to a public Github repo.

## How to add a new Streamlit App

### 0. Create a streamlit secrets file and add your nilchain private key within `.streamlit/secrets.toml`

```
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

### 1. Run the script to generate a new streamlit app for your program

From the root folder of this repo, run the generate-streamlit-app script:

```
python3 generate-streamlit-app.py
```

### 2. Follow the prompts to

- Select an existing program (from the src/ directory)
- Select an existing yaml test file for your program (from the tests/ directory)

This will generate a Streamlit app file: streamlit*demo_apps/app*[your_program_name].py. The script will run the Streamlit app locally with this command

```
streamlit run streamlit_demo_apps/app_[your_program_name].py`
```

### 3. Test your Streamlit app locally

View the app in your browser to make sure everything works as expected.

### 4. Deploy your app

Add and commit your new streamlit app code to your forked Github repo. (Code must be connected to a remote, open source GitHub repository to deploy a Streamlit app.)

```
git add .
git commit -m "my new streamlit nillion app"
git push origin main
```

Once you've committed the open source code, you can click the "deploy" button within your local streamlit app. Sign in with Github and select the "Deploy Now" on Streamlit Community Cloud option to deploy the app for free.

#### Deploy an app settings

Set the main file path to your new app `streamlit_demo_apps/app_[your_program_name].py`

Go to "Advanced settings" and in Secrets, copy in the contents of your .streamlit/secrets.toml file. At a minimum, make sure to add your secret private key:

```
nilchain_private_key = "YOUR_FUNDED_PRIVATE_KEY"
```

Save and click "Deploy" to deploy your testnet Streamlit app!
