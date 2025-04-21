# my_llm

Learning Steps
install python and pip
run setup and lunch basic scrip
create custom model >> using extract frame, labelImg
train Model
update script using trained custom model.

** Steps create Model \***
✅ Step-by-Step Plan
✅ Step 1: Extracted video frames – ✅ Done
python labelImg.py
✅ Step 2: Annotated frames using LabelImg (VOC XML) – ✅ Done
name the label of frame
✅ Step 3: Convert annotations from VOC XML → YOLO format
python convert_voc_to_yolo.py
✅ Step 4: Organize your dataset for YOLOv8
pip install ultralytics
create data.yaml
✅ Step 5: Train your model with Ultralytics YOLOv8
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
output after trained will be "best.pt"

\*\*\* run python detect_and_count.py

\*\* run
run

# Create a virtual environment

python3 -m venv my_llm_env
source my_llm_env/bin/activate

# Upgrade pip

pip install --upgrade pip

# Install dependencies

pip install torch torchvision torchaudio
pip install opencv-python
pip install matplotlib
pip install ultralytics # For YOLOv8 model
pip install numpy

echo "✅ Environment setup complete. Use: source my_llm_env/bin/activate"

python -m venv my_llm_env
.\my_llm_env\Scripts\activate
pip install --upgrade pip
pip install torch torchvision torchaudio
pip install opencv-python
pip install matplotlib
pip install ultralytics
pip install numpy

set OPENCV_FFMPEG_READ_ATTEMPTS=1000000

python detect_and_count.py

\*\* Train Model
python extract_frames.py

once you have the images so you need to label it

git clone https://github.com/tzutalin/labelImg.git
cd labelImg
python -m venv venv
venv\Scripts\activate
pip install pyqt5 sip lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
