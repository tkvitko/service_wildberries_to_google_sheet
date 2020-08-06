from google_integration import add_to_sheet

if __name__ == "__main__":
    values_to_add = [["number",
                      "date",
                      "lastChangeDate",
                      "supplierArticle",
                      "techSize",
                      "barcode",
                      "quantity",
                      "totalPrice",
                      "discountPercent",
                      "isSupply",
                      "isRealization",
                      "orderId",
                      "promoCodeDiscount",
                      "warehouseName",
                      "countryName",
                      "oblastOkrugName",
                      "regionName",
                      "incomeID",
                      "saleID",
                      "odid",
                      "spp",
                      "forPay",
                      "finishedPrice",
                      "priceWithDisc",
                      "nmId",
                      "subject",
                      "category",
                      "brand",
                      "IsStorno"]]

    add_to_sheet(values_to_add)
