"""
Comprehensive test script for all attack types detection
Generates realistic samples for Normal, DoS, Probe, R2L, and U2R attacks
"""

import requests
import json
from datetime import datetime
import time

# Flask API endpoint
API_URL = 'http://127.0.0.1:5000/api/detect'

# ============================================================================
# NORMAL TRAFFIC SAMPLES
# ============================================================================
normal_samples = [
    {
        "name": "Normal Web Traffic 1",
        "data": {
            "duration": 120,
            "protocol_type": 0,  # TCP
            "service": 23,  # telnet
            "flag": 0,  # SYN
            "src_bytes": 1200,
            "dst_bytes": 1500,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 0,
            "hot": 0,
            "num_failed_logins": 0,
            "logged_in": 1,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 0,
            "num_shells": 0,
            "num_access_files": 0,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 45,
            "srv_count": 40,
            "serror_rate": 0.0,
            "srv_serror_rate": 0.0,
            "rerror_rate": 0.0,
            "srv_rerror_rate": 0.0,
            "same_srv_rate": 0.85,
            "diff_srv_rate": 0.1,
            "srv_diff_host_rate": 0.05,
            "dst_host_count": 55,
            "dst_host_srv_count": 45,
            "dst_host_same_srv_rate": 0.8,
            "dst_host_diff_srv_rate": 0.15,
            "dst_host_same_src_port_rate": 0.7,
            "dst_host_srv_diff_host_rate": 0.1,
            "dst_host_serror_rate": 0.0,
            "dst_host_srv_serror_rate": 0.0,
            "dst_host_rerror_rate": 0.0,
            "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "Normal Email Traffic",
        "data": {
            "duration": 180,
            "protocol_type": 0,  # TCP
            "service": 25,  # SMTP
            "flag": 0,
            "src_bytes": 2000,
            "dst_bytes": 2500,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 0,
            "hot": 0,
            "num_failed_logins": 0,
            "logged_in": 1,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 0,
            "num_shells": 0,
            "num_access_files": 0,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 60,
            "srv_count": 55,
            "serror_rate": 0.02,
            "srv_serror_rate": 0.01,
            "rerror_rate": 0.0,
            "srv_rerror_rate": 0.0,
            "same_srv_rate": 0.9,
            "diff_srv_rate": 0.05,
            "srv_diff_host_rate": 0.02,
            "dst_host_count": 70,
            "dst_host_srv_count": 60,
            "dst_host_same_srv_rate": 0.85,
            "dst_host_diff_srv_rate": 0.1,
            "dst_host_same_src_port_rate": 0.75,
            "dst_host_srv_diff_host_rate": 0.08,
            "dst_host_serror_rate": 0.01,
            "dst_host_srv_serror_rate": 0.0,
            "dst_host_rerror_rate": 0.0,
            "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "Normal FTP Transfer",
        "data": {
            "duration": 240,
            "protocol_type": 0,  # TCP
            "service": 21,  # FTP
            "flag": 0,
            "src_bytes": 5000,
            "dst_bytes": 4500,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 0,
            "hot": 0,
            "num_failed_logins": 0,
            "logged_in": 1,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 1,
            "num_shells": 0,
            "num_access_files": 1,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 50,
            "srv_count": 48,
            "serror_rate": 0.0,
            "srv_serror_rate": 0.0,
            "rerror_rate": 0.0,
            "srv_rerror_rate": 0.0,
            "same_srv_rate": 0.95,
            "diff_srv_rate": 0.02,
            "srv_diff_host_rate": 0.0,
            "dst_host_count": 40,
            "dst_host_srv_count": 38,
            "dst_host_same_srv_rate": 0.92,
            "dst_host_diff_srv_rate": 0.05,
            "dst_host_same_src_port_rate": 0.8,
            "dst_host_srv_diff_host_rate": 0.02,
            "dst_host_serror_rate": 0.0,
            "dst_host_srv_serror_rate": 0.0,
            "dst_host_rerror_rate": 0.0,
            "dst_host_srv_rerror_rate": 0.0,
        }
    }
]

# ============================================================================
# PROBE ATTACK SAMPLES (Reconnaissance/Port Scanning)
# ============================================================================
probe_samples = [
    {
        "name": "Port Scan Attack 1",
        "data": {
            "duration": 10,
            "protocol_type": 1,  # UDP
            "service": 0,  # Other/Mixed
            "flag": 3,  # RSTO
            "src_bytes": 120,
            "dst_bytes": 80,
            "land": 0,
            "wrong_fragment": 3,
            "urgent": 0,
            "hot": 1,
            "num_failed_logins": 0,
            "logged_in": 0,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 0,
            "num_shells": 0,
            "num_access_files": 0,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 180,  # Many connections to different ports
            "srv_count": 60,  # Different services
            "serror_rate": 0.8,  # High error rate
            "srv_serror_rate": 0.75,
            "rerror_rate": 0.6,
            "srv_rerror_rate": 0.55,
            "same_srv_rate": 0.2,  # Low - scanning multiple services
            "diff_srv_rate": 0.8,  # High - different services
            "srv_diff_host_rate": 0.75,
            "dst_host_count": 220,  # Scanning many hosts
            "dst_host_srv_count": 110,
            "dst_host_same_srv_rate": 0.25,
            "dst_host_diff_srv_rate": 0.75,
            "dst_host_same_src_port_rate": 0.15,
            "dst_host_srv_diff_host_rate": 0.7,
            "dst_host_serror_rate": 0.7,
            "dst_host_srv_serror_rate": 0.65,
            "dst_host_rerror_rate": 0.5,
            "dst_host_srv_rerror_rate": 0.45,
        }
    },
    {
        "name": "Network Reconnaissance",
        "data": {
            "duration": 15,
            "protocol_type": 2,  # ICMP
            "service": 0,
            "flag": 4,  # RSTR
            "src_bytes": 100,
            "dst_bytes": 60,
            "land": 0,
            "wrong_fragment": 2,
            "urgent": 0,
            "hot": 0,
            "num_failed_logins": 0,
            "logged_in": 0,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 0,
            "num_shells": 0,
            "num_access_files": 0,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 150,
            "srv_count": 40,
            "serror_rate": 0.7,
            "srv_serror_rate": 0.65,
            "rerror_rate": 0.55,
            "srv_rerror_rate": 0.5,
            "same_srv_rate": 0.3,
            "diff_srv_rate": 0.7,
            "srv_diff_host_rate": 0.65,
            "dst_host_count": 200,
            "dst_host_srv_count": 95,
            "dst_host_same_srv_rate": 0.35,
            "dst_host_diff_srv_rate": 0.65,
            "dst_host_same_src_port_rate": 0.2,
            "dst_host_srv_diff_host_rate": 0.6,
            "dst_host_serror_rate": 0.65,
            "dst_host_srv_serror_rate": 0.6,
            "dst_host_rerror_rate": 0.45,
            "dst_host_srv_rerror_rate": 0.4,
        }
    },
    {
        "name": "Service Enumeration",
        "data": {
            "duration": 8,
            "protocol_type": 0,  # TCP
            "service": 0,
            "flag": 3,
            "src_bytes": 110,
            "dst_bytes": 90,
            "land": 0,
            "wrong_fragment": 1,
            "urgent": 0,
            "hot": 2,
            "num_failed_logins": 0,
            "logged_in": 0,
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 0,
            "num_shells": 0,
            "num_access_files": 0,
            "num_outbound_cmds": 0,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 160,
            "srv_count": 70,
            "serror_rate": 0.75,
            "srv_serror_rate": 0.72,
            "rerror_rate": 0.58,
            "srv_rerror_rate": 0.52,
            "same_srv_rate": 0.25,
            "diff_srv_rate": 0.75,
            "srv_diff_host_rate": 0.68,
            "dst_host_count": 210,
            "dst_host_srv_count": 105,
            "dst_host_same_srv_rate": 0.3,
            "dst_host_diff_srv_rate": 0.7,
            "dst_host_same_src_port_rate": 0.18,
            "dst_host_srv_diff_host_rate": 0.65,
            "dst_host_serror_rate": 0.68,
            "dst_host_srv_serror_rate": 0.62,
            "dst_host_rerror_rate": 0.48,
            "dst_host_srv_rerror_rate": 0.42,
        }
    }
]

# ============================================================================
# R2L ATTACK SAMPLES (Remote to Local - Unauthorized Remote Access)
# ============================================================================
r2l_samples = [
    {
        "name": "FTP Brute Force Attack",
        "data": {
            "duration": 200,
            "protocol_type": 0,  # TCP
            "service": 21,  # FTP
            "flag": 0,
            "src_bytes": 2500,
            "dst_bytes": 2000,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 0,
            "hot": 1,
            "num_failed_logins": 6,  # Multiple failed login attempts
            "logged_in": 1,  # Eventually successful login
            "num_compromised": 0,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 2,  # Attacker creates files
            "num_shells": 1,  # Spawns shell
            "num_access_files": 3,  # Accesses files
            "num_outbound_cmds": 1,
            "is_host_login": 1,  # Remote login indicator
            "is_guest_login": 0,
            "count": 65,
            "srv_count": 58,
            "serror_rate": 0.35,
            "srv_serror_rate": 0.3,
            "rerror_rate": 0.2,
            "srv_rerror_rate": 0.15,
            "same_srv_rate": 0.75,
            "diff_srv_rate": 0.25,
            "srv_diff_host_rate": 0.22,
            "dst_host_count": 90,
            "dst_host_srv_count": 75,
            "dst_host_same_srv_rate": 0.7,
            "dst_host_diff_srv_rate": 0.3,
            "dst_host_same_src_port_rate": 0.55,
            "dst_host_srv_diff_host_rate": 0.28,
            "dst_host_serror_rate": 0.25,
            "dst_host_srv_serror_rate": 0.2,
            "dst_host_rerror_rate": 0.12,
            "dst_host_srv_rerror_rate": 0.1,
        }
    },
    {
        "name": "SSH Login Attack",
        "data": {
            "duration": 150,
            "protocol_type": 0,  # TCP
            "service": 22,  # SSH
            "flag": 0,
            "src_bytes": 1800,
            "dst_bytes": 2200,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 0,
            "hot": 0,
            "num_failed_logins": 5,  # Failed attempts
            "logged_in": 1,  # Success
            "num_compromised": 1,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 1,
            "num_shells": 2,
            "num_access_files": 2,
            "num_outbound_cmds": 0,
            "is_host_login": 1,
            "is_guest_login": 0,
            "count": 55,
            "srv_count": 50,
            "serror_rate": 0.32,
            "srv_serror_rate": 0.28,
            "rerror_rate": 0.18,
            "srv_rerror_rate": 0.14,
            "same_srv_rate": 0.8,
            "diff_srv_rate": 0.2,
            "srv_diff_host_rate": 0.18,
            "dst_host_count": 85,
            "dst_host_srv_count": 72,
            "dst_host_same_srv_rate": 0.75,
            "dst_host_diff_srv_rate": 0.25,
            "dst_host_same_src_port_rate": 0.6,
            "dst_host_srv_diff_host_rate": 0.22,
            "dst_host_serror_rate": 0.22,
            "dst_host_srv_serror_rate": 0.18,
            "dst_host_rerror_rate": 0.1,
            "dst_host_srv_rerror_rate": 0.08,
        }
    },
    {
        "name": "Telnet Unauthorized Access",
        "data": {
            "duration": 180,
            "protocol_type": 0,  # TCP
            "service": 23,  # Telnet
            "flag": 0,
            "src_bytes": 1500,
            "dst_bytes": 1900,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 1,
            "hot": 1,
            "num_failed_logins": 4,
            "logged_in": 1,
            "num_compromised": 1,
            "root_shell": 0,
            "su_attempted": 0,
            "num_root": 0,
            "num_file_creations": 2,
            "num_shells": 1,
            "num_access_files": 2,
            "num_outbound_cmds": 1,
            "is_host_login": 1,
            "is_guest_login": 0,
            "count": 70,
            "srv_count": 62,
            "serror_rate": 0.38,
            "srv_serror_rate": 0.33,
            "rerror_rate": 0.22,
            "srv_rerror_rate": 0.17,
            "same_srv_rate": 0.72,
            "diff_srv_rate": 0.28,
            "srv_diff_host_rate": 0.25,
            "dst_host_count": 95,
            "dst_host_srv_count": 80,
            "dst_host_same_srv_rate": 0.68,
            "dst_host_diff_srv_rate": 0.32,
            "dst_host_same_src_port_rate": 0.52,
            "dst_host_srv_diff_host_rate": 0.3,
            "dst_host_serror_rate": 0.28,
            "dst_host_srv_serror_rate": 0.23,
            "dst_host_rerror_rate": 0.14,
            "dst_host_srv_rerror_rate": 0.12,
        }
    }
]

# ============================================================================
# U2R ATTACK SAMPLES (User to Root - Privilege Escalation)
# ============================================================================
u2r_samples = [
    {
        "name": "Privilege Escalation via Buffer Overflow",
        "data": {
            "duration": 120,
            "protocol_type": 0,  # TCP
            "service": 15,  # Shell
            "flag": 0,
            "src_bytes": 2000,
            "dst_bytes": 1800,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 2,  # Urgent data
            "hot": 4,  # Multiple suspicious indicators
            "num_failed_logins": 1,
            "logged_in": 1,  # Already logged in as normal user
            "num_compromised": 2,  # Compromised during attack
            "root_shell": 1,  # ROOT SHELL - Critical indicator
            "su_attempted": 1,  # su command used
            "num_root": 10,  # Multiple root operations
            "num_file_creations": 4,  # Creates files as root
            "num_shells": 3,  # Multiple shells spawned
            "num_access_files": 5,  # Accesses multiple files
            "num_outbound_cmds": 2,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 55,
            "srv_count": 48,
            "serror_rate": 0.18,
            "srv_serror_rate": 0.14,
            "rerror_rate": 0.08,
            "srv_rerror_rate": 0.06,
            "same_srv_rate": 0.82,
            "diff_srv_rate": 0.18,
            "srv_diff_host_rate": 0.12,
            "dst_host_count": 75,
            "dst_host_srv_count": 65,
            "dst_host_same_srv_rate": 0.8,
            "dst_host_diff_srv_rate": 0.2,
            "dst_host_same_src_port_rate": 0.65,
            "dst_host_srv_diff_host_rate": 0.15,
            "dst_host_serror_rate": 0.12,
            "dst_host_srv_serror_rate": 0.1,
            "dst_host_rerror_rate": 0.06,
            "dst_host_srv_rerror_rate": 0.04,
        }
    },
    {
        "name": "Sudo Privilege Escalation",
        "data": {
            "duration": 90,
            "protocol_type": 0,  # TCP
            "service": 15,  # Shell
            "flag": 0,
            "src_bytes": 1600,
            "dst_bytes": 1400,
            "land": 0,
            "wrong_fragment": 0,
            "urgent": 1,
            "hot": 3,
            "num_failed_logins": 2,
            "logged_in": 1,
            "num_compromised": 3,
            "root_shell": 1,  # ROOT SHELL achieved
            "su_attempted": 1,  # Attempted su
            "num_root": 8,  # Root operations
            "num_file_creations": 3,
            "num_shells": 2,
            "num_access_files": 4,
            "num_outbound_cmds": 1,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 50,
            "srv_count": 45,
            "serror_rate": 0.16,
            "srv_serror_rate": 0.12,
            "rerror_rate": 0.07,
            "srv_rerror_rate": 0.05,
            "same_srv_rate": 0.85,
            "diff_srv_rate": 0.15,
            "srv_diff_host_rate": 0.1,
            "dst_host_count": 70,
            "dst_host_srv_count": 62,
            "dst_host_same_srv_rate": 0.82,
            "dst_host_diff_srv_rate": 0.18,
            "dst_host_same_src_port_rate": 0.68,
            "dst_host_srv_diff_host_rate": 0.12,
            "dst_host_serror_rate": 0.1,
            "dst_host_srv_serror_rate": 0.08,
            "dst_host_rerror_rate": 0.05,
            "dst_host_srv_rerror_rate": 0.03,
        }
    },
    {
        "name": "Local Kernel Exploit",
        "data": {
            "duration": 110,
            "protocol_type": 0,  # TCP
            "service": 15,  # Shell
            "flag": 0,
            "src_bytes": 1900,
            "dst_bytes": 1700,
            "land": 0,
            "wrong_fragment": 1,
            "urgent": 1,
            "hot": 5,  # High suspicious activity
            "num_failed_logins": 0,
            "logged_in": 1,
            "num_compromised": 2,
            "root_shell": 1,  # ROOT SHELL
            "su_attempted": 1,
            "num_root": 12,  # Multiple root operations
            "num_file_creations": 4,
            "num_shells": 3,
            "num_access_files": 5,
            "num_outbound_cmds": 2,
            "is_host_login": 0,
            "is_guest_login": 0,
            "count": 60,
            "srv_count": 52,
            "serror_rate": 0.2,
            "srv_serror_rate": 0.16,
            "rerror_rate": 0.09,
            "srv_rerror_rate": 0.07,
            "same_srv_rate": 0.8,
            "diff_srv_rate": 0.2,
            "srv_diff_host_rate": 0.14,
            "dst_host_count": 80,
            "dst_host_srv_count": 70,
            "dst_host_same_srv_rate": 0.78,
            "dst_host_diff_srv_rate": 0.22,
            "dst_host_same_src_port_rate": 0.62,
            "dst_host_srv_diff_host_rate": 0.18,
            "dst_host_serror_rate": 0.14,
            "dst_host_srv_serror_rate": 0.12,
            "dst_host_rerror_rate": 0.07,
            "dst_host_srv_rerror_rate": 0.05,
        }
    }
]

# ============================================================================
# DETECTION FUNCTION
# ============================================================================

def detect_attack(sample_name, sample_data):
    """Send a sample to the detection API and return the result"""
    try:
        response = requests.post(API_URL, json=sample_data, timeout=5)
        response.raise_for_status()
        result = response.json()
        
        return {
            'name': sample_name,
            'success': True,
            'result': result
        }
    except requests.exceptions.RequestException as e:
        return {
            'name': sample_name,
            'success': False,
            'error': str(e)
        }

def print_result(detection_result):
    """Pretty print a detection result"""
    if not detection_result['success']:
        print(f"  ✗ Error: {detection_result['error']}")
        return
    
    result = detection_result['result']
    pred = result.get('prediction_label', 'Unknown')
    conf = result.get('confidence', 0) * 100
    is_attack = "✓ Yes" if result.get('is_attack') else "✗ No"
    
    print(f"  Prediction: {pred}")
    print(f"  Confidence: {conf:.2f}%")
    print(f"  Is Attack: {is_attack}")
    print()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("\n" + "="*80)
    print("AI-NIDS: Multi-Attack Type Detection Test")
    print("="*80 + "\n")
    
    all_results = {
        'Normal': [],
        'Probe': [],
        'R2L': [],
        'U2R': []
    }
    
    # Test Normal Traffic
    print("┌─ NORMAL TRAFFIC DETECTION")
    print("│  Testing legitimate network traffic samples\n")
    for sample in normal_samples:
        print(f"  Testing: {sample['name']}")
        result = detect_attack(sample['name'], sample['data'])
        all_results['Normal'].append(result)
        print_result(result)
    
    # Test Probe Attacks
    print("├─ PROBE ATTACK DETECTION")
    print("│  Testing reconnaissance and port scanning attacks\n")
    for sample in probe_samples:
        print(f"  Testing: {sample['name']}")
        result = detect_attack(sample['name'], sample['data'])
        all_results['Probe'].append(result)
        print_result(result)
    
    # Test R2L Attacks
    print("├─ R2L ATTACK DETECTION (Remote to Local)")
    print("│  Testing unauthorized remote access attempts\n")
    for sample in r2l_samples:
        print(f"  Testing: {sample['name']}")
        result = detect_attack(sample['name'], sample['data'])
        all_results['R2L'].append(result)
        print_result(result)
    
    # Test U2R Attacks
    print("├─ U2R ATTACK DETECTION (User to Root)")
    print("│  Testing privilege escalation attacks\n")
    for sample in u2r_samples:
        print(f"  Testing: {sample['name']}")
        result = detect_attack(sample['name'], sample['data'])
        all_results['U2R'].append(result)
        print_result(result)
    
    # Summary
    print("\n" + "="*80)
    print("DETECTION SUMMARY")
    print("="*80 + "\n")
    
    for attack_type, results in all_results.items():
        successful = sum(1 for r in results if r['success'])
        total = len(results)
        print(f"{attack_type}: {successful}/{total} successful")
        
        if successful > 0:
            attack_count = sum(1 for r in results if r['success'] and r['result'].get('is_attack'))
            print(f"  - Detected as attack: {attack_count}/{successful}")
    
    print("\n" + "="*80)
    print("Test completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*80 + "\n")

if __name__ == '__main__':
    print("\nConnecting to Flask API...")
    print(f"Target: {API_URL}\n")
    time.sleep(1)
    main()
