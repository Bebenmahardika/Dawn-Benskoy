#!/bin/bash

# Function to display loading animation for a given duration
loading_animation() {
    local duration=$1
    local elapsed=0
    while [ $elapsed -lt $duration ]; do
        for i in / - \\ \|; do
            echo -ne "\r$i"
            sleep 0.1
            elapsed=$((elapsed + 1))
            if [ $elapsed -ge $duration ]; then
                break
            fi
        done
    done
    echo -ne "\rDone!          \n"
}

# Display a message before cloning the repository
echo "SABAR NGAB"
loading_animation 50  # Load animation for 5 seconds

# Clone the repository
git clone https://github.com/Bebenmahardika/Dawn-auto

# Display a message before changing directory
echo "MASUK KE DIRECTORYNYA"
loading_animation 50  # Load animation for 5 seconds

# Change to the repository directory
cd Dawn-auto

# Display a message before running the Python script
echo "GASS URUTIN AJA SESUAI NOMOR INPUT SATU2 TUTOR ADA DI GITHUB"
loading_animation 7  # Load animation for 5 seconds

# Run the Python script
python3 benskoy.py
