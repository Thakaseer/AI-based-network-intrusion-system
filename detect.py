#!/usr/bin/env python3
"""
Main detection script for AI Network Intrusion Detection System
"""

import os
import sys
import argparse
import time
from src.intrusion_detector import create_detector
from src.network_sniffer import create_sniffer
from src.utils import setup_logging
import config

logger = setup_logging(__name__, 'detection.log')

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='AI Network Intrusion Detection System - Detection'
    )
    parser.add_argument(
        '--model',
        type=str,
        help='Path to trained model'
    )
    parser.add_argument(
        '--scaler',
        type=str,
        help='Path to feature scaler'
    )
    parser.add_argument(
        '--interface',
        type=str,
        default=config.NETWORK_INTERFACE,
        help='Network interface to monitor'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=0,
        help='Number of packets to capture (0 = infinite)'
    )
    parser.add_argument(
        '--mode',
        type=str,
        choices=['sniffer', 'api', 'demo'],
        default='demo',
        help='Detection mode'
    )
    
    args = parser.parse_args()
    
    logger.info("Starting AI-NIDS Detection Engine")
    logger.info(f"Mode: {args.mode}")
    
    try:
        if args.mode == 'demo':
            run_demo(args.model, args.scaler)
        elif args.mode == 'sniffer':
            run_sniffer(args.model, args.scaler, args.interface, args.count)
        elif args.mode == 'api':
            run_api()
    
    except KeyboardInterrupt:
        logger.info("Detection stopped by user")
        print("\n✓ Detection stopped")
    except Exception as e:
        logger.error(f"Detection failed: {e}")
        print(f"\n✗ Detection failed: {e}")
        sys.exit(1)

def run_demo(model_path=None, scaler_path=None):
    """Run demo detection"""
    print("\n" + "="*60)
    print("AI-NIDS Demo Detection")
    print("="*60)
    
    detector = create_detector(model_path, scaler_path)
    
    # Create sample packets
    sample_packets = [
        {
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
        },
        {
            'duration': 500,
            'protocol_type': 1,
            'service': 10,
            'flag': 3,
            'src_bytes': 5000,
            'dst_bytes': 10000,
            'land': 0,
            'wrong_fragment': 1,
            'urgent': 1,
            'hot': 2,
            'num_failed_logins': 5,
            'logged_in': 0,
            'num_compromised': 1,
            'root_shell': 1,
            'su_attempted': 1,
            'num_root': 2,
            'num_file_creations': 1,
            'num_shells': 1,
            'num_access_files': 1,
            'num_outbound_cmds': 1,
            'is_host_login': 0,
            'is_guest_login': 0,
            'count': 500,
            'srv_count': 200,
            'serror_rate': 0.8,
            'srv_serror_rate': 0.7,
            'rerror_rate': 0.5,
            'srv_rerror_rate': 0.4,
            'same_srv_rate': 0.2,
            'diff_srv_rate': 0.8,
            'srv_diff_host_rate': 0.9,
            'dst_host_count': 50,
            'dst_host_srv_count': 20,
            'dst_host_same_srv_rate': 0.1,
            'dst_host_diff_srv_rate': 0.9,
            'dst_host_same_src_port_rate': 0.05,
            'dst_host_srv_diff_host_rate': 0.95,
            'dst_host_serror_rate': 0.8,
            'dst_host_srv_serror_rate': 0.75,
            'dst_host_rerror_rate': 0.6,
            'dst_host_srv_rerror_rate': 0.5,
        }
    ]
    
    print("\nDetecting intrusions in sample packets...\n")
    
    for i, packet in enumerate(sample_packets, 1):
        result = detector.detect(packet)
        if result:
            print(f"Packet {i}:")
            print(f"  Prediction: {result['prediction_label']}")
            print(f"  Confidence: {result['confidence']*100:.2f}%")
            print(f"  Is Attack: {result['is_attack']}")
            print(f"  Alert: {result['alert']}")
            print()
    
    # Print statistics
    stats = detector.get_detection_statistics()
    if stats:
        print("\nDetection Statistics:")
        print(f"  Total Packets: {stats['total_packets']}")
        print(f"  Total Attacks: {stats['total_attacks']}")
        print(f"  Detection Rate: {stats['detection_rate']:.2f}%")
        print(f"  Average Confidence: {stats['average_confidence']*100:.2f}%")
        print()

def run_sniffer(model_path=None, scaler_path=None, interface=None, count=0):
    """Run packet sniffer with detection"""
    print("\n" + "="*60)
    print("AI-NIDS Packet Sniffer")
    print("="*60)
    print(f"Interface: {interface}")
    print(f"Packet Count: {count if count > 0 else 'Infinite'}")
    print("="*60 + "\n")
    
    detector = create_detector(model_path, scaler_path)
    sniffer = create_sniffer(interface)
    
    def packet_callback(packet):
        if packet:
            result = detector.detect(packet)
            if result and result['alert']:
                print(f"[ALERT] {result['prediction_label']} - Confidence: {result['confidence']*100:.2f}%")
    
    try:
        sniffer.start_sniffing(packet_count=count, callback=packet_callback)
    except PermissionError:
        print("Error: Administrator privileges required for packet capture")
        sys.exit(1)

def run_api():
    """Run Flask API server"""
    print("\n" + "="*60)
    print("AI-NIDS Web API")
    print("="*60)
    print(f"Starting server at http://{config.FLASK_HOST}:{config.FLASK_PORT}")
    print("="*60 + "\n")
    
    from web.app import app
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.FLASK_DEBUG)

if __name__ == '__main__':
    main()
