# AI Systems Project -- Edge AI, Quantum AI & IoT


A practical + theoretical project exploring the fundamentals of **Edge
AI**, **Quantum AI**, and smart agriculture using **AI-driven IoT**.
Includes conceptual essays, prototype implementation details, and system
design diagrams.

------------------------------------------------------------------------

#  Project Structure

    AI-Systems-Project/
    │
    ├── /theory
    │   ├── edge_ai_analysis.md
    │   ├── quantum_ai_analysis.md
    │
    ├── /edge_ai_prototype
    │   ├── model_training.ipynb
    │   ├── recycle_classifier.tflite
    │   └── pi_inference_script.py
    │
    ├── /iot_agriculture
    │   ├── sensors_list.md
    │   ├── ai_model_description.md
    │   └── data_flow_diagram.png
    │
    └── README.md

------------------------------------------------------------------------

#  Part 1 --- Theoretical Analysis

## **1. Edge AI --- Latency & Privacy Advantages**

###  Overview

Edge AI performs inference **directly on devices**, reducing reliance on
cloud servers.

###  Why It Reduces Latency

-   No round-trip to remote cloud\
-   Real-time processing (milliseconds)\
-   Essential for robotics, drones, cars

###  Why It Enhances Privacy

-   Data stays on the device\
-   Lower exposure risk\
-   Easier compliance with data regulations

### **Real-World Example: Autonomous Drones**

-   On-device computation for obstacle detection\
-   No reliance on internet connectivity\
-   Raw video never leaves the drone

------------------------------------------------------------------------

###  **Cloud AI vs Edge AI Comparison Table**

  Feature          Cloud AI                   Edge AI
  ---------------- -------------------------- -----------------------------
  Latency          High (network dependent)   Very Low (local processing)
  Privacy          Data uploaded externally   Data stays on-device
  Connectivity     Requires stable network    Works offline
  Best Use Cases   Large-scale analytics      Real-time decisions

------------------------------------------------------------------------

## **2. Quantum AI vs Classical AI in Optimization**

###  Key Differences

  ------------------------------------------------------------------------
  Aspect           Classical AI                  Quantum AI
  ---------------- ----------------------------- -------------------------
  Computation      Bits (0/1)                    Qubits (superposition +
  Basis                                          entanglement)

  Optimization     Slower for large problems     Faster for combinatorial
  Speed                                          problems

  Scalability      Limited                       Exponential potential

  Solution Quality Approximate                   Near-optimal

  Best Fit         Everyday ML tasks             Complex optimization
  ------------------------------------------------------------------------

###  Industries That Benefit

-   **Finance** → Portfolio optimization\
-   **Logistics** → Route planning\
-   **Pharmaceuticals** → Molecular simulation\
-   **Energy** → Smart grid optimization\
-   **Manufacturing** → Scheduling & workflow optimization

------------------------------------------------------------------------

#  Part 2 --- Practical Implementation

## **Task 1: Edge AI Prototype (TensorFlow Lite)**

A lightweight image classifier deployed to a **Raspberry Pi** using
**TensorFlow Lite**.

### Objective

-   Train a small model\
-   Convert to `.tflite`\
-   Run in real-time on an edge device

###  Model Performance

-   **Training accuracy:** 80--90%\
-   **Validation accuracy:** 70--85%\
-   **Inference speed:** *tens of ms per frame on Raspberry Pi 4*

------------------------------------------------------------------------

###  Deployment Steps

    1. Install TensorFlow Lite on Raspberry Pi
    2. Transfer recycle_classifier.tflite
    3. Connect Pi Camera or USB webcam
    4. Use inference script to classify frames
    5. Display real-time results

###  Edge AI Benefits

-   Near-zero latency\
-   Local privacy protection\
-   Operates offline\
-   Low energy usage

------------------------------------------------------------------------

## **Task 2: AI-Driven IoT Agriculture System**

An IoT-based smart farming system for predicting crop yield and
automating decisions.

###  Required Sensors

  Sensor            Purpose
  ----------------- ----------------------
  Soil moisture     Water levels
  Temperature       Ambient & soil temp
  Humidity          Air moisture
  Light intensity   Sunlight exposure
  pH level          Soil acidity
  NPK sensor        Nutrient levels
  Weather station   Wind, rainfall, etc.

------------------------------------------------------------------------

###  AI Model

-   **Random Forest Regressor**, **Gradient Boosted Trees**, or
    **LSTM**\
-   Predicts crop yield and suggests actions\
-   Inputs: sensor data, weather, historical yields

------------------------------------------------------------------------

#  System Architecture Diagram

    +---------------------+
    |   IoT Sensors       |
    | (Moisture, Temp...) |
    +----------+----------+
               |
               v
    +---------------------+
    | IoT Gateway / Edge  |
    |   (Raspberry Pi)    |
    +----------+----------+
               |
               v
    +---------------------+
    | Data Preprocessing  |
    | Normalization, etc. |
    +----------+----------+
               |
               v
    +---------------------+
    |   AI Prediction     |
    | (Crop Yield Model)  |
    +----------+----------+
               |
               v
    +-----------------------------+
    | Dashboard / Mobile App      |
    | → Recommendations for farms |
    +-----------------------------+
               |
               v
    +-----------------------------+
    | Automated Actuators         |
    | (Irrigation, Fertilizers)   |
    +-----------------------------+

------------------------------------------------------------------------

#  License

Educational & research use only.
