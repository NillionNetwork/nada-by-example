# Deploying Streamlit Apps

Follow the steps to deploy a live Streamlit app for your Nada program and test file. The app will connect to the Nillion Testnet to store your Nada program, store secret inputs (or use computation time secrets), and run blind computation.

## How to add a new Streamlit App

### 0. Create a streamlit secrets file

Run this command to create a `.streamlit/secrets.toml` copied from the example.

```
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Add your Nilchain private key to the .streamlit/secrets.toml file. The private key must be linked to a funded Nillion Testnet address that was created using a Google account (not a mnemonic). This allows you to retrieve the private key from Keplr. If you don’t have a Testnet wallet yet, you can learn how to create one here: https://docs.nillion.com/testnet-guides

### 1. Run the script to generate a new streamlit app for your program

From the root folder of this repo, run the generate-streamlit-app script:

```
python3 generate-streamlit-app.py
```

### 2. Follow the prompts to

- Select an existing program (from the src/ directory)
- Select an existing yaml test file for your program (from the tests/ directory)

This will generate a Streamlit app file: streamlit_demo_apps/app_[your_program_name].py. The script will run the Streamlit app locally with this command

```
streamlit run streamlit_demo_apps/app_[your_program_name].py`
```

### 3. Test your Streamlit app locally

View the app in your browser to make sure everything works as expected.

### 4. Commit your code to GitHub

Add and commit your new streamlit app code to your forked Github repo. (Code must be connected to a remote, open source GitHub repository to deploy a Streamlit app.)

```
git add .
git commit -m "my new streamlit nillion app"
git push origin main
```

Once you've committed the open source code, you can click the "deploy" button within your local streamlit app. Sign in with Github and select the "Deploy Now" on Streamlit Community Cloud option to deploy the app for free.

  <img width="1000" alt="Streamlit Community Cloud" src="https://github.com/user-attachments/assets/74a70b4e-506c-41df-8d59-f949871c9a4e">


### 5. Deploy your app from Streamlit.io

When you click "Deploy Now" from your local app, you'll be taken to streamlit.io and asked to log in with Github to create a new Streamlit app. Set the main file path to your new app `streamlit_demo_apps/app_[your_program_name].py`

  <img width="1000" alt="streamlit settings" src="https://github.com/user-attachments/assets/e3821aa4-44b6-4f16-8400-97e531dfef23">

#### Add your Nilchain Private Key using Advanced Settings > Secrets

Go to "Advanced settings" and in Secrets, copy in the contents of your .streamlit/secrets.toml file. At a minimum, make sure to add your secret private key:

```
nilchain_private_key = "YOUR_FUNDED_PRIVATE_KEY"
```

  <img width="1000" alt="advanced settings" src="https://github.com/user-attachments/assets/6b48b225-60b7-41bd-8591-c04419131bf8">

Save and click "Deploy" to deploy your testnet-connected Streamlit app. 

### 6. Access Your Live Streamlit App

Once deployed, you’ll get a live link to your Nillion Testnet Streamlit app!

Example live Streamlit App: https://stephs-nada-multiplication-app.streamlit.app/
