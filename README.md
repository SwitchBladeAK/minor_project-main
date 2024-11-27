# UTI Prediction App

This Streamlit application predicts the likelihood of a urinary tract infection (UTI) based on user-provided urinalysis data. The prediction is made using a RandomForestClassifier model trained on a cleaned dataset of urinalysis results.
**Note**: This project was developed as a minor project under the guidance of Professor Aniruddha Deb

## Features

The app uses the following features for prediction:

- **Age**: The age of the patient.
- **Gender**: The gender of the patient (Male or Female).
- **Urine Color**: The color of the urine (categorical input).
- **Urine Transparency**: The transparency of the urine (categorical input).
- **Glucose in Urine**: Indicates the presence of glucose in the urine (categorical input).
- **Protein in Urine**: Indicates the presence of protein in the urine (categorical input).
- **pH Level**: The pH level of the urine (numeric input).
- **Specific Gravity**: The specific gravity of the urine (numeric input).
- **Epithelial Cells**: The number of epithelial cells present in the urine (categorical input).
- **Mucous Threads**: The presence of mucous threads in the urine (categorical input).
- **Amorphous Urates**: The presence of amorphous urates in the urine (categorical input).
- **Bacteria in Urine**: The presence of bacteria in the urine (categorical input).

## How to Use

1. **Install Streamlit**: If you haven’t already, install Streamlit using pip:

    ```bash
    pip install streamlit
    ```

2. **Clone the Repository**: Clone this repository to your local machine.

    ```bash
    git clone https://github.com/SwitchBladeAK/minor_project.git
    cd minor_project
    ```

3. **Prepare the Data**: Make sure you have the `Urinalysis_Cleaned.csv` file in the `data` directory. This file should contain the cleaned urinalysis dataset.

4. **Run the App**: Use Streamlit to run the application.

    ```bash
    streamlit run main.py
    ```

5. **Input Data**: In the app interface, input the patient's urinalysis data:
   - Enter the patient's age and pH level.
   - Select options for gender, urine color, transparency, glucose presence, protein presence, epithelial cells, mucous threads, amorphous urates, and bacteria.

6. **Predict**: Click the "Predict" button to see the prediction result:
   - **UTI POSITIVE**: Indicates a high likelihood of a UTI.
   - **UTI NEGATIVE**: Indicates a low likelihood of a UTI.

## Requirements

- Python 3.7 or higher
- Streamlit
- pandas
- numpy
- scikit-learn

## Dataset

The dataset used for training the model is `Urinalysis_Cleaned.csv`, which contains anonymized urinalysis results with various features that may indicate a UTI.

## Model

The model used in this app is a **RandomForestClassifier** from the `scikit-learn` library, trained on the urinalysis dataset to predict the presence of a UTI based on several input features.

## Acknowledgements

- **Streamlit** for providing an easy-to-use framework for creating web apps.
- **scikit-learn** for the machine learning model implementation.
