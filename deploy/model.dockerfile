FROM tensorflow/serving:2.7.0

COPY ./fruit_prediction /models/fruit_prediction/1
ENV MODEL_NAME="fruit_prediction"

