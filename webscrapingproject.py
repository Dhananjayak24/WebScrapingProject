import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
       "URL" : "https://www.flipkart.com/asus-tuf-gaming-f15-core-i5-10th-gen-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-fx506lhb-hn358w-laptop/p/itm4d930ab779cbd?pid=COMGF9Z7JYCFBKAP&lid=LSTCOMGF9Z7JYCFBKAPXYET0O&marketplace=FLIPKART&q=gaming+laptop&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=search-autosuggest&iid=70715502-6f03-45ce-bfa9-0fbfb65dfeb9.COMGF9Z7JYCFBKAP.SEARCH&ppt=sp&ppn=sp&ssid=7off7tl0ow0000001665930101200&qH=da5ee6f53d84b3c2",
       "Name":"ASUS TUF Gaming F15",
        "Target_price" : "47000"
    },
    {
       "URL" : "https://www.flipkart.com/asus-vivobook-15-core-i5-12th-gen-8-gb-512-gb-ssd-windows-11-home-x1502za-bq502ws-laptop/p/itma8764ec63405a?pid=COMGEEY9WMHMW9VB&lid=LSTCOMGEEY9WMHMW9VBXWAOAQ&marketplace=FLIPKART&q=vivobook+15&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&fm=search-autosuggest&iid=29e360d0-76b7-449c-91d1-aad0a5d4a112.COMGEEY9WMHMW9VB.SEARCH&ppt=dynamic&ppn=CART_PAGE&ssid=h5nh7bu2800000001665929307146&qH=a0209f472a143c16",
        "Name" : "ASUS Vivobook 15",
        "Target_price": "60000"
    },
    {
       "URL" : "https://www.flipkart.com/hp-pavilion-ryzen-5-hexa-core-amd-r5-5600h-8-gb-512-gb-ssd-windows-10-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-ec2004ax-gaming-laptop/p/itm98c94bbf9bc20?pid=COMG5GZXPWMGTNWS&lid=LSTCOMG5GZXPWMGTNWSQE9WVW&marketplace=FLIPKART&q=gaming+laptop&store=6bo%2Fb5g&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=search-autosuggest&iid=70715502-6f03-45ce-bfa9-0fbfb65dfeb9.COMG5GZXPWMGTNWS.SEARCH&ppt=sp&ppn=sp&ssid=7off7tl0ow0000001665930101200&qH=da5ee6f53d84b3c2",
        "Name" : "HP Pavilion Ryzen 5",
        "Target_price": "52000"
    },
    {
       "URL" : "https://www.flipkart.com/msi-gf63-thin-hexa-core-i5-10th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-max-q-144-hz-10scxr-1616in-10sc-611in-gaming-laptop/p/itmb8888c44a1a68?pid=COMG2K9ZBFJ3ZASR&lid=LSTCOMG2K9ZBFJ3ZASRMMSIPX&marketplace=FLIPKART&q=gaming+laptop&store=6bo%2Fb5g&spotlightTagId=BestvalueId_6bo%2Fb5g&srno=s_1_10&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=search-autosuggest&iid=70715502-6f03-45ce-bfa9-0fbfb65dfeb9.COMG2K9ZBFJ3ZASR.SEARCH&ppt=sp&ppn=sp&qH=da5ee6f53d84b3c2",
        "Name" : "MSI GF63",
        "Target_price": "53500"
    },
    {
       "URL" : "https://www.flipkart.com/lenovo-ideapad-gaming-3-core-i5-11th-gen-8-gb-512-gb-ssd-windows-11-home-4-graphics-nvidia-geforce-rtx-3050-15ihu6d2-laptop/p/itm78e98bb9abfb1?pid=COMGBNFUHREA8EJN&lid=LSTCOMGBNFUHREA8EJNCOPCZZ&marketplace=FLIPKART&q=gaming+laptop&store=6bo%2Fb5g&srno=s_1_11&otracker=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_7_na_na_na&fm=search-autosuggest&iid=en_STOAZapClD1i0y3Fcyq%2B9wRqQwet3yoZZU%2Fjfb1SBwwwLVVlAtOWw1sV4KETmlTMZjVCOTlzjdgjWzUGAkJMhg%3D%3D&ppt=sp&ppn=sp&ssid=7off7tl0ow0000001665930101200&qH=da5ee6f53d84b3c2",
        "Name" : "Lenovo IdeaPad Gaming 3",
        "Target_price": "56000"
    }
]

def give_product_price(URL):
   headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
   page = requests.get(URL, headers=headers)
   soup = BeautifulSoup(page.content, 'html.parser')
   price1 = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
   return price1.getText()
result_file = open("my_result_file.txt",'w')
try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("URL"))
        print(every_product.get("Name") + " - " + product_price_returned)

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(",", "")
        my_product_price = float(my_product_price)
        print(my_product_price)

        if my_product_price < int(every_product.get("Target_price")):
            print("You can purchase this product")
            result_file.write(every_product.get(
                'Name') + ' ' + "is available at" '\t' + str(my_product_price) + ",Which is within your price range" '\n' )
        else:
            print("Product is still out of your range")
finally:
    result_file.close()