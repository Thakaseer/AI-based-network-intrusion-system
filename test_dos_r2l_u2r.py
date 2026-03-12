"""
DoS Attack Detection with Different R2L and U2R Samples
Focuses on detecting Denial of Service attacks
"""

import sys
sys.path.insert(0, '.')

from src.intrusion_detector import create_detector
from datetime import datetime
import json

# Initialize detector
print("\n" + "="*80)
print("AI-NIDS: DoS Attack Detection with R2L & U2R Variants")
print("="*80 + "\n")

print("[*] Initializing detector...")
detector = create_detector()
print("[+] Detector initialized\n")

# ============================================================================
# DOS ATTACK SAMPLES (Main Focus)
# ============================================================================
dos_samples = [
    {
        "name": "SYN Flood Attack",
        "data": {
            "duration": 1, "protocol_type": 0, "service": 0, "flag": 0,
            "src_bytes": 40, "dst_bytes": 0, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 511, "srv_count": 500, "serror_rate": 1.0, "srv_serror_rate": 1.0,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.99,
            "diff_srv_rate": 0.01, "srv_diff_host_rate": 0.0, "dst_host_count": 255,
            "dst_host_srv_count": 240, "dst_host_same_srv_rate": 0.99, "dst_host_diff_srv_rate": 0.01,
            "dst_host_same_src_port_rate": 1.0, "dst_host_srv_diff_host_rate": 0.0,
            "dst_host_serror_rate": 1.0, "dst_host_srv_serror_rate": 1.0,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "UDP Flood Attack",
        "data": {
            "duration": 2, "protocol_type": 1, "service": 0, "flag": 0,
            "src_bytes": 50, "dst_bytes": 10, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 480, "srv_count": 470, "serror_rate": 0.95, "srv_serror_rate": 0.94,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.98,
            "diff_srv_rate": 0.02, "srv_diff_host_rate": 0.01, "dst_host_count": 250,
            "dst_host_srv_count": 245, "dst_host_same_srv_rate": 0.98, "dst_host_diff_srv_rate": 0.02,
            "dst_host_same_src_port_rate": 0.99, "dst_host_srv_diff_host_rate": 0.01,
            "dst_host_serror_rate": 0.95, "dst_host_srv_serror_rate": 0.94,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "ICMP Ping Flood (Smurf Attack)",
        "data": {
            "duration": 3, "protocol_type": 2, "service": 0, "flag": 0,
            "src_bytes": 60, "dst_bytes": 30, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 500, "srv_count": 490, "serror_rate": 0.98, "srv_serror_rate": 0.97,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 0.99,
            "diff_srv_rate": 0.01, "srv_diff_host_rate": 0.0, "dst_host_count": 255,
            "dst_host_srv_count": 250, "dst_host_same_srv_rate": 0.99, "dst_host_diff_srv_rate": 0.01,
            "dst_host_same_src_port_rate": 1.0, "dst_host_srv_diff_host_rate": 0.0,
            "dst_host_serror_rate": 0.98, "dst_host_srv_serror_rate": 0.97,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    },
    {
        "name": "Application Level DoS (HTTP)",
        "data": {
            "duration": 1, "protocol_type": 0, "service": 80, "flag": 0,
            "src_bytes": 100, "dst_bytes": 0, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 2, "num_failed_logins": 0, "logged_in": 0,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 0, "num_access_files": 0,
            "num_outbound_cmds": 0, "is_host_login": 0, "is_guest_login": 0,
            "count": 450, "srv_count": 440, "serror_rate": 1.0, "srv_serror_rate": 1.0,
            "rerror_rate": 0.0, "srv_rerror_rate": 0.0, "same_srv_rate": 1.0,
            "diff_srv_rate": 0.0, "srv_diff_host_rate": 0.0, "dst_host_count": 240,
            "dst_host_srv_count": 235, "dst_host_same_srv_rate": 1.0, "dst_host_diff_srv_rate": 0.0,
            "dst_host_same_src_port_rate": 0.95, "dst_host_srv_diff_host_rate": 0.0,
            "dst_host_serror_rate": 1.0, "dst_host_srv_serror_rate": 1.0,
            "dst_host_rerror_rate": 0.0, "dst_host_srv_rerror_rate": 0.0,
        }
    }
]

# ============================================================================
# DIFFERENT R2L ATTACK SAMPLES
# ============================================================================
r2l_samples = [
    {
        "name": "R2L: Guess Password Attack",
        "data": {
            "duration": 300, "protocol_type": 0, "service": 23, "flag": 0,
            "src_bytes": 3000, "dst_bytes": 2800, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 12, "logged_in": 1,
            "num_compromised": 0, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 1, "num_shells": 0, "num_access_files": 1,
            "num_outbound_cmds": 0, "is_host_login": 1, "is_guest_login": 0,
            "count": 80, "srv_count": 72, "serror_rate": 0.4, "srv_serror_rate": 0.35,
            "rerror_rate": 0.25, "srv_rerror_rate": 0.2, "same_srv_rate": 0.7,
            "diff_srv_rate": 0.3, "srv_diff_host_rate": 0.25, "dst_host_count": 110,
            "dst_host_srv_count": 95, "dst_host_same_srv_rate": 0.65, "dst_host_diff_srv_rate": 0.35,
            "dst_host_same_src_port_rate": 0.45, "dst_host_srv_diff_host_rate": 0.35,
            "dst_host_serror_rate": 0.3, "dst_host_srv_serror_rate": 0.25,
            "dst_host_rerror_rate": 0.15, "dst_host_srv_rerror_rate": 0.12,
        }
    },
    {
        "name": "R2L: Dictionary Attack (SSH)",
        "data": {
            "duration": 250, "protocol_type": 0, "service": 22, "flag": 0,
            "src_bytes": 2200, "dst_bytes": 2500, "land": 0, "wrong_fragment": 0,
            "urgent": 0, "hot": 0, "num_failed_logins": 8, "logged_in": 1,
            "num_compromised": 1, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 0, "num_shells": 1, "num_access_files": 1,
            "num_outbound_cmds": 0, "is_host_login": 1, "is_guest_login": 0,
            "count": 70, "srv_count": 65, "serror_rate": 0.38, "srv_serror_rate": 0.33,
            "rerror_rate": 0.22, "srv_rerror_rate": 0.18, "same_srv_rate": 0.75,
            "diff_srv_rate": 0.25, "srv_diff_host_rate": 0.2, "dst_host_count": 100,
            "dst_host_srv_count": 88, "dst_host_same_srv_rate": 0.7, "dst_host_diff_srv_rate": 0.3,
            "dst_host_same_src_port_rate": 0.5, "dst_host_srv_diff_host_rate": 0.28,
            "dst_host_serror_rate": 0.28, "dst_host_srv_serror_rate": 0.23,
            "dst_host_rerror_rate": 0.13, "dst_host_srv_rerror_rate": 0.1,
        }
    },
    {
        "name": "R2L: rsh/rlogin Exploit",
        "data": {
            "duration": 180, "protocol_type": 0, "service": 514, "flag": 0,
            "src_bytes": 1800, "dst_bytes": 1600, "land": 0, "wrong_fragment": 0,
            "urgent": 1, "hot": 1, "num_failed_logins": 3, "logged_in": 1,
            "num_compromised": 1, "root_shell": 0, "su_attempted": 0, "num_root": 0,
            "num_file_creations": 2, "num_shells": 1, "num_access_files": 2,
            "num_outbound_cmds": 1, "is_host_login": 1, "is_guest_login": 0,
            "count": 60, "srv_count": 54, "serror_rate": 0.35, "srv_serror_rate": 0.3,
            "rerror_rate": 0.2, "srv_rerror_rate": 0.15, "same_srv_rate": 0.8,
            "diff_srv_rate": 0.2, "srv_diff_host_rate": 0.15, "dst_host_count": 90,
            "dst_host_srv_count": 80, "dst_host_same_srv_rate": 0.75, "dst_host_diff_srv_rate": 0.25,
            "dst_host_same_src_port_rate": 0.55, "dst_host_srv_diff_host_rate": 0.22,
            "dst_host_serror_rate": 0.25, "dst_host_srv_serror_rate": 0.2,
            "dst_host_rerror_rate": 0.12, "dst_host_srv_rerror_rate": 0.09,
        }
    }
]

# ============================================================================
# DIFFERENT U2R ATTACK SAMPLES
# ============================================================================
u2r_samples = [
    {
        "name": "U2R: Buffer Overflow (Apache)",
        "data": {
            "duration": 100, "protocol_type": 0, "service": 80, "flag": 0,
            "src_bytes": 1500, "dst_bytes": 1200, "land": 0, "wrong_fragment": 1,
            "urgent": 3, "hot": 5, "num_failed_logins": 0, "logged_in": 1,
            "num_compromised": 2, "root_shell": 1, "su_attempted": 1, "num_root": 15,
            "num_file_creations": 5, "num_shells": 4, "num_access_files": 6,
            "num_outbound_cmds": 3, "is_host_login": 0, "is_guest_login": 0,
            "count": 50, "srv_count": 45, "serror_rate": 0.2, "srv_serror_rate": 0.15,
            "rerror_rate": 0.1, "srv_rerror_rate": 0.08, "same_srv_rate": 0.8,
            "diff_srv_rate": 0.2, "srv_diff_host_rate": 0.1, "dst_host_count": 70,
            "dst_host_srv_count": 62, "dst_host_same_srv_rate": 0.82, "dst_host_diff_srv_rate": 0.18,
            "dst_host_same_src_port_rate": 0.7, "dst_host_srv_diff_host_rate": 0.12,
            "dst_host_serror_rate": 0.15, "dst_host_srv_serror_rate": 0.12,
            "dst_host_rerror_rate": 0.08, "dst_host_srv_rerror_rate": 0.05,
        }
    },
    {
        "name": "U2R: Kernel Privilege Escalation",
        "data": {
            "duration": 80, "protocol_type": 0, "service": 15, "flag": 0,
            "src_bytes": 1400, "dst_bytes": 1300, "land": 0, "wrong_fragment": 2,
            "urgent": 2, "hot": 4, "num_failed_logins": 1, "logged_in": 1,
            "num_compromised": 3, "root_shell": 1, "su_attempted": 1, "num_root": 20,
            "num_file_creations": 6, "num_shells": 5, "num_access_files": 7,
            "num_outbound_cmds": 2, "is_host_login": 0, "is_guest_login": 0,
            "count": 45, "srv_count": 42, "serror_rate": 0.18, "srv_serror_rate": 0.14,
            "rerror_rate": 0.09, "srv_rerror_rate": 0.07, "same_srv_rate": 0.85,
            "diff_srv_rate": 0.15, "srv_diff_host_rate": 0.08, "dst_host_count": 65,
            "dst_host_srv_count": 58, "dst_host_same_srv_rate": 0.85, "dst_host_diff_srv_rate": 0.15,
            "dst_host_same_src_port_rate": 0.75, "dst_host_srv_diff_host_rate": 0.1,
            "dst_host_serror_rate": 0.12, "dst_host_srv_serror_rate": 0.09,
            "dst_host_rerror_rate": 0.06, "dst_host_srv_rerror_rate": 0.04,
        }
    },
    {
        "name": "U2R: Local Exploit (sendmail/xterm)",
        "data": {
            "duration": 120, "protocol_type": 0, "service": 25, "flag": 0,
            "src_bytes": 1700, "dst_bytes": 1500, "land": 0, "wrong_fragment": 1,
            "urgent": 1, "hot": 3, "num_failed_logins": 0, "logged_in": 1,
            "num_compromised": 2, "root_shell": 1, "su_attempted": 1, "num_root": 12,
            "num_file_creations": 4, "num_shells": 3, "num_access_files": 5,
            "num_outbound_cmds": 2, "is_host_login": 0, "is_guest_login": 0,
            "count": 55, "srv_count": 50, "serror_rate": 0.22, "srv_serror_rate": 0.18,
            "rerror_rate": 0.11, "srv_rerror_rate": 0.09, "same_srv_rate": 0.78,
            "diff_srv_rate": 0.22, "srv_diff_host_rate": 0.15, "dst_host_count": 75,
            "dst_host_srv_count": 68, "dst_host_same_srv_rate": 0.8, "dst_host_diff_srv_rate": 0.2,
            "dst_host_same_src_port_rate": 0.65, "dst_host_srv_diff_host_rate": 0.15,
            "dst_host_serror_rate": 0.18, "dst_host_srv_serror_rate": 0.14,
            "dst_host_rerror_rate": 0.08, "dst_host_srv_rerror_rate": 0.06,
        }
    }
]

# ============================================================================
# TEST FUNCTION
# ============================================================================

def test_samples(attack_type, samples):
    """Test a list of samples"""
    print(f"{'─'*80}")
    print(f"[*] {attack_type.upper()}")
    print(f"{'─'*80}\n")
    
    results = []
    for i, sample in enumerate(samples, 1):
        result = detector.detect(sample['data'])
        results.append(result)
        
        pred = result.get('prediction_label', 'Unknown')
        conf = result.get('confidence', 0) * 100
        is_attack = "[+] ATTACK" if result.get('is_attack') else "[-] NORMAL"
        
        print(f"  [{i}] {sample['name']:<50}")
        print(f"      → {is_attack:<12} | Type: {pred:<12} | Confidence: {conf:.1f}%\n")
    
    return results

# ============================================================================
# RUN TESTS
# ============================================================================

print("\n" + "="*80)
print("PHASE 1: DoS ATTACK DETECTION (Focus Area)")
print("="*80 + "\n")
dos_results = test_samples('DoS Attacks', dos_samples)

print("\n" + "="*80)
print("PHASE 2: R2L ATTACK SAMPLES (Remote to Local)")
print("="*80 + "\n")
r2l_results = test_samples('R2L Attacks', r2l_samples)

print("\n" + "="*80)
print("PHASE 3: U2R ATTACK SAMPLES (User to Root Privilege Escalation)")
print("="*80 + "\n")
u2r_results = test_samples('U2R Attacks', u2r_samples)

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

print("\n" + "="*80)
print("\n[*] DETECTION SUMMARY & STATISTICS")
print("="*80 + "\n")

def count_attacks(results):
    return sum(1 for r in results if r.get('is_attack'))

def avg_confidence(results):
    confs = [r.get('confidence', 0) for r in results]
    return sum(confs) / len(confs) if confs else 0

print(f"DoS Attacks:")
print(f"  [+] Detected: {count_attacks(dos_results)}/{len(dos_results)}")
print(f"  Avg Confidence: {avg_confidence(dos_results)*100:.1f}%\n")

print(f"R2L Attacks (Remote to Local):")
print(f"  [+] Detected: {count_attacks(r2l_results)}/{len(r2l_results)}")
print(f"  Avg Confidence: {avg_confidence(r2l_results)*100:.1f}%\n")

print(f"U2R Attacks (User to Root):")
print(f"  [+] Detected: {count_attacks(u2r_results)}/{len(u2r_results)}")
print(f"  Avg Confidence: {avg_confidence(u2r_results)*100:.1f}%\n")

total_attacks = count_attacks(dos_results) + count_attacks(r2l_results) + count_attacks(u2r_results)
total_samples = len(dos_results) + len(r2l_results) + len(u2r_results)

print(f"TOTAL ATTACKS DETECTED: {total_attacks}/{total_samples} ({total_attacks*100//total_samples}%)")
print("\n" + "="*80)
print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*80 + "\n")
