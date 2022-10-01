from google_integration import add_to_sheet


def header_adding():
    """Adding header to google sheet"""

    values_to_add = [[
        "number",
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
        "IsStorno"
    ]]

    add_to_sheet(values_to_add)


if __name__ == "__main__":
    header_adding()
