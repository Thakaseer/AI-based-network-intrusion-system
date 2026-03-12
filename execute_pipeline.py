#!/usr/bin/env python3
"""
Complete Execution Pipeline for AI-NIDS
Executes: Data Load → Process → Train → Test → Web Display
"""

import os
import sys
import json
import time
import glob
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from sklearn.model_selection import train_test_split

# Add paths
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from src.data_processing import DataProcessor
from src.model_training import ModelTrainer
from src.intrusion_detector import create_detector
from src.utils import setup_logging

logger = setup_logging(__name__, 'pipeline_execution.log')

class ExecutionPipeline:
    """Complete execution pipeline"""
    
    def __init__(self, dataset_path=None):
        self.start_time = datetime.now()
        self.dataset_path = dataset_path
        self.results = {
            'phase': {},
            'summary': {}
        }
        self.processor = None
        self.trainer = None
        self.detector = None
        
    def log_phase(self, phase_name, status, details=""):
        """Log phase execution"""
        timestamp = datetime.now().isoformat()
        self.results['phase'][phase_name] = {
            'status': status,
            'timestamp': timestamp,
            'details': details
        }
        print(f"\n{'='*80}")
        print(f"[{status.upper()}] {phase_name}")
        print(f"{'='*80}")
        if details:
            print(details)
        logger.info(f"{phase_name}: {status}")
    
    # =====================================================================
    # PHASE 1: DATA LOADING
    # =====================================================================
    
    def phase_1_load_data(self):
        """Phase 1: Load dataset"""
        self.log_phase("PHASE 1: DATA LOADING", "started")
        
        try:
            self.processor = DataProcessor()
            
            # Determine which dataset to load
            dataset_path = None
            
            # First priority: explicit dataset_path parameter
            if self.dataset_path:
                dataset_path = self.dataset_path
                print(f"📂 Using provided dataset path: {dataset_path}")
            else:
                # Second priority: look for CSV in raw data directory
                import glob
                csv_files = glob.glob(os.path.join(config.RAW_DATA_DIR, '*.csv'))
                if csv_files:
                    dataset_path = csv_files[0]
                    print(f"📂 Found dataset in raw directory: {dataset_path}")
            
            # Load the dataset
            if dataset_path:
                print(f"📂 Loading dataset from: {dataset_path}")
                # For dashboard testing, limit to 10000 rows for speed
                # Full processing uses all data
                max_rows = 10000 if 'KDD' in dataset_path else None
                if max_rows:
                    print(f"⚡ Using first {max_rows} rows for faster processing")
                df = self.processor.load_dataset(dataset_path, nrows=max_rows)
                print(f"✓ Dataset loaded successfully: {len(df)} records")
            else:
                print(f"⚠️  No dataset found")
                print(f"📊 Creating synthetic dataset...")
                df = self.processor.create_synthetic_data(n_samples=5000)
                print(f"✓ Synthetic dataset created: {len(df)} samples")
            
            details = f"Dataset: {len(df)} rows × {len(df.columns)} columns\n"
            details += f"Attack distribution:\n"
            if 'label' in df.columns:
                attack_counts = df['label'].value_counts()
                for attack, count in attack_counts.items():
                    pct = (count / len(df)) * 100
                    details += f"  {attack}: {count} ({pct:.1f}%)\n"
            
            self.log_phase("PHASE 1: DATA LOADING", "completed", details)
            self.results['data'] = df
            return df
            
        except Exception as e:
            self.log_phase("PHASE 1: DATA LOADING", "FAILED", str(e))
            raise
    
    # =====================================================================
    # PHASE 2: DATA PROCESSING
    # =====================================================================
    
    def phase_2_process_data(self, df):
        """Phase 2: Preprocess and split data"""
        self.log_phase("PHASE 2: DATA PROCESSING", "started")
        
        try:
            print("🔄 Preprocessing data...")
            X, y = self.processor.preprocess_data(df)
            print(f"✓ Preprocessing complete: X={X.shape}, y={y.shape}")
            
            print("📊 Splitting into train/val/test...")
            # First split: 80% train+val, 20% test
            X_temp, X_test, y_temp, y_test = train_test_split(
                X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE, stratify=y
            )
            
            # Second split: split temp into train (80%) and val (20%)
            val_ratio = config.VALIDATION_SIZE / (1 - config.TEST_SIZE)
            X_train, X_val, y_train, y_val = train_test_split(
                X_temp, y_temp, test_size=val_ratio, random_state=config.RANDOM_STATE, stratify=y_temp
            )
            
            details = f"Training set:   {X_train.shape[0]:,} samples\n"
            details += f"Validation set: {X_val.shape[0]:,} samples\n"
            details += f"Test set:       {X_test.shape[0]:,} samples\n"
            details += f"Features:       {X_train.shape[1]}"
            
            self.log_phase("PHASE 2: DATA PROCESSING", "completed", details)
            
            self.results['processed_data'] = {
                'X_train': X_train, 'X_val': X_val, 'X_test': X_test,
                'y_train': y_train, 'y_val': y_val, 'y_test': y_test
            }
            return self.results['processed_data']
            
        except Exception as e:
            self.log_phase("PHASE 2: DATA PROCESSING", "FAILED", str(e))
            raise
    
    # =====================================================================
    # PHASE 3: MODEL TRAINING
    # =====================================================================
    
    def phase_3_train_models(self, data):
        """Phase 3: Train ML models"""
        self.log_phase("PHASE 3: MODEL TRAINING", "started")
        
        try:
            print("🤖 Initializing model trainer...")
            self.trainer = ModelTrainer()
            
            print("📚 Training models on training data...")
            # Combine train and val for training
            X_train_combined = pd.concat([data['X_train'], data['X_val']], axis=0)
            y_train_combined = np.concatenate([data['y_train'], data['y_val']])
            
            self.trainer.train_all_models(
                X_train_combined, y_train_combined,
                data['X_test'], data['y_test']
            )
            
            print(f"✓ Models trained successfully")
            
            # Save models
            print("💾 Saving models...")
            self.trainer.save_all_models(config.MODELS_DIR)
            self.trainer.save_best_model(config.MODELS_DIR)
            if hasattr(self.trainer, 'save_scaler'):
                self.trainer.save_scaler(config.MODELS_DIR)
            print(f"✓ Models saved to {config.MODELS_DIR}")
            
            details = f"Best Model: {self.trainer.best_model_name}\n"
            details += f"Models trained: {len(self.trainer.models)}\n"
            details += f"Saved to: {config.MODELS_DIR}"
            
            self.log_phase("PHASE 3: MODEL TRAINING", "completed", details)
            
            self.results['training'] = {
                'best_model': self.trainer.best_model_name,
                'models_count': len(self.trainer.models),
                'results': self.trainer.results if hasattr(self.trainer, 'results') else {}
            }
            return self.trainer
            
        except Exception as e:
            self.log_phase("PHASE 3: MODEL TRAINING", "FAILED", str(e))
            raise
    
    # =====================================================================
    # PHASE 4: MODEL TESTING
    # =====================================================================
    
    def phase_4_test_models(self, data):
        """Phase 4: Test models on test dataset"""
        self.log_phase("PHASE 4: MODEL TESTING", "started")
        
        try:
            print("🔧 Loading detector with trained model...")
            self.detector = create_detector()
            
            if self.detector.model is None:
                raise Exception("Model failed to load")
            
            print(f"✓ Detector loaded successfully")
            
            print("🧪 Testing on test dataset...")
            test_results = []
            predictions = []
            confidences = []
            
            # Test on subset of test data
            test_size = min(len(data['X_test']), 100)
            
            for i in range(test_size):
                # Convert row to dict
                if isinstance(data['X_test'], pd.DataFrame):
                    row_dict = data['X_test'].iloc[i].to_dict()
                else:
                    # numpy array
                    row_dict = {f'feature_{j}': data['X_test'][i, j] for j in range(data['X_test'].shape[1])}
                
                result = self.detector.detect(row_dict)
                
                if result:
                    test_results.append(result)
                    predictions.append(result['prediction'])
                    confidences.append(result['confidence'])
            
            # Calculate metrics
            if test_results:
                correct = sum(1 for i, r in enumerate(test_results) 
                             if r['prediction'] == data['y_test'][i])
                accuracy = correct / len(test_results)
                avg_confidence = np.mean(confidences)
            else:
                accuracy = 0
                avg_confidence = 0
                correct = 0
            
            details = f"Tests run:      {len(test_results)}\n"
            details += f"Correct:        {correct}/{len(test_results)}\n"
            details += f"Accuracy:       {accuracy*100:.2f}%\n"
            details += f"Avg Confidence: {avg_confidence*100:.2f}%"
            
            self.log_phase("PHASE 4: MODEL TESTING", "completed", details)
            
            diverse_results = []
            seen = set()
            for r in test_results:
                if r['prediction_label'] not in seen:
                    diverse_results.append(r)
                    seen.add(r['prediction_label'])
            for r in test_results:
                if len(diverse_results) >= 10:
                    break
                if r not in diverse_results:
                    diverse_results.append(r)

            self.results['testing'] = {
                'total_tests': len(test_results),
                'correct_predictions': correct,
                'accuracy': accuracy,
                'avg_confidence': avg_confidence,
                'sample_results': diverse_results[:10]
            }
            return test_results
            
        except Exception as e:
            self.log_phase("PHASE 4: MODEL TESTING", "FAILED", str(e))
            raise
    
    # =====================================================================
    # PHASE 5: GENERATE STATISTICS
    # =====================================================================
    
    def phase_5_get_statistics(self):
        """Phase 5: Generate and collect statistics"""
        self.log_phase("PHASE 5: STATISTICS GENERATION", "started")
        
        try:
            print("📊 Calculating statistics...")
            stats = self.detector.get_detection_statistics()
            
            details = f"Total packets:    {stats.get('total_packets', 0)}\n"
            details += f"Total attacks:    {stats.get('total_attacks', 0)}\n"
            details += f"Detection rate:   {stats.get('detection_rate', 0)*100:.2f}%\n"
            details += f"Alert rate:       {stats.get('alert_rate', 0)*100:.2f}%\n"
            details += f"Avg confidence:   {stats.get('average_confidence', 0)*100:.2f}%"
            
            self.log_phase("PHASE 5: STATISTICS GENERATION", "completed", details)
            
            self.results['statistics'] = stats
            return stats
            
        except Exception as e:
            self.log_phase("PHASE 5: STATISTICS GENERATION", "WARNING", str(e))
            # Don't fail on statistics
            self.results['statistics'] = {}
            return {}
    
    # =====================================================================
    # PHASE 6: SAVE RESULTS
    # =====================================================================
    
    def phase_6_save_results(self):
        """Phase 6: Save execution results"""
        self.log_phase("PHASE 6: RESULTS SAVING", "started")
        
        try:
            # Create results file
            os.makedirs('logs', exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            results_file = f'logs/execution_results_{timestamp}.json'
            
            # Prepare data for JSON serialization
            json_results = {
                'timestamp': datetime.now().isoformat(),
                'duration': str(datetime.now() - self.start_time),
                'phases': self.results['phase'],
                'training': self.results.get('training', {}),
                'testing': {
                    k: v for k, v in self.results.get('testing', {}).items()
                    if k != 'sample_results'
                },
                'statistics': self.results.get('statistics', {})
            }
            
            with open(results_file, 'w') as f:
                json.dump(json_results, f, indent=2, default=lambda x: x.item() if hasattr(x, 'item') else str(x))
            
            details = f"Results saved to: {results_file}\n"
            details += f"Total execution time: {datetime.now() - self.start_time}"
            
            self.log_phase("PHASE 6: RESULTS SAVING", "completed", details)
            
            return results_file
            
        except Exception as e:
            self.log_phase("PHASE 6: RESULTS SAVING", "WARNING", str(e))
            return None
    
    # =====================================================================
    # EXECUTE COMPLETE PIPELINE
    # =====================================================================
    
    def execute(self):
        """Execute complete pipeline"""
        print("\n")
        print("╔" + "="*78 + "╗")
        print("║" + " "*78 + "║")
        print("║" + " AI NETWORK INTRUSION DETECTION SYSTEM ".center(78) + "║")
        print("║" + " COMPLETE EXECUTION PIPELINE ".center(78) + "║")
        print("║" + " "*78 + "║")
        print("╚" + "="*78 + "╝")
        
        try:
            # Phase 1: Load Data
            df = self.phase_1_load_data()
            
            # Phase 2: Process Data
            data = self.phase_2_process_data(df)
            
            # Phase 3: Train Models
            self.phase_3_train_models(data)
            
            # Phase 4: Test Models
            self.phase_4_test_models(data)
            
            # Phase 5: Get Statistics
            self.phase_5_get_statistics()
            
            # Phase 6: Save Results
            results_file = self.phase_6_save_results()
            
            # Final Summary
            self.print_summary()
            
            return True
            
        except Exception as e:
            logger.error(f"Pipeline execution failed: {e}")
            print(f"\n❌ Pipeline failed: {e}")
            return False
    
    def print_summary(self):
        """Print execution summary"""
        print("\n")
        print("╔" + "="*78 + "╗")
        print("║" + " EXECUTION SUMMARY ".center(78) + "║")
        print("╚" + "="*78 + "╝\n")
        
        # Phase Summary
        print("📋 PHASE STATUS:")
        for phase, result in self.results['phase'].items():
            status_symbol = "✓" if result['status'].lower() == 'completed' else "✗"
            print(f"  {status_symbol} {phase}: {result['status']}")
        
        # Training Summary
        if 'training' in self.results:
            print(f"\n🤖 TRAINING RESULTS:")
            print(f"  ✓ Best Model: {self.results['training']['best_model']}")
            print(f"  ✓ Models Trained: {self.results['training']['models_count']}")
        
        # Testing Summary
        if 'testing' in self.results:
            print(f"\n🧪 TESTING RESULTS:")
            print(f"  ✓ Accuracy: {self.results['testing']['accuracy']*100:.2f}%")
            print(f"  ✓ Avg Confidence: {self.results['testing']['avg_confidence']*100:.2f}%")
            print(f"  ✓ Tests Run: {self.results['testing']['total_tests']}")
        
        # Statistics Summary
        if 'statistics' in self.results:
            stats = self.results['statistics']
            print(f"\n📊 STATISTICS:")
            print(f"  ✓ Total Packets: {stats.get('total_packets', 0)}")
            print(f"  ✓ Total Attacks: {stats.get('total_attacks', 0)}")
            print(f"  ✓ Detection Rate: {stats.get('detection_rate', 0)*100:.2f}%")
        
        # Execution Time
        execution_time = datetime.now() - self.start_time
        print(f"\n⏱️  EXECUTION TIME: {execution_time}")
        
        print("\n" + "="*80)
        print("✅ PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
        print("="*80)
        print("\n🌐 To view results in web dashboard:")
        print("   python detect.py --mode api")
        print("   Then open: http://localhost:5000")
        print("\n")

def main():
    """Main entry point"""
    try:
        pipeline = ExecutionPipeline()
        success = pipeline.execute()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
