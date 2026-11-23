import os
from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime, timezone
import requests

email = os.environ["TASK8_BROWSER_EMAIL"]
password = os.environ["TASK8_BROWSER_PASSWORD"]
r = requests.post("http://127.0.0.1:18331/api/auth/register",
                  json={"name":"Task Eight Fixture","email":email,"password":password,"phone":"5550100042"}, timeout=8)
r.raise_for_status()
customer = r.json()["user"]["id"]
client = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = client.comein_disposable_task8
now = datetime.now(timezone.utc)
shop, menu = ObjectId(), ObjectId()
db.restaurants.insert_one({"_id":shop,"owner_id":str(ObjectId()),"name":"Task Eight Kitchen","status":"approved",
                           "available":True,"delivery_available":False,"pickup_available":True,"tax_rate":10,
                           "delivery_fee":25,"payment_methods":["pickup"],"created_at":now})
db.restaurant_menu.insert_one({"_id":menu,"restaurant_id":str(shop),"name":"Task Eight Bowl","available":True,
                               "price":60,"variants":[{"id":"large","name":"Large","price":100}],
                               "add_ons":[{"id":"dip","name":"Dip","price":10}]})
db.restaurant_orders.insert_one({"customer_id":customer,"restaurant_id":str(shop),"restaurant_name":"Task Eight Kitchen",
                                 "ref":"TASK8-HISTORY","status":"picked_up","payment_status":"paid","payment_method":"razorpay",
                                 "gateway_payment_id":"historic_fixture","fulfillment":"pickup","total":45,
                                 "created_at":now,"idempotency_key":"task8-browser-history",
                                 "items":[{"menu_item_id":str(menu),"name":"Task Eight Bowl","quantity":1,"unit_price":45,
                                           "variant":{"id":"large"},"add_ons":[{"id":"dip"}],"instructions":"No onions"},
                                          {"menu_item_id":str(ObjectId()),"name":"Removed side","quantity":1,"unit_price":15}]})
