import requests
from playwright.async_api import Playwright

orderPayload = {"orders": [{"country": "Israel", "productOrderedId": "68a961459320a140fe1ca57a"}]}
productPayload = {
  "productName": "",
  "minPrice": "null",
  "maxPrice": "null",
  "productCategory": [],
  "productSubCategory": [],
  "productFor": []
}

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_content = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_content.post("/api/ecom/auth/login",
                                            data = {"userEmail": "shlomi@aol.com", "userPassword": "Shlomi123"})

        assert response.ok
        print (response.json())
        responseBody = response.json()
        return responseBody ["token"]



    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_content = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_content.post("/api/ecom/order/create-order",
                                 data = orderPayload,
                                 headers = {"Authorization": token,
                                            "Content-type":"application/json" })
        
        print (response.json())
        response_body = response.json()
        orderId =  response_body["orders"][0]
        return orderId
    
    def getProductCount(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_content = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_content.post("/api/ecom/product/get-all-products",
                                 data = productPayload,
                                 headers = {"Authorization": token,
                                            "Content-type":"application/json" })
        
        print(response.json())  # Print the actual response body for debugging
        if 'count' in response.json():
            count = response.json()['count']
        else:
            raise Exception(f"No 'count' in response: {response.json()}")
        return count

        

       
