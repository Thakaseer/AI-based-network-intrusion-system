# AI Network Intrusion Detection System - Testing Guide

## Testing Overview

This guide provides comprehensive testing procedures for the AI-NIDS system.

## Unit Testing

### Testing Data Processing

```python
# test_data_processing.py
import unittest
from src.data_processing import DataProcessor

class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = DataProcessor()
    
    def test_synthetic_data_creation(self):
        """Test synthetic data generation"""
        df = self.processor.create_synthetic_data(n_samples=100)
        self.assertEqual(len(df), 100)
        self.assertIn('label', df.columns)
    
    def test_data_preprocessing(self):
        """Test data preprocessing"""
        df = self.processor.create_synthetic_data(n_samples=100)
        X, y = self.processor.preprocess_data(df)
        self.assertEqual(len(X), len(y))
        self.assertGreater(len(X.columns), 0)
    
    def test_feature_names(self):
        """Test feature name extraction"""
        df = self.processor.create_synthetic_data(n_samples=100)
        X, y = self.processor.preprocess_data(df)
        features = self.processor.get_feature_names()
        self.assertIsNotNone(features)
        self.assertEqual(len(features), len(X.columns))

if __name__ == '__main__':
    unittest.main()
```

### Testing Model Training

```python
# test_model_training.py
import unittest
from src.model_training import ModelTrainer
from src.data_processing import DataProcessor
from sklearn.model_selection import train_test_split
import config

class TestModelTrainer(unittest.TestCase):
    
    def setUp(self):
        self.processor = DataProcessor()
        self.trainer = ModelTrainer()
        
        # Create synthetic data
        df = self.processor.create_synthetic_data(n_samples=500)
        X, y = self.processor.preprocess_data(df)
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
    
    def test_random_forest_training(self):
        """Test Random Forest training"""
        model, metrics = self.trainer.train_random_forest(
            self.X_train, self.y_train, self.X_test, self.y_test
        )
        self.assertIsNotNone(model)
        self.assertGreater(metrics['accuracy'], 0.5)
    
    def test_xgboost_training(self):
        """Test XGBoost training"""
        model, metrics = self.trainer.train_xgboost(
            self.X_train, self.y_train, self.X_test, self.y_test
        )
        self.assertIsNotNone(model)
        self.assertGreater(metrics['accuracy'], 0.5)
    
    def test_model_selection(self):
        """Test best model selection"""
        self.trainer.train_all_models(
            self.X_train, self.y_train, self.X_test, self.y_test
        )
        self.assertIsNotNone(self.trainer.best_model)
        self.assertIsNotNone(self.trainer.best_model_name)

if __name__ == '__main__':
    unittest.main()
```

### Testing Intrusion Detection

```python
# test_intrusion_detector.py
import unittest
from src.intrusion_detector import IntrusionDetector, create_detector
import config

class TestIntrusionDetector(unittest.TestCase):
    
    def setUp(self):
        self.detector = create_detector()
    
    def test_detector_initialization(self):
        """Test detector initialization"""
        self.assertIsNotNone(self.detector)
        self.assertIsNotNone(self.detector.model)
    
    def test_single_detection(self):
        """Test single packet detection"""
        packet = {
            'duration': 100,
            'protocol_type': 0,
            'service': 5,
            'flag': 2,
            'src_bytes': 1000,
            'dst_bytes': 2000,
            # ... other features
        }
        result = self.detector.detect(packet)
        self.assertIsNotNone(result)
        self.assertIn('prediction', result)
        self.assertIn('confidence', result)
    
    def test_batch_detection(self):
        """Test batch detection"""
        packets = [
            {'duration': 100, 'protocol_type': 0, ...},
            {'duration': 200, 'protocol_type': 1, ...},
        ]
        results = self.detector.detect_batch(packets)
        self.assertEqual(len(results), len(packets))
    
    def test_statistics(self):
        """Test statistics calculation"""
        # Run some detections
        packet = {'duration': 100, 'protocol_type': 0, ...}
        self.detector.detect(packet)
        
        stats = self.detector.get_detection_statistics()
        self.assertIsNotNone(stats)
        self.assertIn('total_packets', stats)
        self.assertIn('detection_rate', stats)

if __name__ == '__main__':
    unittest.main()
```

## Integration Testing

### Testing Complete Pipeline

```python
# test_integration.py
import unittest
from src.model_training import train_pipeline
from src.intrusion_detector import create_detector
from src.data_processing import DataProcessor
import os
import config

class TestIntegration(unittest.TestCase):
    
    def test_complete_training_pipeline(self):
        """Test complete training pipeline"""
        # Train models
        trainer, processor, scaler = train_pipeline()
        
        # Verify models are trained
        self.assertGreater(len(trainer.models), 0)
        self.assertIsNotNone(trainer.best_model)
        self.assertIsNotNone(scaler)
    
    def test_detection_after_training(self):
        """Test detection after training"""
        # Train models
        train_pipeline()
        
        # Create detector
        detector = create_detector()
        
        # Test detection
        packet = {'duration': 100, 'protocol_type': 0, ...}
        result = detector.detect(packet)
        
        self.assertIsNotNone(result)
        self.assertIn('prediction_label', result)

if __name__ == '__main__':
    unittest.main()
```

## Performance Testing

### Testing Model Performance

```python
# test_performance.py
import time
import unittest
from src.intrusion_detector import create_detector
from src.data_processing import DataProcessor

class TestPerformance(unittest.TestCase):
    
    def setUp(self):
        self.detector = create_detector()
        self.processor = DataProcessor()
    
    def test_detection_speed(self):
        """Test detection speed"""
        packet = {'duration': 100, 'protocol_type': 0, ...}
        
        start_time = time.time()
        for _ in range(100):
            self.detector.detect(packet)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / 100
        print(f"Average detection time: {avg_time*1000:.2f}ms")
        
        # Should be less than 10ms per detection
        self.assertLess(avg_time, 0.01)
    
    def test_batch_processing_speed(self):
        """Test batch processing speed"""
        packets = [{'duration': 100, 'protocol_type': 0, ...} for _ in range(100)]
        
        start_time = time.time()
        self.detector.detect_batch(packets)
        end_time = time.time()
        
        total_time = end_time - start_time
        print(f"Batch processing time: {total_time:.2f}s for 100 packets")
        
        # Should process 100 packets in less than 2 seconds
        self.assertLess(total_time, 2.0)
    
    def test_memory_usage(self):
        """Test memory usage"""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        
        # Get initial memory
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Run detections
        packet = {'duration': 100, 'protocol_type': 0, ...}
        for _ in range(1000):
            self.detector.detect(packet)
        
        # Get final memory
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        memory_increase = final_memory - initial_memory
        print(f"Memory increase: {memory_increase:.2f}MB")
        
        # Should not increase more than 100MB
        self.assertLess(memory_increase, 100)

if __name__ == '__main__':
    unittest.main()
```

## API Testing

### Testing Flask API

```python
# test_api.py
import unittest
import json
from web.app import app

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        """Test home page"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_page(self):
        """Test dashboard page"""
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
    
    def test_detect_api(self):
        """Test detection API"""
        packet = {
            'duration': 100,
            'protocol_type': 0,
            'service': 5,
            # ... other features
        }
        
        response = self.app.post(
            '/api/detect',
            data=json.dumps(packet),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('prediction', data)
    
    def test_statistics_api(self):
        """Test statistics API"""
        response = self.app.get('/api/statistics')
        self.assertIn(response.status_code, [200, 404])
    
    def test_health_check(self):
        """Test health check"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
    unittest.main()
```

## Manual Testing Checklist

### Data Processing
- [ ] Load KDD99 dataset
- [ ] Load NSL-KDD dataset
- [ ] Load CICIDS2017 dataset
- [ ] Preprocess data correctly
- [ ] Handle missing values
- [ ] Remove outliers
- [ ] Encode categorical features
- [ ] Scale features

### Model Training
- [ ] Train Random Forest
- [ ] Train XGBoost
- [ ] Train Neural Network
- [ ] Train SVM
- [ ] Select best model
- [ ] Save models
- [ ] Load models
- [ ] Evaluate models

### Detection
- [ ] Detect normal traffic
- [ ] Detect DoS attacks
- [ ] Detect Probe attacks
- [ ] Detect R2L attacks
- [ ] Detect U2R attacks
- [ ] Batch detection
- [ ] Get statistics
- [ ] Get alerts

### Web Interface
- [ ] Home page loads
- [ ] Dashboard loads
- [ ] Statistics display
- [ ] Charts render
- [ ] Test detection works
- [ ] Export results
- [ ] Clear history
- [ ] Refresh data

### API Endpoints
- [ ] GET / (home)
- [ ] GET /dashboard
- [ ] POST /api/detect
- [ ] POST /api/detect-batch
- [ ] GET /api/statistics
- [ ] GET /api/alerts
- [ ] GET /api/export
- [ ] POST /api/clear-history
- [ ] GET /api/health

## Running Tests

### Run All Tests
```bash
python -m pytest tests/
```

### Run Specific Test
```bash
python -m pytest tests/test_data_processing.py
```

### Run with Coverage
```bash
python -m pytest --cov=src tests/
```

### Run Performance Tests
```bash
python -m pytest tests/test_performance.py -v
```

## Test Results

### Expected Results

| Test | Expected Result |
|------|-----------------|
| Data Loading | ✓ Pass |
| Data Preprocessing | ✓ Pass |
| Model Training | ✓ Pass |
| Model Evaluation | ✓ Pass |
| Single Detection | ✓ Pass |
| Batch Detection | ✓ Pass |
| API Endpoints | ✓ Pass |
| Web Interface | ✓ Pass |
| Performance | ✓ Pass |

## Continuous Integration

### GitHub Actions Example

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    - name: Run tests
      run: |
        pytest tests/ --cov=src
```

## Debugging

### Enable Debug Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Print Debug Information
```python
import pdb
pdb.set_trace()  # Breakpoint
```

### Check Model Predictions
```python
from src.intrusion_detector import create_detector
detector = create_detector()
result = detector.detect(packet)
print(result)
```

## Test Coverage Goals

- **Overall Coverage**: >80%
- **Core Modules**: >90%
- **Utils**: >85%
- **API**: >80%

---

**Testing is crucial for reliability and performance!**
