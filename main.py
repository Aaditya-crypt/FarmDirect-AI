from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import json

# ✅ Initialize app
app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load model and encoders
model = joblib.load("price_model.pkl")
crop_encoder = joblib.load("crop_encoder.pkl")
state_encoder = joblib.load("state_encoder.pkl")


# =========================
# 🔹 UTILITY FUNCTIONS
# =========================

def load_crops():
    try:
        with open("crops.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_crops(data):
    with open("crops.json", "w") as f:
        json.dump(data, f, indent=4)


# =========================
# 🔹 ROUTES
# =========================

# ✅ Home route
@app.get("/")
def home():
    return {"message": "FarmDirect AI Running"}


# ✅ Predict route (AI)
@app.get("/predict")
def predict(crop: str, state: str, month: int):
    try:
        crop = crop.strip().title()
        state = state.strip().title()

        crop_val = crop_encoder.transform([crop])[0]
        state_val = state_encoder.transform([state])[0]

        data = pd.DataFrame({
            "month": [month],
            "crop_encoded": [crop_val],
            "state_encoded": [state_val]
        })

        price = model.predict(data)[0]

        return {
            "crop": crop,
            "state": state,
            "month": month,
            "predicted_price": round(price, 2)
        }

    except Exception as e:
        return {
            "error": str(e),
            "valid_crops": list(crop_encoder.classes_),
            "valid_states": list(state_encoder.classes_)
        }


# ✅ Add Crop (Farmer)
@app.post("/order")
def place_order(
    crop_id: int = Body(...),
    quantity: int = Body(..., gt=0)
):
    try:
        crops = load_crops()
        orders = load_orders()

        crop = next((c for c in crops if c["id"] == crop_id), None)

        if not crop:
            return {"error": "Crop not found"}

        # 🔥 THIS PART (UPDATED)
        new_order = {
            "id": len(orders) + 1,
            "crop_id": crop_id,
            "name": crop["name"],
            "state": crop["state"],
            "quantity": quantity,
            "status": "Placed",
            "delivery_partner": None
        }

        orders.append(new_order)
        save_orders(orders)

        return {"message": "Order placed", "order": new_order}

    except Exception as e:
        return {"error": str(e)}


# ✅ Get Crops (Customer view)
@app.get("/crops")
def get_crops():
    try:
        return load_crops()
    except Exception as e:
        return {"error": str(e)}

# =========================
# 🔹 ORDER SYSTEM
# =========================

def load_orders():
    try:
        with open("orders.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_orders(data):
    with open("orders.json", "w") as f:
        json.dump(data, f, indent=4)


# ✅ PLACE ORDER
@app.post("/order")
def place_order(
    crop_id: int = Body(...),
    quantity: int = Body(..., gt=0)
):
    try:
        crops = load_crops()
        orders = load_orders()

        crop = next((c for c in crops if c["id"] == crop_id), None)

        if not crop:
            return {"error": "Crop not found"}

        new_order = {
            "id": len(orders) + 1,
            "crop_id": crop_id,
            "name": crop["name"],
            "state": crop["state"],
            "quantity": quantity
        }

        orders.append(new_order)
        save_orders(orders)

        return {"message": "Order placed", "order": new_order}

    except Exception as e:
        return {"error": str(e)}


# ✅ GET ORDERS
@app.get("/orders")
def get_orders():
    return load_orders()