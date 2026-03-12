#!/usr/bin/env python3
"""
Test script to generate, process, and detect R2L and U2R attacks
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
from src.intrusion_detector import create_detector
from src.data_processing import DataProcessor
from src.utils import setup_logging

logger = setup_logging(__name__, 'test_r2l_u2r.log')

def generate_r2l_data(n_samples=20):
    """Generate R2L (Remote to Local) attack data"""
    print(f"\n{'='*80}")
    print(f"Generating {n_samples} R2L Attack Samples")
    print(f"{'='*80}")
    
    r2l_data = []
    
    for i in range(n_samples):
        packet = {
            'duration': np.random.randint(200, 400),
            'protocol_type': 0,  # TCP
            'service': np.random.choice([21, 23, 25]),  # FTP, telnet, smtp
            'flag': 0,  # SYN
            'src_bytes': np.random.randint(2000, 6000),
            'dst_bytes': np.random.randint(1500, 4000),
            'land': 0,
            'wrong_fragment': np.random.choice([0, 1]),
            'urgent': 0,
            'hot': 0,
            'num_failed_logins': np.random.randint(2, 8),  # Multiple failed attempts
            'logged_in': 1,  # Eventually logs in
            'num_compromised': 0,
            'root_shell': 0,
            'su_attempted': 0,
            'num_root': 0,
            'num_file_creations': np.random.randint(0, 3),
            'num_shells': np.random.randint(0, 2),
            'num_access_files': np.random.randint(0, 3),
            'num_outbound_cmds': np.random.randint(0, 2),
            'is_host_login': 1,  # Remote login
            'is_guest_login': 0,
            'count': np.random.randint(50, 100),
            'srv_count': np.random.randint(30, 70),
            'serror_rate': np.random.uniform(0.2, 0.4),
            'srv_serror_rate': np.random.uniform(0.15, 0.35),
            'rerror_rate': np.random.uniform(0.05, 0.2),
            'srv_rerror_rate': np.random.uniform(0.05, 0.15),
            'same_srv_rate': np.random.uniform(0.6, 0.8),
            'diff_srv_rate': np.random.uniform(0.2, 0.4),
            'srv_diff_host_rate': np.random.uniform(0.1, 0.3),
            'dst_host_count': np.random.randint(80, 150),
            'dst_host_srv_count': np.random.randint(50, 100),
            'dst_host_same_srv_rate': np.random.uniform(0.5, 0.75),
            'dst_host_diff_srv_rate': np.random.uniform(0.25, 0.5),
            'dst_host_same_src_port_rate': np.random.uniform(0.3, 0.6),
            'dst_host_srv_diff_host_rate': np.random.uniform(0.2, 0.4),
            'dst_host_serror_rate': np.random.uniform(0.1, 0.3),
            'dst_host_srv_serror_rate': np.random.uniform(0.08, 0.25),
            'dst_host_rerror_rate': np.random.uniform(0.05, 0.15),
            'dst_host_srv_rerror_rate': np.random.uniform(0.05, 0.12),
            'attack_type': 'R2L'
        }
        r2l_data.append(packet)
    
    return pd.DataFrame(r2l_data)

def generate_u2r_data(n_samples=20):
    """Generate U2R (User to Root) attack data"""
    print(f"\n{'='*80}")
    print(f"Generating {n_samples} U2R Attack Samples")
    print(f"{'='*80}")
    
    u2r_data = []
    
    for i in range(n_samples):
        packet = {
            'duration': np.random.randint(100, 300),
            'protocol_type': 0,  # TCP
            'service': np.random.choice([15, 23]),  # shell, telnet
            'flag': 0,  # SYN
            'src_bytes': np.random.randint(1500, 4000),
            'dst_bytes': np.random.randint(1000, 3000),
            'land': 0,
            'wrong_fragment': 0,
            'urgent': np.random.choice([0, 1]),
            'hot': np.random.randint(1, 4),  # Multiple hot indicators
            'num_failed_logins': np.random.randint(1, 4),
            'logged_in': 1,
            'num_compromised': np.random.randint(1, 3),  # Compromised access
            'root_shell': 1,  # ROOT SHELL - Critical indicator
            'su_attempted': 1,  # su command attempted
            'num_root': np.random.randint(5, 12),  # Multiple root operations
            'num_file_creations': np.random.randint(2, 5),
            'num_shells': np.random.randint(1, 4),
            'num_access_files': np.random.randint(2, 5),
            'num_outbound_cmds': np.random.randint(1, 3),
            'is_host_login': 0,
            'is_guest_login': 0,
            'count': np.random.randint(40, 80),
            'srv_count': np.random.randint(30, 60),
            'serror_rate': np.random.uniform(0.1, 0.25),
            'srv_serror_rate': np.random.uniform(0.08, 0.2),
            'rerror_rate': np.random.uniform(0.02, 0.1),
            'srv_rerror_rate': np.random.uniform(0.02, 0.08),
            'same_srv_rate': np.random.uniform(0.7, 0.9),
            'diff_srv_rate': np.random.uniform(0.1, 0.3),
            'srv_diff_host_rate': np.random.uniform(0.05, 0.2),
            'dst_host_count': np.random.randint(60, 120),
            'dst_host_srv_count': np.random.randint(50, 100),
            'dst_host_same_srv_rate': np.random.uniform(0.65, 0.85),
            'dst_host_diff_srv_rate': np.random.uniform(0.15, 0.35),
            'dst_host_same_src_port_rate': np.random.uniform(0.4, 0.7),
            'dst_host_srv_diff_host_rate': np.random.uniform(0.1, 0.25),
            'dst_host_serror_rate': np.random.uniform(0.08, 0.2),
            'dst_host_srv_serror_rate': np.random.uniform(0.05, 0.15),
            'dst_host_rerror_rate': np.random.uniform(0.02, 0.1),
            'dst_host_srv_rerror_rate': np.random.uniform(0.02, 0.08),
            'attack_type': 'U2R'
        }
        u2r_data.append(packet)
    
    return pd.DataFrame(u2r_data)

def process_and_detect(detector, df, attack_name):
    """Process data and run detection"""
    print(f"\n{'='*80}")
    print(f"Processing and Detecting {attack_name} Attacks")
    print(f"{'='*80}")
    
    attack_type_col = df['attack_type'].copy()
    df_for_detection = df.drop('attack_type', axis=1)
    
    results = []
    predictions = []
    confidences = []
    
    for idx, row in df_for_detection.iterrows():
        result = detector.detect(row.to_dict())
        if result:
            results.append(result)
            predictions.append(result['prediction_label'])
            confidences.append(result['confidence'])
        else:
            print(f"  ❌ Detection failed for sample {idx+1}")
    
    # Create results dataframe
    results_df = pd.DataFrame(results)
    
    # Calculate statistics
    total_samples = len(results)
    detected_as_attacks = sum([1 for pred in predictions if pred != 'Normal'])
    accuracy = (detected_as_attacks / total_samples * 100) if total_samples > 0 else 0
    avg_confidence = np.mean(confidences) if confidences else 0
    
    print(f"\n{'─'*80}")
    print(f"📊 Detection Summary for {attack_name}:")
    print(f"{'─'*80}")
    print(f"Total Samples:           {total_samples}")
    print(f"Detected as Attacks:     {detected_as_attacks}/{total_samples}")
    print(f"Attack Detection Rate:   {accuracy:.2f}%")
    print(f"Average Confidence:      {avg_confidence*100:.2f}%")
    
    # Attack type distribution
    print(f"\n{'─'*80}")
    print(f"📈 Predicted Attack Types:")
    print(f"{'─'*80}")
    attack_counts = pd.Series(predictions).value_counts()
    for attack_type, count in attack_counts.items():
        percentage = (count / total_samples * 100)
        print(f"  {attack_type:12s}: {count:2d} samples ({percentage:5.1f}%)")
    
    # Sample detections
    print(f"\n{'─'*80}")
    print(f"🔍 Sample Detection Results (first 5):")
    print(f"{'─'*80}")
    for i in range(min(5, len(results))):
        result = results[i]
        print(f"\n  Sample {i+1}:")
        print(f"    Predicted:  {result['prediction_label']}")
        print(f"    Confidence: {result['confidence']*100:.2f}%")
        print(f"    Is Attack:  {'✓ Yes' if result['is_attack'] else '✗ No'}")
    
    return results_df, results

def main():
    """Main execution"""
    print("\n" + "="*80)
    print("R2L and U2R Attack Data Generation and Detection")
    print("="*80)
    
    # Create detector
    print("\n🔧 Initializing detector...")
    detector = create_detector()
    
    if detector.model is None:
        print("❌ Model not loaded! Please train the model first.")
        return
    
    if detector.scaler is None:
        print("❌ Scaler not loaded!")
        return
    
    print("✓ Detector initialized successfully")
    
    # Generate data
    r2l_df = generate_r2l_data(n_samples=20)
    u2r_df = generate_u2r_data(n_samples=20)
    
    # Process and detect
    r2l_results_df, r2l_results = process_and_detect(detector, r2l_df, "R2L")
    u2r_results_df, u2r_results = process_and_detect(detector, u2r_df, "U2R")
    
    # Combined statistics
    print(f"\n{'='*80}")
    print("📋 Combined Statistics")
    print(f"{'='*80}")
    
    total_samples = len(r2l_results) + len(u2r_results)
    total_attacks_detected = len([r for r in r2l_results if r['is_attack']]) + \
                             len([r for r in u2r_results if r['is_attack']])
    
    print(f"Total Samples Tested:    {total_samples}")
    print(f"Total Attacks Detected:  {total_attacks_detected}")
    print(f"Overall Detection Rate:  {(total_attacks_detected/total_samples*100):.2f}%")
    
    # Save results to CSV
    output_dir = os.path.join('logs')
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save R2L results
    r2l_output_file = os.path.join(output_dir, f'r2l_detection_results_{timestamp}.csv')
    r2l_results_df.to_csv(r2l_output_file, index=False)
    print(f"\n✓ R2L results saved to: {r2l_output_file}")
    
    # Save U2R results
    u2r_output_file = os.path.join(output_dir, f'u2r_detection_results_{timestamp}.csv')
    u2r_results_df.to_csv(u2r_output_file, index=False)
    print(f"✓ U2R results saved to: {u2r_output_file}")
    
    # Create summary file
    summary_file = os.path.join(output_dir, f'r2l_u2r_summary_{timestamp}.txt')
    with open(summary_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("R2L and U2R Attack Detection Summary\n")
        f.write("="*80 + "\n\n")
        
        f.write("R2L ATTACKS:\n")
        f.write("-"*80 + "\n")
        f.write(f"Total Samples: {len(r2l_results)}\n")
        f.write(f"Detected as Attacks: {len([r for r in r2l_results if r['is_attack']])}\n")
        f.write(f"Detection Rate: {(len([r for r in r2l_results if r['is_attack']])/len(r2l_results)*100):.2f}%\n")
        f.write(f"Average Confidence: {np.mean([r['confidence'] for r in r2l_results])*100:.2f}%\n\n")
        
        f.write("U2R ATTACKS:\n")
        f.write("-"*80 + "\n")
        f.write(f"Total Samples: {len(u2r_results)}\n")
        f.write(f"Detected as Attacks: {len([r for r in u2r_results if r['is_attack']])}\n")
        f.write(f"Detection Rate: {(len([r for r in u2r_results if r['is_attack']])/len(u2r_results)*100):.2f}%\n")
        f.write(f"Average Confidence: {np.mean([r['confidence'] for r in u2r_results])*100:.2f}%\n\n")
        
        f.write("COMBINED:\n")
        f.write("-"*80 + "\n")
        f.write(f"Total Samples: {total_samples}\n")
        f.write(f"Total Attacks Detected: {total_attacks_detected}\n")
        f.write(f"Overall Detection Rate: {(total_attacks_detected/total_samples*100):.2f}%\n")
    
    print(f"✓ Summary saved to: {summary_file}")
    
    print(f"\n{'='*80}")
    print("✓ Testing completed successfully!")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()
