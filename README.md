# OpenCV & Computer Vision for Robotics 🤖

### A Practical, Project-Based Learning Roadmap

**Python | OpenCV | NumPy | Computer Vision | Deep Learning | ROS 2 Jazzy | Robotics**

Welcome to my OpenCV and Computer Vision learning repository!

This repository documents my journey of learning **Computer Vision from the fundamentals to advanced robotics applications**, with a focus on practical implementations, real-world use cases, and integration with ROS 2.

The goal is to build a strong foundation in computer vision and apply these concepts to **autonomous mobile robots, robotic perception, object detection, tracking, localization, and navigation**.

As I progress through the roadmap, I will continuously update this repository with study notes, Python implementations, experiments, troubleshooting guides, and projects.

> **Repository Status:** 🚧 Work in Progress — Updated as I learn and implement new concepts.

---

## 🎯 Learning Objectives

By completing this roadmap, I aim to:

- Understand computer vision fundamentals and image processing.
- Develop practical skills in Python, NumPy, and OpenCV.
- Work with USB cameras and real-time video streams.
- Implement object detection, tracking, and feature extraction.
- Understand camera calibration and 3D vision.
- Explore deep learning-based computer vision using YOLO and PyTorch.
- Integrate computer vision algorithms with ROS 2 Jazzy.
- Build vision-based robotic perception and control systems.
- Explore visual odometry, visual SLAM, and sensor fusion.
- Develop and document portfolio-ready robotics projects.

---

## 🛠️ Development Environment

| Component | Technology |
|---|---|
| Operating System | Ubuntu 24.04 LTS |
| Programming Language | Python 3.12 |
| IDE | Visual Studio Code |
| Computer Vision | OpenCV |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Deep Learning | PyTorch, YOLO |
| Robotics Middleware | ROS 2 Jazzy |
| Simulation | Gazebo |
| Robot Visualization | RViz2 |
| Camera | USB Camera |
| Version Control | Git & GitHub |

### Hardware

**Development Laptop**
- Processor: AMD Ryzen 5 5500U
- RAM: 14 GiB
- GPU: AMD Radeon Integrated Graphics
- OS: Ubuntu 24.04 LTS

**Robotics Platform**
- Raspberry Pi 4
- ROS 2 Jazzy
- Differential-drive mobile robot
- USB camera for computer vision experiments

---

# 📚 Complete Learning Roadmap

The roadmap is divided into six stages, progressing from image processing fundamentals to complete robotics perception systems.

## Stage 1 — Python, NumPy & OpenCV Fundamentals

**Lessons 1–6 | Beginner**

| Lesson | Topic |
|---|---|
| 01 | [Introduction to Computer Vision and OpenCV](opencv-fundamentals/lesson_01/README.md) |
| 02 | NumPy for Computer Vision and Pixel Manipulation |
| 03 | Image Operations and Transformations |
| 04 | Color Spaces, Thresholding and Masking |
| 05 | Image Filtering and Morphological Operations |
| 06 | Edge Detection and Image Gradients |

**Practical Implementations**
- Reading and displaying images
- USB camera video capture
- Image resizing, cropping and rotation
- Grayscale conversion
- HSV-based color detection
- Image filtering and edge detection

**Stage Project:** Real-Time Color-Based Object Detector

---

## Stage 2 — Classical Robot Perception

**Lessons 7–11 | Beginner to Intermediate**

| Lesson | Topic |
|---|---|
| 07 | Contours, Shape Detection and Object Localization |
| 08 | Vision-Based Line Following |
| 09 | Feature Detection and Matching |
| 10 | Motion Detection and Background Subtraction |
| 11 | Optical Flow and Object Tracking |

**Practical Implementations**
- Contour detection and bounding boxes
- Shape recognition
- Line detection and steering error calculation
- ORB and SIFT feature extraction
- Motion detection
- Object tracking in video

**Stage Projects:**
- Vision-Based Line Following
- Real-Time Object Tracking

---

## Stage 3 — Camera Geometry & 3D Vision

**Lessons 12–17 | Intermediate**

| Lesson | Topic |
|---|---|
| 12 | Camera Models and Coordinate Systems |
| 13 | Camera Calibration and Lens Distortion |
| 14 | Perspective Transformations and Homography |
| 15 | ArUco Marker Detection and Pose Estimation |
| 16 | Stereo Vision and Depth Estimation |
| 17 | Introduction to Visual Odometry |

**Practical Implementations**
- Chessboard camera calibration
- Camera intrinsic and extrinsic parameters
- Perspective correction
- ArUco marker detection
- Marker pose estimation
- Stereo disparity and depth estimation
- Feature-based motion estimation

**Stage Project:** ArUco-Based Robot Localization

---

## Stage 4 — Deep Learning for Robot Perception

**Lessons 18–23 | Intermediate to Advanced**

| Lesson | Topic |
|---|---|
| 18 | Deep Learning and CNN Fundamentals |
| 19 | PyTorch for Computer Vision |
| 20 | YOLO Object Detection |
| 21 | Image Segmentation |
| 22 | Custom Dataset Preparation and Model Training |
| 23 | Real-Time AI Inference and Optimization |

**Practical Implementations**
- Image classification
- Object detection with YOLO
- Real-time webcam inference
- Semantic and instance segmentation
- Custom dataset annotation
- Model training and evaluation
- FPS and inference latency benchmarking

**Stage Project:** Real-Time AI Object Detection System

---

## Stage 5 — Computer Vision with ROS 2

**Lessons 24–29 | Advanced Robotics**

| Lesson | Topic |
|---|---|
| 24 | ROS 2 Image Topics and cv_bridge |
| 25 | Camera Publisher and Subscriber Nodes |
| 26 | Camera Simulation in Gazebo |
| 27 | Vision-Based Robot Control |
| 28 | Camera Frames, TF2 and 3D Coordinates |
| 29 | Visual Perception Integration with Navigation |

**Practical Implementations**
- Publishing camera images in ROS 2
- Subscribing to `/camera/image_raw`
- Converting ROS images using `cv_bridge`
- Gazebo camera sensor integration
- Object detection nodes
- Vision-based robot following
- TF2 camera transformations
- Camera-based navigation assistance

**Stage Project:** ROS 2 Vision-Based Object-Following Robot

---

## Stage 6 — Advanced Robotics Vision

**Lessons 30–34 | Advanced**

| Lesson | Topic |
|---|---|
| 30 | Visual SLAM Fundamentals |
| 31 | RGB-D Cameras and Point Clouds |
| 32 | Camera, IMU and LiDAR Sensor Fusion |
| 33 | Robotics Perception Optimization and Deployment |
| 34 | Final Robotics Vision Capstone |

**Practical Implementations**
- Visual localization
- Visual SLAM concepts and pipelines
- Depth-based object localization
- Multi-sensor perception
- Real-time performance evaluation
- Robot perception pipeline development

**Final Project:** Intelligent Mobile Robot Perception System

---

# 🚀 Portfolio Projects

The following projects will be developed progressively throughout the learning roadmap.

| Project | Technologies | Status |
|---|---|---|
| Real-Time Color Object Detector | OpenCV, NumPy | ⬜ Planned |
| Vision-Based Line Following | OpenCV, Python | ⬜ Planned |
| Real-Time Object Tracker | OpenCV, Optical Flow | ⬜ Planned |
| ArUco Marker Localization | OpenCV, Camera Calibration | ⬜ Planned |
| AI Object Detection | YOLO, PyTorch | ⬜ Planned |
| ROS 2 Object-Following Robot | ROS 2, OpenCV, Gazebo | ⬜ Planned |
| Vision-Assisted Navigation | ROS 2, OpenCV, Nav2 | ⬜ Planned |
| Intelligent Robot Perception System | ROS 2, OpenCV, AI | ⬜ Planned |

Project statuses will be updated as implementations are completed.

---

# 📂 Repository Structure

```text
opencv-robotics-roadmap/
│
├── README.md
├── .gitignore
│
├── 01_foundations/
│   ├── lesson_01/
│   │   ├── README.md
│   │   ├── read_image.py
│   │   └── usb_camera.py
│   ├── lesson_02/
│   └── ...
│
├── 02_classical_perception/
│
├── 03_camera_geometry/
│
├── 04_deep_learning/
│
├── 05_ros2_vision/
│
├── 06_advanced_perception/
│
├── projects/
│   ├── color_object_detector/
│   ├── line_following/
│   ├── object_tracking/
│   ├── aruco_localization/
│   └── ros2_object_following/
│
├── docs/
│   ├── concepts/
│   ├── troubleshooting/
│   └── references/
│
└── assets/
    ├── images/
    └── demos/
```

*Folders and files will be added progressively as lessons and projects are completed.*

---

# ⚙️ Installation and Setup

## 1. Install Required Packages

```bash
sudo apt update

sudo apt install -y \
python3-pip \
python3-venv \
python3-dev \
v4l-utils
```

## 2. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>

cd opencv-robotics-roadmap
```

Replace `<YOUR_REPOSITORY_URL>` with the repository's actual GitHub URL.

## 3. Create a Python Virtual Environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## 4. Install OpenCV and Dependencies

```bash
python -m pip install --upgrade pip

python -m pip install opencv-python numpy matplotlib
```

Later stages may require additional dependencies, including PyTorch, YOLO and ROS 2 packages.

## 5. Verify OpenCV Installation

```bash
python -c "import cv2; print(cv2.__version__)"
```

## 6. Check USB Camera

```bash
v4l2-ctl --list-devices
```

## 7. Run a Practical Example

Once the Lesson 1 files have been added:

```bash
cd 01_foundations/lesson_01

python usb_camera.py
```

Press `q` to close the camera window.

---

# 📝 Documentation Approach

Each lesson will follow a consistent format.

### 1. WHAT
Understand the concept, its fundamentals, and the underlying mathematics where applicable.

### 2. WHY
Understand why the concept is necessary and what problems it solves.

### 3. HOW
Implement the concept through Python programs, terminal commands, and practical examples.

### 4. Industry Applications
Explore how the concept is used in autonomous mobile robots, industrial automation, autonomous vehicles, and other real-world systems.

### 5. Practical Exercises
Apply the concepts through hands-on experiments and mini-projects.

### 6. Troubleshooting
Document common errors, debugging techniques, and solutions.

### 7. Key Takeaways
Summarize the important concepts learned.

---

# 🔗 ROS 2 Integration

An important objective of this repository is to connect computer vision algorithms with real robotic systems.

The planned architecture is:

```text
USB Camera / Gazebo Camera
           |
           v
     ROS 2 Camera Node
           |
           v
    /camera/image_raw
           |
           v
      cv_bridge
           |
           v
    OpenCV Processing
           |
           v
   Object Detection /
   Tracking / Localization
           |
           v
    ROS 2 Control Logic
           |
           v
      /cmd_vel
           |
           v
      Mobile Robot
```

This pipeline will be developed incrementally as the roadmap progresses.

---

# 📊 Learning Progress

- [ ] Stage 1 — OpenCV Fundamentals
- [ ] Stage 2 — Classical Robot Perception
- [ ] Stage 3 — Camera Geometry and 3D Vision
- [ ] Stage 4 — Deep Learning for Robot Perception
- [ ] Stage 5 — Computer Vision with ROS 2
- [ ] Stage 6 — Advanced Robotics Vision

**Current Focus:** Lesson 1 — Introduction to Computer Vision and OpenCV

Progress indicators will be updated after practical verification.

---

# 📖 Related Learning

This repository complements my ROS 2 robotics learning roadmap:

**[ROS 2 Jazzy Robotics Roadmap](https://github.com/charles-shaju/ros2-jazzy-robotics-roadmap)**

The ROS 2 repository focuses on robot software architecture, communication, simulation, control, TF2, odometry, LiDAR, SLAM, and navigation.

This computer vision repository focuses on visual perception, camera geometry, object detection, tracking, and vision-based robotic behavior.

Together, they form the foundation for developing intelligent autonomous robotic systems.

---

# 📚 References

- [OpenCV Official Documentation](https://docs.opencv.org/4.x/)
- [NumPy Documentation](https://numpy.org/doc/)
- [ROS 2 Jazzy Documentation](https://docs.ros.org/en/jazzy/)
- [PyTorch Documentation](https://docs.pytorch.org/)
- [Ultralytics Documentation](https://docs.ultralytics.com/)
- [OpenCV GitHub Repository](https://github.com/opencv/opencv)

---

# 🤝 Contributions and Feedback

This is an ongoing learning repository intended to document practical computer vision and robotics concepts.

Suggestions, corrections, discussions, and constructive feedback are welcome through GitHub Issues.

---

# 📌 Final Note

Computer vision is an essential part of modern intelligent robotic systems.

My objective is to move beyond simply understanding algorithms and develop the ability to **design, implement, test, and deploy practical computer vision systems for robotics**.

This repository will continue to evolve as I learn new concepts, implement algorithms, solve problems, and build projects.

**Learning by building. Documenting by doing.**

⭐ If you find this repository helpful, consider starring it.