# AI Network Intrusion Detection System - Setup Guide

## Quick Start

### 1. Installation

```bash
# Clone or navigate to the project directory
cd AI-NIDS

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Training Models

```bash
# Train with synthetic data (default)
python train.py

# Train with custom dataset
python train.py --dataset path/to/dataset.csv --output data/models

# View training options
python train.py --help
```

### 3. Running Detection

#### Demo Mode (Recommended for Testing)
```bash
python detect.py --mode demo
```

#### Web API Server
```bash
python detect.py --mode api
# Then open http://localhost:5000 in your browser
```

#### Packet Sniffer (Requires Admin Privileges)
```bash
# Windows (Run as Administrator)
python detect.py --mode sniffer --interface eth0 --count 100

# Linux/Mac
sudo python detect.py --mode sniffer --interface eth0 --count 100
```

## Project Structure

```
AI-NIDS/
├── config.py                    # Configuration settings
├── train.py                     # Training script
├── detect.py                    # Detection script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── SETUP.md                     # This file
│
├── src/                         # Source code
│   ├── __init__.py
│   ├── utils.py                 # Utility functions
│   ├── data_processing.py       # Data preprocessing
│   ├── model_training.py        # Model training
│   ├── intrusion_detector.py    # Detection engine
│   └── network_sniffer.py       # Packet capture
│
├── web/                         # Web application
│   ├── app.py                   # Flask application
│   ├── templates/
│   │   ├── index.html           # Home page
│   │   └── dashboard.html       # Dashboard
│   └── static/
│       ├── style.css            # Styling
│       ├── script.js            # Home page script
│       └── dashboard.js         # Dashboard script
│
├── data/                        # Data directory
│   ├── raw/                     # Raw datasets
│   ├── processed/               # Processed data
│   └── models/                  # Trained models
│
└── logs/                        # Log files
```

## Configuration

Edit `config.py` to customize:

- **Dataset**: Change `DATASET_NAME` to 'KDD99', 'NSL-KDD', or 'CICIDS2017'
- **Models**: Modify `MODELS_TO_TRAIN` to select which models to train
- **Thresholds**: Adjust `DETECTION_THRESHOLD` and `ALERT_THRESHOLD`
- **Network**: Set `NETWORK_INTERFACE` for packet capture
- **Web**: Configure `FLASK_HOST` and `FLASK_PORT`

## Datasets

### Supported Datasets

1. **KDD99** - Classic intrusion detection dataset
   - Download: http://kdd.ics.uci.edu/databases/kddcup99/

2. **NSL-KDD** - Improved version of KDD99
   - Download: https://www.unb.ca/cic/datasets/nsl-kdd.html

3. **CICIDS2017** - Modern network intrusion dataset
   - Download: https://www.unb.ca/cic/datasets/ids-2017.html

### Dataset Format

Datasets should be in CSV format with the following columns:
- Network features (duration, protocol_type, service, etc.)
- Label column (attack type or 'Normal')

## Models

### Trained Models

The system trains and evaluates multiple models:

1. **Random Forest** - Fast, interpretable
2. **XGBoost** - High accuracy, gradient boosting
3. **Neural Network** - Deep learning approach
4. **SVM** - Support Vector Machine

### Model Selection

The best model is automatically selected based on F1-score and saved as `best_model_*.pkl`

## Web Dashboard

### Features

- **Real-time Statistics**: Total packets, attacks, detection rate
- **Attack Distribution**: Pie chart of attack types
- **Confidence Analysis**: Distribution of detection confidence
- **Recent Alerts**: Latest detected threats
- **Test Detection**: Manual packet testing
- **Export Results**: Download detection results as CSV

### API Endpoints

- `GET /` - Home page
- `GET /dashboard` - Dashboard
- `POST /api/detect` - Single packet detection
- `POST /api/detect-batch` - Batch detection
- `GET /api/statistics` - Detection statistics
- `GET /api/alerts` - Recent alerts
- `GET /api/export` - Export results
- `POST /api/clear-history` - Clear history
- `GET /api/health` - Health check

## Performance Metrics

### Expected Performance

- **Accuracy**: >99%
- **Precision**: >98%
- **Recall**: >98%
- **F1-Score**: >98%
- **Detection Rate**: >98%
- **False Positive Rate**: <1%

### Evaluation Metrics

The system provides:
- Confusion Matrix
- Classification Report
- ROC Curve
- Feature Importance
- Cross-validation Scores

## Troubleshooting

### Issue: "No module named 'tensorflow'"
**Solution**: Install TensorFlow
```bash
pip install tensorflow
```

### Issue: "Administrator privileges required"
**Solution**: Run packet sniffer with admin/sudo privileges
```bash
# Windows: Run Command Prompt as Administrator
# Linux/Mac: Use sudo
sudo python detect.py --mode sniffer
```

### Issue: "Port 5000 already in use"
**Solution**: Change port in config.py or use different port
```bash
python detect.py --mode api --port 5001
```

### Issue: "Model not found"
**Solution**: Train models first
```bash
python train.py
```

## Advanced Usage

### Custom Model Training

```python
from src.model_training import ModelTrainer
from src.data_processing import DataProcessor

# Load and preprocess data
processor = DataProcessor()
df = processor.load_dataset('path/to/dataset.csv')
X, y = processor.preprocess_data(df)

# Train models
trainer = ModelTrainer()
trainer.train_all_models(X_train, y_train, X_test, y_test)
trainer.save_best_model()
```

### Custom Detection

```python
from src.intrusion_detector import create_detector

# Create detector
detector = create_detector()

# Detect single packet
result = detector.detect(packet_data)

# Detect batch
results = detector.detect_batch(packets_list)

# Get statistics
stats = detector.get_detection_statistics()
```

### Ensemble Detection

```python
from src.intrusion_detector import EnsembleDetector

# Create ensemble
ensemble = EnsembleDetector()
ensemble.add_detector('model1', detector1, weight=0.5)
ensemble.add_detector('model2', detector2, weight=0.5)

# Detect with ensemble
result = ensemble.detect(packet_data)
```

## Performance Optimization

### For Better Accuracy

1. Use larger datasets
2. Tune hyperparameters in config.py
3. Use ensemble methods
4. Implement feature engineering

### For Better Speed

1. Use Random Forest instead of Neural Network
2. Reduce number of features
3. Use batch processing
4. Implement caching

## Security Considerations

1. **Model Protection**: Keep trained models secure
2. **Data Privacy**: Handle network data responsibly
3. **Access Control**: Restrict API access
4. **Logging**: Monitor all detection activities
5. **Updates**: Regularly retrain models with new data

## Contributing

To contribute improvements:

1. Create a new branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code documentation
3. Check project issues on GitHub

## References

- KDD99 Dataset: http://kdd.ics.uci.edu/
- NSL-KDD Dataset: https://www.unb.ca/cic/
- Scikit-learn: https://scikit-learn.org/
- TensorFlow: https://www.tensorflow.org/
- XGBoost: https://xgboost.readthedocs.io/

## Version History

### v1.0.0 (Current)
- Initial release
- Support for multiple ML models
- Web dashboard
- Real-time detection
- Batch processing
- Comprehensive evaluation metrics

---

**Last Updated**: 2024
**Author**: Your Name
**Status**: Active Development
