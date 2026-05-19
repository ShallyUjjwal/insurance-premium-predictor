from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output


from schema.user_input import UserInput

# import the ml model

app = FastAPI()



@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Category Predictor"}

@app.get('/health')
def health():
    return {"message": "Healthy"}   

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input  ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'predicted_category': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})



