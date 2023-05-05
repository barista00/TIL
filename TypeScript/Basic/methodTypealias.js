var 회원정보 = {
    name: 'kim',
    age: 30,
    plusOne: function (x) {
        return x + 1;
    },
    changeName: function () {
        console.log('안녕');
    }
};
회원정보.plusOne(1);
회원정보.changeName();
var varicutZero = function cutZero(x) {
    if (x[0] === '0') {
        return x.slice(1);
    }
    else {
        return x;
    }
};
var variremove = function removeDash(x) {
    return parseInt(x.replace(/-/g, ""));
};
var threeplus = function (x, y, z) {
    return z(y(x));
};
threeplus('010-1234-1234', varicutZero, variremove); // 1012341234 출력
