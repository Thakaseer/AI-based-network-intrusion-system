# AI Network Intrusion Detection System - Technical Documentation

## Overview

The AI Network Intrusion Detection System (AI-NIDS) is a comprehensive machine learning-based solution for detecting and classifying network intrusions in real-time. It combines multiple advanced algorithms to achieve high accuracy in threat detection while minimizing false positives.

## System Architecture

### Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Web Dashboard (Flask)                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Home Page | Dashboard | Analytics | Test Detection │   │
│  └────────────────────────────────────────────────���─────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    REST API Layer                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ /api/detect | /api/statistics | /api/alerts | ...   │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              Intrusion Detection Engine                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Single Detector | Ensemble Detector | Batch Mode   │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              ML Models (Trained)                             │
│  ┌────────────────────────────────────────────────────���─┐   │
│  │ Random Forest | XGBoost | Neural Network | SVM       │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              Data Processing Pipeline                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Feature Scaling | Encoding | Normalization           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────��───────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              Data Sources                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Network Packets | CSV Files | API Requests           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Core Modules

### 1. Data Processing (`src/data_processing.py`)

**Purpose**: Load, preprocess, and engineer features from network data

**Key Classes**:
- `DataProcessor`: Main data processing class

**Key Methods**:
- `load_dataset()`: Load datasets in various formats
- `preprocess_data()`: Clean and prepare data
- `create_synthetic_data()`: Generate synthetic network traffic

**Features**:
- Support for KDD99, NSL-KDD, CICIDS2017 datasets
- Categorical feature encoding
- Missing value handling
- Outlier detection and removal
- Feature normalization

### 2. Model Training (`src/model_training.py`)

**Purpose**: Train and evaluate multiple ML models

**Key Classes**:
- `ModelTrainer`: Manages model training and evaluation

**Supported Models**:
1. **Random Forest**
   - Fast training
   - Good interpretability
   - Handles non-linear relationships

2. **XGBoost**
   - High accuracy
   - Gradient boosting
   - Feature importance ranking

3. **Neural Network**
   - Deep learning approach
   - Handles complex patterns
   - Requires more data

4. **SVM**
   - Support Vector Machine
   - Good for binary classification
   - Kernel methods

**Key Methods**:
- `train_random_forest()`: Train RF model
- `train_xgboost()`: Train XGBoost model
- `train_neural_network()`: Train NN model
- `train_svm()`: Train SVM model
- `train_all_models()`: Train all models
- `select_best_model()`: Select best performing model

### 3. Intrusion Detection (`src/intrusion_detector.py`)

**Purpose**: Real-time intrusion detection and classification

**Key Classes**:
- `IntrusionDetector`: Single model detector
- `EnsembleDetector`: Multiple model ensemble

**Key Methods**:
- `detect()`: Detect intrusion in single packet
- `detect_batch()`: Detect intrusions in batch
- `get_detection_statistics()`: Get detection metrics
- `get_recent_alerts()`: Get recent alerts
- `export_results()`: Export results to CSV

**Detection Output**:
```json
{
    "timestamp": "2024-01-15T10:30:45.123456",
    "prediction": 0,
    "prediction_label": "Normal",
    "confidence": 0.95,
    "probabilities": {
        "Normal": 0.95,
        "DoS": 0.03,
        "Probe": 0.01,
        "R2L": 0.01,
        "U2R": 0.00
    },
    "is_attack": false,
    "alert": false
}
```

### 4. Network Sniffer (`src/network_sniffer.py`)

**Purpose**: Capture and parse network packets

**Key Classes**:
- `PacketSniffer`: Network packet capture

**Key Methods**:
- `start_sniffing()`: Start packet capture
- `stop_sniffing()`: Stop packet capture
- `get_packets()`: Get captured packets
- `get_statistics()`: Get packet statistics

**Supported Protocols**:
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)
- ICMP (Internet Control Message Protocol)

### 5. Utilities (`src/utils.py`)

**Purpose**: Common utility functions

**Key Functions**:
- `setup_logging()`: Configure logging
- `save_model()`: Save trained model
- `load_model()`: Load trained model
- `scale_features()`: Scale features
- `evaluate_model()`: Evaluate model performance
- `plot_confusion_matrix()`: Visualize confusion matrix
- `plot_feature_importance()`: Visualize feature importance

## Machine Learning Pipeline

### Training Pipeline

```
1. Data Loading
   ↓
2. Data Preprocessing
   - Handle missing values
   - Encode categorical features
   - Remove outliers
   ↓
3. Feature Scaling
   - StandardScaler or MinMaxScaler
   ↓
4. Train-Test Split
   - 80% training, 20% testing
   ↓
5. Model Training
   - Train multiple models
   - Hyperparameter tuning
   ↓
6. Model Evaluation
   - Accuracy, Precision, Recall, F1-Score
   - Confusion Matrix
   - ROC Curve
   ↓
7. Model Selection
   - Select best model based on F1-Score
   ↓
8. Model Persistence
   - Save trained models
   - Save scalers
```

### Detection Pipeline

```
1. Packet Reception
   ↓
2. Feature Extraction
   - Extract network features
   ↓
3. Feature Preprocessing
   - Apply same transformations as training
   ↓
4. Feature Scaling
   - Scale using saved scaler
   ↓
5. Model Prediction
   - Get prediction and confidence
   ↓
6. Post-Processing
   - Apply thresholds
   - Generate alerts
   ↓
7. Result Output
   - Return detection result
   - Store in history
```

## Attack Types

The system detects and classifies the following attack types:

### 1. DoS (Denial of Service)
- **Description**: Attacks that overwhelm network resources
- **Examples**: SYN flood, UDP flood, ICMP flood
- **Characteristics**: High packet rate, resource exhaustion

### 2. Probe
- **Description**: Reconnaissance and scanning activities
- **Examples**: Port scanning, network mapping
- **Characteristics**: Multiple connection attempts, varied ports

### 3. R2L (Remote to Local)
- **Description**: Unauthorized remote access attempts
- **Examples**: SSH brute force, FTP attacks
- **Characteristics**: Failed login attempts, unusual protocols

### 4. U2R (User to Root)
- **Description**: Privilege escalation attacks
- **Examples**: Buffer overflow, privilege escalation exploits
- **Characteristics**: Unusual system calls, root access attempts

### 5. Normal
- **Description**: Legitimate network traffic
- **Characteristics**: Normal traffic patterns, expected protocols

## Network Features

The system analyzes 41 network features:

### Basic Features
- `duration`: Connection duration
- `protocol_type`: Protocol (TCP, UDP, ICMP)
- `service`: Network service
- `flag`: Connection flag
- `src_bytes`: Source bytes
- `dst_bytes`: Destination bytes

### Content Features
- `land`: Same source and destination
- `wrong_fragment`: Wrong fragments
- `urgent`: Urgent packets
- `hot`: Hot indicators

### Traffic Features
- `count`: Number of connections
- `srv_count`: Service connections
- `serror_rate`: SYN error rate
- `srv_serror_rate`: Service SYN error rate

### Host-based Features
- `dst_host_count`: Destination host connections
- `dst_host_srv_count`: Destination service connections
- `dst_host_same_srv_rate`: Same service rate
- `dst_host_diff_srv_rate`: Different service rate

## Web Application

### Frontend

**Technologies**:
- HTML5
- CSS3
- JavaScript (Vanilla)
- Chart.js for visualizations

**Pages**:
1. **Home Page** (`index.html`)
   - Project overview
   - Feature highlights
   - Quick test button

2. **Dashboard** (`dashboard.html`)
   - Real-time statistics
   - Attack distribution chart
   - Confidence analysis
   - Recent alerts
   - Manual testing interface

### Backend

**Framework**: Flask

**API Endpoints**:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/dashboard` | Dashboard page |
| POST | `/api/detect` | Single packet detection |
| POST | `/api/detect-batch` | Batch detection |
| GET | `/api/statistics` | Detection statistics |
| GET | `/api/alerts` | Recent alerts |
| GET | `/api/export` | Export results |
| POST | `/api/clear-history` | Clear history |
| POST | `/api/train` | Train new model |
| GET | `/api/model-info` | Model information |
| GET | `/api/health` | Health check |

## Configuration

### Key Configuration Parameters

```python
# Dataset
DATASET_NAME = 'NSL-KDD'
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.1

# Feature Processing
FEATURE_SCALING = 'StandardScaler'
HANDLE_MISSING = 'mean'
REMOVE_OUTLIERS = True

# Models
MODELS_TO_TRAIN = ['RandomForest', 'XGBoost', 'NeuralNetwork', 'SVM']

# Detection
DETECTION_THRESHOLD = 0.5
ALERT_THRESHOLD = 0.8

# Web
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
```

## Performance Metrics

### Evaluation Metrics

1. **Accuracy**: (TP + TN) / (TP + TN + FP + FN)
2. **Precision**: TP / (TP + FP)
3. **Recall**: TP / (TP + FN)
4. **F1-Score**: 2 * (Precision * Recall) / (Precision + Recall)
5. **ROC-AUC**: Area under ROC curve

### Expected Performance

- **Accuracy**: >99%
- **Precision**: >98%
- **Recall**: >98%
- **F1-Score**: >98%
- **Detection Rate**: >98%
- **False Positive Rate**: <1%

## Usage Examples

### Training Models

```bash
# Train with synthetic data
python train.py

# Train with custom dataset
python train.py --dataset data/raw/kdd99.csv --output data/models
```

### Running Detection

```bash
# Demo mode
python detect.py --mode demo

# Web API
python detect.py --mode api

# Packet sniffer
sudo python detect.py --mode sniffer --interface eth0
```

### Python API

```python
from src.intrusion_detector import create_detector
from src.data_processing import DataProcessor

# Create detector
detector = create_detector()

# Detect packet
packet = {...}
result = detector.detect(packet)

# Get statistics
stats = detector.get_detection_statistics()
```

## Deployment

### Local Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Train models
python train.py

# Run web server
python detect.py --mode api
```

### Docker Deployment

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "detect.py", "--mode", "api"]
```

### Cloud Deployment

- **AWS**: Deploy on EC2 or Lambda
- **Azure**: Deploy on App Service
- **Google Cloud**: Deploy on Cloud Run

## Security Considerations

1. **Model Security**: Encrypt trained models
2. **Data Privacy**: Handle network data responsibly
3. **Access Control**: Implement authentication
4. **Logging**: Monitor all activities
5. **Updates**: Regularly retrain models

## Future Enhancements

1. **Real-time Learning**: Online learning capabilities
2. **Distributed Detection**: Multi-node deployment
3. **Advanced Visualization**: 3D network graphs
4. **Mobile App**: Mobile dashboard
5. **IoT Integration**: Support for IoT devices
6. **Blockchain**: Immutable alert logging

## References

- KDD99 Dataset: http://kdd.ics.uci.edu/
- NSL-KDD Dataset: https://www.unb.ca/cic/
- Scikit-learn Documentation: https://scikit-learn.org/
- TensorFlow Documentation: https://www.tensorflow.org/
- XGBoost Documentation: https://xgboost.readthedocs.io/

## License

MIT License

## Support

For issues or questions, refer to SETUP.md or contact the development team.

---

**Version**: 1.0.0
**Last Updated**: 2024
**Status**: Active Development
