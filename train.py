#!/usr/bin/env python3
"""
Main training script for AI Network Intrusion Detection System
"""

import os
import sys
import argparse
import logging
from src.model_training import train_pipeline
from src.utils import setup_logging

logger = setup_logging(__name__, 'main.log')

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='AI Network Intrusion Detection System - Training'
    )
    parser.add_argument(
        '--dataset',
        type=str,
        help='Path to dataset file (CSV format)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/models',
        help='Output directory for trained models'
    )
    parser.add_argument(
        '--synthetic',
        action='store_true',
        help='Use synthetic data for training'
    )
    
    args = parser.parse_args()
    
    logger.info("Starting AI-NIDS Training Pipeline")
    logger.info(f"Dataset: {args.dataset or 'Synthetic'}")
    logger.info(f"Output: {args.output}")
    
    try:
        trainer, processor, scaler = train_pipeline(args.dataset, args.output)
        logger.info("Training completed successfully")
        print("\n✓ Training completed successfully!")
        print(f"✓ Best model: {trainer.best_model_name}")
        print(f"✓ Models saved to: {args.output}")
    
    except Exception as e:
        logger.error(f"Training failed: {e}")
        print(f"\n✗ Training failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
    