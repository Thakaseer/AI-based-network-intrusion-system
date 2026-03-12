"""
Direct attack detection test - tests all attack types locally
Without requiring Flask to be running
"""

import sys
sys.path.insert(0, '.')

from src.intrusion_detector import create_detector
from datetime import datetime
import json

# Initialize detector
print("\n" + "="*80)
print("AI-NIDS: Direct Multi-Attack Type Detection Test")
print("="*80 + "\n")

print("🔧 Initializing detector...")
detector = create_detector()
print("✓ Detector initialized\n")

# ============================================================================
# NORMAL TRAFFIC SAMPLES
# ============================================================================
normal_samples = [
    {
        "name": "Normal Web Traffic",
        "data": {
            "duration": 120, "protocol_type": 0, "service": 23, "flag": 0,
            "src_bytes": 1200, "dst_bytes": 1500, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 1,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 45, "srv_count": 40, "serror_rate": 0.0, "srv_serror_rate": 0.0,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.85,
            "diff_srv_rate": 0.1, "srv_diff_host_rate": 0.05, "dst_host_count": 55,
            "dst_host_srv_count": 45, "dst_host_same_srv_rate": 0.8, "dst_host_diff_srv_rate": 0.15,
            "dst_host_same_src_port_rate": 0.7, "dst_host_srv_diff_host_rate": 0.1,
            "dst_host_serror_rate": 0.0, "dst_host_srv_serror_rate": 0.0,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "Normal Email Traffic",
        "data": {
            "duration": 180, "protocol_type": 0, "service": 25, "flag": 0,
            "src_bytes": 2000, "dst_bytes": 2500, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 1,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 60, "srv_count": 55, "serror_rate": 0.02, "srv_serror_rate": 0.01,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.9,
            "diff_srv_rate": 0.05, "srv_diff_host_rate": 0.02, "dst_host_count": 70,
            "dst_host_srv_count": 60, "dst_host_same_srv_rate": 0.85, "dst_host_diff_srv_rate": 0.1,
            "dst_host_same_src_port_rate": 0.75, "dst_host_srv_diff_host_rate": 0.08,
            "dst_host_serror_rate": 0.01, "dst_host_srv_serror_rate": 0.0,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    }
]

# ============================================================================
# PROBE ATTACK SAMPLES
# ============================================================================
probe_samples = [
    {
        "name": "Port Scan Attack",
        "data": {
            "duration": 10, "protocol_type": 1, "service": 0, "flag": 3,
            "src_bytes": 120, "dst_bytes": 80, "land": 0, "wrong_fragment": 3,
            "urgent": 0, "hot": 1, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 180, "srv_count": 60, "serror_rate": 0.8, "srv_serror_rate": 0.75,
            "rerror_rate": 0.6, "srv_rerror_rate": 0.55, "same_srv_rate": 0.2,
            "diff_srv_rate": 0.8, "srv_diff_host_rate": 0.75, "dst_host_count": 220,
            "dst_host_srv_count": 110, "dst_host_same_srv_rate": 0.25, "dst_host_diff_srv_rate": 0.75,
            "dst_host_same_src_port_rate": 0.15, "dst_host_srv_diff_host_rate": 0.7,
            "dst_host_serror_rate": 0.7, "dst_host_srv_serror_rate": 0.65,
            "dst_host_rerror_rate": 0.5, "dst_host_srv_rerror_rate": 0.45,
        }
    },
    {
        "name": "Network Reconnaissance",
        "data": {
            "duration": 15, "protocol_type": 2, "service": 0, "flag": 4,
            "src_bytes": 100, "dst_bytes": 60, "land": 0, "wrong_fragment": 2,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 150, "srv_count": 40, "serror_rate": 0.7, "srv_serror_rate": 0.65,
            "rerror_rate": 0.55, "srv_rerror_rate": 0.5, "same_srv_rate": 0.3,
            "diff_srv_rate": 0.7, "srv_diff_host_rate": 0.65, "dst_host_count": 200,
            "dst_host_srv_count": 95, "dst_host_same_srv_rate": 0.35, "dst_host_diff_srv_rate": 0.65,
            "dst_host_same_src_port_rate": 0.2, "dst_host_srv_diff_host_rate": 0.6,
            "dst_host_serror_rate": 0.65, "dst_host_srv_serror_rate": 0.6,
            "dst_host_rerror_rate": 0.45, "dst_host_srv_rerror_rate": 0.4,
        }
    }
]

# ============================================================================
# R2L ATTACK SAMPLES
# ============================================================================
r2l_samples = [
    {
        "name": "FTP Brute Force Attack",
        "data": {
            "duration": 200, "protocol_type": 0, "service": 21, "flag": 0,
            "src_bytes": 2500, "dst_bytes": 2000, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 1, "num_failed_logins": 6, "logged_in": 1,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 2, "num_shells": 1, "num_access_files": 3,
            "num_outbound_cmds": 1, "is_host_login": 1, "is_guest_login": 0,
            "count": 65, "srv_count": 58, "serror_rate": 0.35, "srv_serror_rate": 0.3,
            "rerror_rate": 0.2, "srv_rerror_rate": 0.15, "same_srv_rate": 0.75,
            "diff_srv_rate": 0.25, "srv_diff_host_rate": 0.22, "dst_host_count": 90,
            "dst_host_srv_count": 75, "dst_host_same_srv_rate": 0.7, "dst_host_diff_srv_rate": 0.3,
            "dst_host_same_src_port_rate": 0.55, "dst_host_srv_diff_host_rate": 0.28,
            "dst_host_serror_rate": 0.25, "dst_host_srv_serror_rate": 0.2,
            "dst_host_rerror_rate": 0.12, "dst_host_srv_rerror_rate": 0.1,
        }
    },
    {
        "name": "SSH Login Attack",
        "data": {
            "duration": 150, "protocol_type": 0, "service": 22, "flag": 0,
            "src_bytes": 1800, "dst_bytes": 2200, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 5, "logged_in": 1,
            "num_compromised": 1, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 1, "num_shells": 2, "num_access_files": 2,
            "num_outbound_cmds": 0, "is_host_login": 1, "is_guest_login": 0,
            "count": 55, "srv_count": 50, "serror_rate": 0.32, "srv_serror_rate": 0.28,
            "rerror_rate": 0.18, "srv_rerror_rate": 0.14, "same_srv_rate": 0.8,
            "diff_srv_rate": 0.2, "srv_diff_host_rate": 0.18, "dst_host_count": 85,
            "dst_host_srv_count": 72, "dst_host_same_srv_rate": 0.75, "dst_host_diff_srv_rate": 0.25,
            "dst_host_same_src_port_rate": 0.6, "dst_host_srv_diff_host_rate": 0.22,
            "dst_host_serror_rate": 0.22, "dst_host_srv_serror_rate": 0.18,
            "dst_host_rerror_rate": 0.1, "dst_host_srv_rerror_rate": 0.08,
        }
    }
]

# ============================================================================
# U2R ATTACK SAMPLES
# ============================================================================
u2r_samples = [
    {
        "name": "Privilege Escalation via Buffer Overflow",
        "data": {
            "duration": 120, "protocol_type": 0, "service": 15, "flag": 0,
            "src_bytes": 2000, "dst_bytes": 1800, "land": 0, "wrong_fragment": 0,
            "urgent": 2, "hot": 4, "num_failed_logins": 1, "logged_in": 1,
            "num_compromised": 2, "root_shell": 1, "su_attempted": 1, "num_root": 10,
            "num_file_creations": 4, "num_shells": 3, "num_access_files": 5,
            "num_outbound_cmds": 2, "is_host_login": 0, "is_guest_login": 0,
            "count": 55, "srv_count": 48, "serror_rate": 0.18, "srv_serror_rate": 0.14,
            "rerror_rate": 0.08, "srv_rerror_rate": 0.06, "same_srv_rate": 0.82,
            "diff_srv_rate": 0.18, "srv_diff_host_rate": 0.12, "dst_host_count": 75,
            "dst_host_srv_count": 65, "dst_host_same_srv_rate": 0.8, "dst_host_diff_srv_rate": 0.2,
            "dst_host_same_src_port_rate": 0.65, "dst_host_srv_diff_host_rate": 0.15,
            "dst_host_serror_rate": 0.12, "dst_host_srv_serror_rate": 0.1,
            "dst_host_rerror_rate": 0.06, "dst_host_srv_rerror_rate": 0.04,
        }
    },
    {
        "name": "Sudo Privilege Escalation",
        "data": {
            "duration": 90, "protocol_type": 0, "service": 15, "flag": 0,
            "src_bytes": 1600, "dst_bytes": 1400, "land": 0, "wrong_fragment": 0,
            "urgent": 1, "hot": 3, "num_failed_logins": 2, "logged_in": 1,
            "num_compromised": 3, "root_shell": 1, "su_attempted": 1, "num_root": 8,
            "num_file_creations": 3, "num_shells": 2, "num_access_files": 4,
            "num_outbound_cmds": 1, "is_host_login": 0, "is_guest_login": 0,
            "count": 50, "srv_count": 45, "serror_rate": 0.16, "srv_serror_rate": 0.12,
            "rerror_rate": 0.07, "srv_rerror_rate": 0.05, "same_srv_rate": 0.85,
            "diff_srv_rate": 0.15, "srv_diff_host_rate": 0.1, "dst_host_count": 70,
            "dst_host_srv_count": 62, "dst_host_same_srv_rate": 0.82, "dst_host_diff_srv_rate": 0.18,
            "dst_host_same_src_port_rate": 0.68, "dst_host_srv_diff_host_rate": 0.12,
            "dst_host_serror_rate": 0.1, "dst_host_srv_serror_rate": 0.08,
            "dst_host_rerror_rate": 0.05, "dst_host_srv_rerror_rate": 0.03,
        }
    }
]

# ============================================================================
# TEST FUNCTION
# ============================================================================

def test_samples(attack_type, samples):
    """Test a list of samples"""
    print(f"┌─ {attack_type.upper()} DETECTION")
    print(f"│  Testing {len(samples)} samples\n")
    
    results = []
    for sample in samples:
        result = detector.detect(sample['data'])
        results.append(result)
        
        pred = result.get('prediction_label', 'Unknown')
        conf = result.get('confidence', 0) * 100
        is_attack = "✓" if result.get('is_attack') else "✗"
        
        print(f"  {is_attack} {sample['name']:<50} → {pred:<12} ({conf:.1f}%)")
    
    print()
    return results

# ============================================================================
# RUN TESTS
# ============================================================================

all_results = {
    'Normal': test_samples('Normal Traffic', normal_samples),
    'Probe': test_samples('Probe Attacks', probe_samples),
    'R2L': test_samples('R2L Attacks (Remote to Local)', r2l_samples),
    'U2R': test_samples('U2R Attacks (User to Root)', u2r_samples)
}

# Print summary
print("\n" + "="*80)
print("DETECTION SUMMARY")
print("="*80 + "\n")

total_detected = 0
total_samples = 0

for attack_type, results in all_results.items():
    detected_count = sum(1 for r in results if r.get('is_attack'))
    total = len(results)
    total_detected += detected_count
    total_samples += total
    
    print(f"{attack_type:15} - {detected_count}/{total} detected as attacks")

print(f"\n{'TOTAL':15} - {total_detected}/{total_samples} detected ({total_detected*100//total_samples}%)")
print("\n" + "="*80)
print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*80 + "\n")
