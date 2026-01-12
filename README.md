# asl-hand
Digital Electronics Final Project Kiana Lee


## Project Overview
The ASL Hand Project is an ongoing engineering and research project that explores the design of a robotic hand capable of producing American Sign Language (ASL) fingerspelling. The project is split into two parts: a joint detection based on MediaPipe to identify ASL letters and produce a text output, and then the physical/mechanical hand, designed with servos to move individual fingers.

  At its current stage, the project focuses on:
```
    System design and planning
    Servo control experiments
    Power, wiring, and communication testing
    Software development and troubleshooting
```
The physical robotic hand has **not yet been fully assembled**, and this repository documents the _design process, experimentation_, and _preparation_ leading up to a full build.

## Project Objectives
```
Design a robotic hand system capable of ASL fingerspelling
Develop Python-based control logic for multi-servo coordination
Test and validate servo drivers, power delivery, and timing
Document all engineering decisions in a reproducible manner
Prepare a system architecture that can be physically assembled in future work
```

American Sign Language is a complete visual language that is often underrepresented in engineering applications. This project aims to explore how robotic systems could support ASL education and accessibility through careful, respectful design.

As a Deaf/Hard-of-Hearing student, this project is motivated by both **technical curiosity and personal experience** with accessibility in STEM. 

## Digital Notebook (Primary Documentation)

This project is supported by a detailed Digital Notebook, which serves as the **official technical record**. 
The Digital Notebook includes the following:
```
Design planning and system architecture
Software testing and troubleshooting steps
Servo control experiments and parameters tested
Power and wiring analysis
Calibration attempts and limitations
Links to external resources used for decision-making
Screenshots, diagrams, graphs, and code excerpts
```
The notebook is structured so that all work can be reviewed, followed, and replicated by others. 

You can access the notebook with the following link: 

## System Design Overview

The system is designed as a modular robotics platform consisting of:
* A tendon-driven robotic hand (future physical build)
* Multiple servo motors for finger articulation
* A servo drive board for stable PWM control
* A single-board computer or microcontroller for logic and coordination
* Python-based software for command sequencing and timing

At this stage, emphasis is placed on validating control logic, power constraints, and communication, prior to commiting to a final mechanical assembly.
## CAD Selection and Hand Design

### Open Source-CAD Selection
Rather than designing a robotic hand entirely from scratch, this project uses the Robot Nano Hand as a foundational open-source CAD model.

Robot Nano Hand
https://robotnanohand.com/

This decision was made to:
* Reduce development time
* Focus effort on control systems, actuation, and accessibility
* Build upon a proven mechanical design
* Follow real-world engineering practices using open-source hardware

Using an existing design allowed the project to move more quickly into testing, modification, and evaluation, rather than reinventing a complex mechanical system.

https://github.com/user-attachments/assets/eff40282-3cfc-4599-8152-4d10dabdfc5d

### Evaluation of the NANO Hand Design
The Nano Hand was evaluated specifically for ASL fingerspelling, rather than general grasping.

Identified strengths:
* Compact form factor
* Tendon-driven finger actuation
* Modular finger structure
* Clear servo-to-tendon mapping

Identified limitations for ASL:
* Limited thumb opposition
* Finger joint coupling reduces fine articulation
* No wrist articulation
* Not originally designed for linguistic hand shapes

These limitations informed later planning and future modification goals.

### Modifications for ASL Use

While the base CAD model is open-source, the following adaptations were planned or explored:
* Adjusting finger rest positions to better match ASL neutral pose
* Re-tensioning tendons for consistent letter formation
* Evaluating alternative thumb configurations
* Considering additional degrees of freedom for the thumb
* Exploring wrist articulation as a future extension, via a Spherical Parallel Manipulator
<img width="189" height="267" alt="image" src="https://github.com/user-attachments/assets/a667db2e-e598-4e83-b046-6b4622a8caa9" />

### Future CAD Work

Planned future CAD work includes:
* Minor geometry changes to improve ASL finger spacing
* Custom mounts for selected servos
* Tendon routing refinements
* Optional wrist or forearm extension


Not all modifications have been implemented yet; this repository documents the design evaluation and planning phase.

## Component Selection

### Servo Selection

Servo motors are used to actuate individual fingers via a tendon-driven mechanism. Selection criteria included:
* Physical size (micro servos for compact design)
* Torque sufficient for finger flexion
* Compatibility with standard PWM control
* Availability of documentation and testing libraries

![IMG_0563](https://github.com/user-attachments/assets/786905e5-466c-42c1-ab92-d7e924efadf6)
![IMG_0624](https://github.com/user-attachments/assets/6372a694-0dcf-42fd-9262-0f860abca99f)



Multiple servo models were researched and tested to evaluate consistency, jitter, and power draw.

### Servo Driver Selection

To support multi-servo coordination, a PCA9685 16-channel PWM servo driver was selected. This board was chosen because it:
* Allows precise PWM timing
* Reduces load on the main controller
* Supports multiple servos simultaneously
* Enables consistent 50–60 Hz servo control

### Controller Selection
Python was selected as the primary programming language due to:
* Strong library support
* Readability and maintainability
* Compatibility with Raspberry Pi-based systems
* Ease of rapid testing and debugging

This allows the project to scale from simple servo tests to more complex sequencing logic in future iterations.

## Software Development

The software component of this project focuses on:
* Initializing and addressing multiple servo channels
* Mapping finger positions to servo angles
* Sequencing movements for ASL fingerspelling
* Managing timing between letter transitions
* Troubleshooting communication and power issues

The software is developed incrementally, with isolated tests for each subsystem before integration.
![Flowchart for Code](https://github.com/user-attachments/assets/e8d0f103-faf9-44c9-be53-3b4039a0f95c)


## Testing and Troubleshooting

Extensive testing was conducted to validate:
* Servo response consistency
* PWM timing accuracy
* Power stability under load
* I2C communication reliability
* Software logic correctness

Each test iteration is documented in the Digital Notebook, including parameters tested, observed behavior, and resulting design decisions.


