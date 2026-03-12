"""
Configuration settings for AI Network Intrusion Detection System
"""

import os

# Project paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
MODELS_DIR = os.path.join(DATA_DIR, 'models')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Dataset configuration
DATASET_NAME = 'NSL-KDD'  # Options: 'KDD99', 'NSL-KDD', 'CICIDS2017'
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.1
RANDOM_STATE = 42

# Feature configuration
FEATURE_SCALING = 'StandardScaler'  # Options: 'StandardScaler', 'MinMaxScaler'
HANDLE_MISSING = 'mean'  # Options: 'mean', 'median', 'drop'
REMOVE_OUTLIERS = True
OUTLIER_METHOD = 'IQR'  # Options: 'IQR', 'ZScore'
OUTLIER_REMOVAL_MAX_ROWS = 10000  # Skip outlier removal for datasets larger than this to improve speed

# Model configuration
MODELS_TO_TRAIN = ['RandomForest', 'XGBoost', 'NeuralNetwork', 'SVM']
RANDOM_FOREST_PARAMS = {
    'n_estimators': 100,
    'max_depth': 20,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': RANDOM_STATE,
    'n_jobs': -1
}

XGBOOST_PARAMS = {
    'n_estimators': 100,
    'max_depth': 7,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'random_state': RANDOM_STATE,
    'n_jobs': -1
}

NEURAL_NETWORK_PARAMS = {
    'hidden_layers': [128, 64, 32],
    'activation': 'relu',
    'output_activation': 'softmax',
    'epochs': 20,  # Reduced from 50 for faster training
    'batch_size': 32,
    'validation_split': 0.2,
    'dropout_rate': 0.3
}

SVM_PARAMS = {
    'kernel': 'rbf',
    'C': 1.0,
    'gamma': 'scale',
    'random_state': RANDOM_STATE
}

# Attack types
ATTACK_TYPES = {
    'Normal': 0,
    'DoS': 1,
    'Probe': 2,
    'R2L': 3,
    'U2R': 4
}

ATTACK_NAMES = {v: k for k, v in ATTACK_TYPES.items()}

# Network configuration
NETWORK_INTERFACE = 'eth0'  # Change based on your system
PACKET_COUNT = 0  # 0 = infinite
PACKET_TIMEOUT = 30  # seconds

# Web application configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True
SECRET_KEY = 'your-secret-key-change-in-production'

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Performance thresholds
DETECTION_THRESHOLD = 0.5
ALERT_THRESHOLD = 0.8

# Batch processing
BATCH_SIZE = 1000
BUFFER_SIZE = 10000
