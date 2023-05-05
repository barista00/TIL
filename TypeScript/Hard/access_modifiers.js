// 다음 x, y, z 속성의 특징을 설명해보십시오.
// class User {
//   private static x = 10;
//   public static y = 20;
//   protected z = 30;
// }
// 누가 쓸 수 있고, 어디서 수정할 수 있는지 이런 것들이요. 
// 친구가 물어봤을 때 어떻게 답해줄 것입니까
// private static - class 내부에서만 사용가능하며 인스턴스화 하지못하고 클래스 자체로 사용가능하다
// public static - 인스턴스화해서 사용하지 못하며 클래스 자체로 사용가능하다
// protected - 클래스 내부에서만 사용가능하며 확장할 때도 상속받는다 
// x 속성에 숫자를 더해주는 함수가 필요합니다.
// class User {
// private static x = 10;
// public static y = 20;
// }
// User.addOne(3) //이렇게 하면 x가 3 더해져야함
// User.addOne(4) //이렇게 하면 x가 4 더해져야함
// User.printX()  //이렇게 하면 콘솔창에 x값이 출력되어야함
// 저렇게 User.addOne() 쓸 때마다 x가 증가하는 함수는 어떻게 만들 수 있을까요? 
// 그리고 x값을 콘솔창에 출력해주는 printX() 함수도 한번 만들어보십시오.
// (조건) private static x = 10; 이 코드 수정금지 
var User = /** @class */ (function () {
    function User() {
    }
    User.addOne = function (a) {
        User.x = User.x + a;
    };
    ;
    User.printx = function () {
        console.log(User.x);
    };
    ;
    User.x = 10;
    User.y = 20;
    return User;
}());
User.addOne(3);
User.addOne(3);
User.addOne(3);
User.addOne(3);
User.printx();
