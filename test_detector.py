#!/usr/bin/env python3
"""Test detector loading"""

from src.intrusion_detector import create_detector

detector = create_detector()
print('Model loaded:', detector.model is not None)
print('Scaler loaded:', detector.scaler is not None)
print('Feature names:', len(detector.feature_names))

# Test detection
sample_packet = {
    'duration': 100,
    'protocol_type': 0,
    'service': 5,
    'flag': 2,
    'src_bytes': 1000,
    'dst_bytes': 2000,
    'land': 0,
    'wrong_fragment': 0,
    'urgent': 0,
    'hot': 0,
    'num_failed_logins': 0,
    'logged_in': 1,
    'num_compromised': 0,
    'root_shell': 0,
    'su_attempted': 0,
    'num_root': 0,
    'num_file_creations': 0,
    'num_shells': 0,
    'num_access_files': 0,
    'num_outbound_cmds': 0,
    'is_host_login': 0,
    'is_guest_login': 0,
    'count': 100,
    'srv_count': 50,
    'serror_rate': 0.1,
    'srv_serror_rate': 0.05,
    'rerror_rate': 0.0,
    'srv_rerror_rate': 0.0,
    'same_srv_rate': 0.8,
    'diff_srv_rate': 0.2,
    'srv_diff_host_rate': 0.1,
    'dst_host_count': 200,
    'dst_host_srv_count': 100,
    'dst_host_same_srv_rate': 0.7,
    'dst_host_diff_srv_rate': 0.3,
    'dst_host_same_src_port_rate': 0.5,
    'dst_host_srv_diff_host_rate': 0.2,
    'dst_host_serror_rate': 0.05,
    'dst_host_srv_serror_rate': 0.02,
    'dst_host_rerror_rate': 0.0,
    'dst_host_srv_rerror_rate': 0.0,
}

result = detector.detect(sample_packet)
if result:
    print('\nDetection Result:')
    print(f"  Prediction: {result['prediction_label']}")
    print(f"  Confidence: {result['confidence']*100:.2f}%")
    print(f"  Is Attack: {result['is_attack']}")
else:
    print('Detection failed')
