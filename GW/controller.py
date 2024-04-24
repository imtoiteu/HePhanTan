from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from gateway import Cart_Gateway, CartDetail_Gateway, Category_Gateway, Favorites_Gateway, Notification_Gateway, Oder_Gateway, OderDetail_Gateway,Product_Gateway, Rate_Gateway, SendMail_Gateway, Statistical_Gateway, User_Gateway
 
from fastapi.middleware.cors import CORSMiddleware 




app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:8080"],
        allow_methods=['*'],
        allow_headers=['*']
    )
app.include_router(Cart_Gateway.router, prefix="/api/cart", tags=["cart"])
app.include_router(CartDetail_Gateway.router, prefix="/api/cartDetail", tags=["cartDetail"])
app.include_router(Category_Gateway.router, prefix="/api/categories", tags=["categories"])
app.include_router(Favorites_Gateway.router, prefix="/api/favorites", tags=["favorites"])
app.include_router(Notification_Gateway.router, prefix="/api/notification", tags=["notification"])
app.include_router(Oder_Gateway.router, prefix="/api/orders", tags=["orders"])
app.include_router(OderDetail_Gateway.router, prefix="/api/orderDetail", tags=["orderDetail"])
app.include_router(Product_Gateway.router, prefix="/api/products", tags=["products"])
app.include_router(Rate_Gateway.router, prefix="/api/rates", tags=["rates"])
app.include_router(SendMail_Gateway.router, prefix="/api/send-mail", tags=["send-mail"])
app.include_router(Statistical_Gateway.router, prefix="/api/statistical", tags=["statistical"])
app.include_router(User_Gateway.router, prefix="/api/auth", tags=["auth"])



@app.get("/")
def documentation():
    return RedirectResponse(url="/docs") 



