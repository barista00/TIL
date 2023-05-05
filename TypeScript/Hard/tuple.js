// 여러분이 최근에 사먹은 음식의 1. 이름 2. 가격 3. 맛있는지여부를 array 자료에 담아보고 타입지정까지 해보십시오.
// 오늘 배운 tuple 타입으로 타입지정합시다. 
// 쉬워서 답은 생략합니다. 
// (예시) [ '동서녹차', 4000, true ] 이런 자료 만들고 타입지정하라는 소리입니다.
var arr = ['치킨', 5000, true];
// 이렇게 생긴 자료는 타입지정 어떻게 해야할까요?
// let arr = ['동서녹차', 4000, true, false, true, true, false, true]
// 몇개인지는 모르겠지만 true와 false가 셋째 자료부터 잔뜩 들어올 수 있다고 합니다. 
// tuple 타입과 spread 연산자를 써보도록 합시다. 
var arr2 = ['동서녹차', 4000, true, false, true, true, false, true];
function f() {
    var rest = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        rest[_i] = arguments[_i];
    }
    console.log.apply(console, rest);
}
f('문자', true, 123, 'hello');
// 다음과 같은 문자/숫자 분류기 함수를 만들어보십시오.
// 파라미터 중 문자만 모아서 [] 에 담아주고, 숫자만 모아서 [] 에 담아주는 함수가 필요합니다.
// 문자 숫자 외의 자료는 입력불가능하고 파라미터 갯수 제한은 일단 없습니다. 
// 함수 만들어보시고 함수의 파라미터/return 타입지정도 확실하게 해봅시다. 
// (동작예시)
// 함수('b', 5, 6, 8, 'a') 이렇게 사용할 경우 이 자리에 [ ['b', 'a'], [5, 6, 8] ] 이 return 되어야합니다.
function split() {
    var rest = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        rest[_i] = arguments[_i];
    }
    var stringarr = [];
    var numberarr = [];
    rest.forEach(function (a) {
        if (typeof a === 'string') {
            stringarr.push(a);
        }
        else {
            numberarr.push(a);
        }
    });
    return [stringarr, numberarr];
}
console.log(split('a', 1, 2, 'c'));
var arr3 = [4, 5, 6, 7, 8, 9, 10];
console.log(arr3);
