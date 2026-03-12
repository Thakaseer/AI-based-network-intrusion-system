#!/bin/bash

# Complete AI-NIDS Execution Pipeline
# Runs: Data Load -> Process -> Train -> Test -> Display Results

cd "$(dirname "$0")"

echo ""
echo "============================================================"
echo "  AI Network Intrusion Detection System"
echo "  Complete Execution Pipeline"
echo "============================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "[1/5] Checking dependencies..."
python3 -m pip show pandas &> /dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi
echo "OK: Dependencies ready"

echo ""
echo "[2/5] Executing complete pipeline..."
echo "This will take a few minutes..."
echo ""

python3 execute_pipeline.py
if [ $? -ne 0 ]; then
    echo "Error: Pipeline execution failed"
    exit 1
fi

echo ""
echo "[3/5] Pipeline completed successfully!"
echo ""

while true; do
    echo ""
    echo "============================================================"
    echo "  What would you like to do next?"
    echo "============================================================"
    echo ""
    echo "1. View Results in Web Dashboard (Recommended)"
    echo "2. View Results in Console"
    echo "3. View Results File"
    echo "4. Exit"
    echo ""
    
    read -p "Enter your choice (1-4): " choice
    
    case $choice in
        1)
            echo ""
            echo "Starting web server at http://localhost:5000"
            echo "Press Ctrl+C to stop"
            echo ""
            python3 detect.py --mode api
            ;;
        2)
            echo ""
            echo "Showing test results..."
            echo ""
            python3 detect.py --mode demo
            ;;
        3)
            echo ""
            echo "Opening results file..."
            latest_file=$(ls -t logs/execution_results*.json 2>/dev/null | head -1)
            if [ -n "$latest_file" ]; then
                cat "$latest_file"
            else
                echo "No results file found"
            fi
            ;;
        4)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done
