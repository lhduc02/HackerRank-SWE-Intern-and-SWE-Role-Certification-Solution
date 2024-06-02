def priceCheck(products, productPrices, productSold, soldPrice):
    cnt = 0
    for i in range(len(productSold)):
        idx = products.index(productSold[i])
        if productPrices[idx] != soldPrice[i]:
            cnt += 1
    return cnt
