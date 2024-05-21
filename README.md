# VeriFacts: Streamlit Fake News Detector

VeriFacts is a machine learning project aimed at detecting fake news headlines using a Naive Bayes classifier. The project provides an interactive web interface built with Streamlit, allowing users to input news headlines and instantly receive predictions on their authenticity.

## Features

- **Fake News Detection**: Utilizes a machine learning model trained on a dataset of labeled news headlines to predict whether a given headline is fake or real.
- **User-Friendly Interface**: Offers a simple and intuitive web interface where users can easily interact with the model.
- **Example Predictions**: Demonstrates the model's capabilities with example predictions on predefined news headlines.
- **Dataset Exploration**: Includes a dataset of labeled news headlines for model training and evaluation.

## Installation and Usage

To use VeriFacts, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/verifacts.git


2. Install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install --no-cache-dir -r requirements.txt

3. Run the Streamlit app using the command `streamlit run app.py`.

   ```bash
   streamlit run app.py

4. Open your web browser and go to the URL provided by Streamlit (typically `http://localhost:8501`).

5. Enter a news headline in the text area and click the "Predict" button to see the prediction.

## Example Predictions

- **Headline**: "Iranian President Ebrahim Raisi Dies In Chopper Crash: Iran Media"
  - **Prediction**: Fake

- **Headline**: "Ginger Is 10,000x More Effective Than Chemotherapy"
  - **Prediction**: Real

## Dataset
The dataset used for training and evaluating the model is available in the dataset directory. It contains labeled news headlines indicating whether they are fake or real.

## Contributing
Contributions are welcome! If you have any ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
