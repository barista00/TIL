var 상품 = { brand: 'Samsung', serialNumber: 1360, model: ['TV', 'phone'] };
var 장바구니 = [{ product: '청소기', price: 7000 }, { product: '삼다수', price: 800 }];
var new장바구니 = [{ product: '청소기', price: 7000, card: false }];
var obj = {
    plus: function (a, b) {
        return a + b;
    },
    minus: function (a, b) {
        return a - b;
    },
};
console.log(obj.plus(1, 2)); // 3
console.log(obj.minus(2, 3)); // -1
