import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models

# -------------------------------
# Parameters
# -------------------------------
IMG_SIZE = 64      # Resize frame size
SEQ_LEN = 20       # Number of frames per video
BATCH_SIZE = 8
EPOCHS = 20
DATASET_PATH = r"C:\Users\sreeyaa raaman\AppData\Local\Programs\Python\Python310\streetpro\VioPeru-main"   # root folder containing train/ and val/

# -------------------------------
# Helper: Load video frames
# -------------------------------
def load_video_frames(video_path, max_frames=SEQ_LEN):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    # Pad if fewer frames
    while len(frames) < max_frames:
        frames.append(np.zeros((IMG_SIZE, IMG_SIZE, 3)))
    return np.array(frames) / 255.0

# -------------------------------
# Load dataset from folder
# -------------------------------
def load_dataset(split):
    X, y = [], []
    split_path = os.path.join(DATASET_PATH, split)
    for label, category in enumerate(["NonFight", "Fight"]):
        folder = os.path.join(split_path, category)
        for file in os.listdir(folder):
            if file.endswith((".mp4", ".avi", ".mov")):
                video_path = os.path.join(folder, file)
                frames = load_video_frames(video_path)
                X.append(frames)
                y.append(label)
    return np.array(X), np.array(y)

print("Loading training data...")
X_train, y_train = load_dataset("train")
print("Train:", X_train.shape, y_train.shape)

print("Loading validation data...")
X_val, y_val = load_dataset("val")
print("Validation:", X_val.shape, y_val.shape)

# -------------------------------
# Build CNN + LSTM Model
# -------------------------------
def build_model():
    model = models.Sequential([
        layers.TimeDistributed(layers.Conv2D(32, (3,3), activation='relu'),
                               input_shape=(SEQ_LEN, IMG_SIZE, IMG_SIZE, 3)),
        layers.TimeDistributed(layers.MaxPooling2D((2,2))),
        layers.TimeDistributed(layers.Conv2D(64, (3,3), activation='relu')),
        layers.TimeDistributed(layers.MaxPooling2D((2,2))),
        layers.TimeDistributed(layers.Flatten()),
        
        layers.LSTM(64, return_sequences=False),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Binary output
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

model = build_model()
model.summary()

# -------------------------------
# Train
# -------------------------------
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# -------------------------------
# Print final accuracies
# -------------------------------
train_acc = history.history['accuracy'][-1]
val_acc = history.history['val_accuracy'][-1]
print(f"\n✅ Final Training Accuracy: {train_acc*100:.2f}%")
print(f"✅ Final Validation Accuracy: {val_acc*100:.2f}%")

# -------------------------------
# Save model
# -------------------------------
model.save("suspicious_activity_cnn_lstm.h5")
print("✅ Model saved as suspicious_activity_cnn_lstm.h5")


