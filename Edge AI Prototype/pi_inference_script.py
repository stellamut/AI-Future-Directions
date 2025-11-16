{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b013e40",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "# Convert trained model to TensorFlow Lite\n",
    "converter = tf.lite.TFLiteConverter.from_keras_model(model)\n",
    "tflite_model = converter.convert()\n",
    "\n",
    "# Save model\n",
    "with open(\"recycle_classifier.tflite\", \"wb\") as f:\n",
    "    f.write(tflite_model)\n",
    "\n",
    "# Test inference with TFLite interpreter\n",
    "interpreter = tf.lite.Interpreter(model_path=\"recycle_classifier.tflite\")\n",
    "interpreter.allocate_tensors()\n",
    "\n",
    "input_details = interpreter.get_input_details()\n",
    "output_details = interpreter.get_output_details()\n",
    "\n",
    "# Run inference on one test image\n",
    "test_image = np.expand_dims(x_test[0], axis=0).astype(np.float32)\n",
    "interpreter.set_tensor(input_details[0]['index'], test_image)\n",
    "interpreter.invoke()\n",
    "output_data = interpreter.get_tensor(output_details[0]['index'])\n",
    "print(\"Predicted class:\", np.argmax(output_data))\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
