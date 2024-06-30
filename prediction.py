import joblib
 
model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")


def prediction(data):
    result = model.predict(data.values)
    final_result = result_target.inverse_transform(result)[0]

    print(final_result)
    return final_result