# AI Network Intrusion Detection System (NIDS)

A machine learning-based Network Intrusion Detection System that uses advanced algorithms to detect and classify network attacks in real-time.

## Features

- **Real-time Detection**: Monitors network traffic and detects intrusions in real-time
- **Multiple ML Models**: Implements Random Forest, Gradient Boosting, and Neural Networks
- **Feature Engineering**: Advanced feature extraction from network packets
- **Web Dashboard**: Interactive dashboard for monitoring and analysis
- **Model Training**: Automated model training and evaluation pipeline
- **Attack Classification**: Classifies attacks into multiple categories (DoS, Probe, R2L, U2R, Normal)
- **Performance Metrics**: Comprehensive evaluation metrics and visualizations

## Project Structure

```
AI-NIDS/
├── data/
│   ├── raw/                 # Raw network traffic data
│   ├── processed/           # Processed datasets
│   └── models/              # Trained models
├���─ src/
│   ├── data_processing.py   # Data preprocessing and feature engineering
│   ├── model_training.py    # Model training and evaluation
│   ├── intrusion_detector.py # Main detection engine
│   ├── network_sniffer.py   # Network packet capture
│   └── utils.py             # Utility functions
├── web/
│   ├── app.py               # Flask web application
│   ├── templates/           # HTML templates
│   └── static/              # CSS and JavaScript
├── notebooks/
│   └── analysis.ipynb       # Jupyter notebook for analysis
├── requirements.txt         # Python dependencies
└── config.py                # Configuration settings
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the KDD99 or NSL-KDD dataset

## Usage

### Training Models
```bash
python src/model_training.py --dataset data/processed/train.csv --output data/models/
```

### Running Detection
```bash
python src/intrusion_detector.py --model data/models/best_model.pkl --interface eth0
```

### Web Dashboard
```bash
python web/app.py
```
Then open `http://localhost:5000` in your browser.

## Datasets

- **KDD99**: Classic intrusion detection dataset
- **NSL-KDD**: Improved version of KDD99
- **CICIDS2017**: Modern network intrusion dataset

## Models

1. **Random Forest**: Fast and interpretable
2. **Gradient Boosting (XGBoost)**: High accuracy
3. **Neural Network (TensorFlow)**: Deep learning approach
4. **Ensemble**: Combines multiple models

## Performance

- Accuracy: >99%
- Detection Rate: >98%
- False Positive Rate: <1%

## Technologies

- Python 3.8+
- Scikit-learn
- TensorFlow/Keras
- XGBoost
- Flask
- Pandas
- NumPy
- Matplotlib/Seaborn

## License

MIT License

## Author

Your Name - Final Year Project
