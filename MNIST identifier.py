import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# --------------------------------------------------
# 0. SETTINGS
# --------------------------------------------------

SEED = 42
EPOCHS = 15
BATCH_SIZE = 128
LR_ADAM = 0.001
LR_RMSPROP = 0.001
THRESHOLD = 98.5

np.random.seed(SEED)
tf.random.set_seed(SEED)


def create_callbacks():
    """Create fresh callbacks for each training run."""
    return [
        keras.callbacks.EarlyStopping(
            monitor="val_accuracy",
            patience=4,
            restore_best_weights=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=2,
            verbose=1
        )
    ]


# --------------------------------------------------
# 1. LOAD AND PREPROCESS DATA
# --------------------------------------------------

print("\n1. Loading and preprocessing data...")

(x_train, y_train), (x_test, y_test) = (
    keras.datasets.mnist.load_data()
)

# Normalise pixels to the range 0 to 1.
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Flatten images into 784 values for Dense layers.
x_train_flat = x_train.reshape(-1, 784)
x_test_flat = x_test.reshape(-1, 784)

# Add a channel dimension for image augmentation.
x_train_4d = x_train[..., np.newaxis]
x_test_4d = x_test[..., np.newaxis]

# Convert labels to one-hot encoded values.
y_train_oh = keras.utils.to_categorical(y_train, 10)
y_test_oh = keras.utils.to_categorical(y_test, 10)

# Keep 90% for training and 10% for validation.
split_index = int(len(x_train) * 0.9)

x_train_main = x_train_flat[:split_index]
y_train_main = y_train_oh[:split_index]

x_val_flat = x_train_flat[split_index:]
y_val_oh = y_train_oh[split_index:]

x_train_aug = x_train_4d[:split_index]
x_val_4d = x_train_4d[split_index:]

y_train_aug = y_train_oh[:split_index]

print("Training samples:", len(x_train_main))
print("Validation samples:", len(x_val_flat))
print("Test samples:", len(x_test_flat))


# --------------------------------------------------
# 2. BUILD THE NEURAL NETWORK
# --------------------------------------------------

def build_model(optimizer, name):
    """Build and compile a three-hidden-layer model."""

    model = keras.Sequential(
        [
            layers.Input(shape=(784,)),

            # Hidden layer 1
            layers.Dense(512, use_bias=False),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.1),
            layers.Dropout(0.3),

            # Hidden layer 2
            layers.Dense(256, use_bias=False),
            layers.BatchNormalization(),
            layers.LeakyReLU(negative_slope=0.1),
            layers.Dropout(0.3),

            # Hidden layer 3
            layers.Dense(128, activation="relu"),
            layers.Dropout(0.2),

            # Output layer: 10 digit classes
            layers.Dense(10, activation="softmax")
        ],
        name=name
    )

    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


print("\n2. Building models...")

model_adam = build_model(
    keras.optimizers.Adam(learning_rate=LR_ADAM),
    "MNIST_Adam"
)

model_rmsprop = build_model(
    keras.optimizers.RMSprop(learning_rate=LR_RMSPROP),
    "MNIST_RMSprop"
)

model_adam.summary()


# --------------------------------------------------
# 3. TRAIN WITHOUT AUGMENTATION
# --------------------------------------------------

print("\n3. Training with Adam...")

hist_adam = model_adam.fit(
    x_train_main,
    y_train_main,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_data=(x_val_flat, y_val_oh),
    callbacks=create_callbacks(),
    verbose=1
)

print("\nTraining with RMSprop...")

hist_rmsprop = model_rmsprop.fit(
    x_train_main,
    y_train_main,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_data=(x_val_flat, y_val_oh),
    callbacks=create_callbacks(),
    verbose=1
)


# --------------------------------------------------
# 4. TRAIN WITH DATA AUGMENTATION
# --------------------------------------------------

print("\n4. Training with data augmentation...")

datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)

# Build a model that accepts 28 x 28 images.
aug_input = keras.Input(shape=(28, 28, 1))
flat_output = layers.Flatten()(aug_input)

# Use a separate model for the augmented experiment.
model_aug = build_model(
    keras.optimizers.Adam(learning_rate=LR_ADAM),
    "MNIST_Adam_Augmented"
)

aug_output = model_aug(flat_output)

full_aug_model = keras.Model(
    inputs=aug_input,
    outputs=aug_output,
    name="Augmented_Pipeline"
)

full_aug_model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LR_ADAM),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

train_gen = datagen.flow(
    x_train_aug,
    y_train_aug,
    batch_size=BATCH_SIZE,
    shuffle=True,
    seed=SEED
)

# Use original, unaugmented images for validation.
hist_aug = full_aug_model.fit(
    train_gen,
    epochs=EPOCHS,
    validation_data=(x_val_4d, y_val_oh),
    callbacks=create_callbacks(),
    verbose=1
)


# --------------------------------------------------
# 5. EVALUATE THE MODELS
# --------------------------------------------------

print("\n5. Evaluating models...")

loss_adam, acc_adam = model_adam.evaluate(
    x_test_flat, y_test_oh, verbose=0
)

loss_rmsprop, acc_rmsprop = model_rmsprop.evaluate(
    x_test_flat, y_test_oh, verbose=0
)

loss_aug, acc_aug = full_aug_model.evaluate(
    x_test_4d, y_test_oh, verbose=0
)

print(
    f"Adam: Loss = {loss_adam:.4f}, "
    f"Accuracy = {acc_adam * 100:.2f}%"
)

print(
    f"RMSprop: Loss = {loss_rmsprop:.4f}, "
    f"Accuracy = {acc_rmsprop * 100:.2f}%"
)

print(
    f"Adam + Augmentation: Loss = {loss_aug:.4f}, "
    f"Accuracy = {acc_aug * 100:.2f}%"
)


# --------------------------------------------------
# 6. PLOT TRAINING CURVES
# --------------------------------------------------

print("\n6. Creating graphs...")

histories = [
    (hist_adam, "Adam"),
    (hist_rmsprop, "RMSprop"),
    (hist_aug, "Adam + Augmentation")
]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for history, name in histories:
    axes[0].plot(
        history.history["accuracy"],
        label=f"{name} - Train"
    )
    axes[0].plot(
        history.history["val_accuracy"],
        linestyle="--",
        label=f"{name} - Validation"
    )

    axes[1].plot(
        history.history["loss"],
        label=f"{name} - Train"
    )
    axes[1].plot(
        history.history["val_loss"],
        linestyle="--",
        label=f"{name} - Validation"
    )

axes[0].set_title("Accuracy per Epoch")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Accuracy")
axes[0].legend(fontsize=7)
axes[0].grid(True)

axes[1].set_title("Loss per Epoch")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Loss")
axes[1].legend(fontsize=7)
axes[1].grid(True)

fig.tight_layout()
fig.savefig("training_curves.png", dpi=150)
plt.close(fig)

print("Saved: training_curves.png")


# --------------------------------------------------
# 7. DISPLAY SAMPLE PREDICTIONS
# --------------------------------------------------

print("\n7. Creating prediction grid...")

y_pred_probs = model_adam.predict(x_test_flat, verbose=0)
y_pred = np.argmax(y_pred_probs, axis=1)

n_cols = 10
n_rows = 4

fig = plt.figure(figsize=(16, 8))
fig.suptitle(
    f"MNIST Predictions - Accuracy: {acc_adam * 100:.2f}%"
)

gs = gridspec.GridSpec(n_rows, n_cols)

rng = np.random.default_rng(SEED)

sample_indices = rng.choice(
    len(x_test),
    n_rows * n_cols,
    replace=False
)

for i, sample_idx in enumerate(sample_indices):
    ax = fig.add_subplot(gs[i // n_cols, i % n_cols])

    ax.imshow(x_test[sample_idx], cmap="gray_r")

    predicted = y_pred[sample_idx]
    actual = y_test[sample_idx]

    title_color = "green" if predicted == actual else "red"

    ax.set_title(
        f"P:{predicted} T:{actual}",
        fontsize=8,
        color=title_color
    )

    ax.axis("off")

fig.tight_layout()
fig.savefig("predictions_grid.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Saved: predictions_grid.png")


# --------------------------------------------------
# 8. COMPARE TEST ACCURACY
# --------------------------------------------------

labels = ["Adam", "RMSprop", "Adam + Augmentation"]

accuracies = [
    acc_adam * 100,
    acc_rmsprop * 100,
    acc_aug * 100
]

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(labels, accuracies)

ax.set_ylim(0, 100)
ax.set_ylabel("Test Accuracy (%)")
ax.set_title("Optimizer and Augmentation Comparison")
ax.grid(axis="y", alpha=0.3)

for bar, accuracy in zip(bars, accuracies):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{accuracy:.2f}%",
        ha="center"
    )

fig.tight_layout()
fig.savefig("accuracy_comparison.png", dpi=150)
plt.close(fig)

print("Saved: accuracy_comparison.png")


# --------------------------------------------------
# 9. FEEDBACK AND SUGGESTIONS
# --------------------------------------------------

print("\n9. Feedback and suggestions...")

results = {
    "Adam": acc_adam * 100,
    "RMSprop": acc_rmsprop * 100,
    "Adam + Augmentation": acc_aug * 100
}

best_name = max(results, key=results.get)
best_accuracy = results[best_name]

print(f"\nBest model: {best_name}")
print(f"Test accuracy: {best_accuracy:.2f}%")

if best_accuracy >= THRESHOLD:
    print("The model meets the accuracy target.")
    print("Suggestions:")
    print("- Try a Convolutional Neural Network (CNN).")
    print("- Experiment with learning-rate scheduling.")
    print("- Compare model performance on unseen images.")
else:
    print("The model is below the accuracy target.")
    print("Suggestions:")
    print("- Try training for more epochs.")
    print("- Experiment with batch size and learning rate.")
    print("- Consider using a CNN for image classification.")

print("\nAll done!")
print("Check the three PNG images in your project folder.")
