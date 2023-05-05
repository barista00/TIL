// 숫자 여러개를 입력하면 최댓값을 return 해주는 함수를 만들어봅시다. 
// 최댓값(6,3,7,2) 이렇게 쓰면 7이 return 되어야합니다. 
// (조건1) 넣을 수 있는 숫자 갯수는 제한없음, 0 이상의 정수만 가능합니다.
// (조건2) Math.max() 사용금지 반복문이나 쓰셈 
function maxnum() {
    var nums = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        nums[_i] = arguments[_i];
    }
    var newnum = 0;
    nums.forEach(function (a) {
        if (newnum < a) {
            newnum = a;
        }
    });
    return newnum;
}
console.log(maxnum(10, 2, 3, 4, 5));
function 함수(_a) {
    var user = _a.user, comment = _a.comment, admin = _a.admin;
    console.log(user, comment, admin);
}
함수({ user: 'Kim', comment: [3, 5, 4], admin: false });
function func(_a) {
    var a = _a[0], b = _a[1], c = _a[2];
    console.log(a, b, c);
}
func([40, 'wine', false]);
