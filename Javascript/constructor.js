// 0. 오브젝트 자료 여러개를 만들고 싶습니다. 
// 제일 잘하는게 하드코딩이기 때문에 하드코딩해봤습니다. 
// var 학생1 = { name : 'Kim', age : 20 }
// var 학생2 = { name : 'Park', age : 21 }
// var 학생3 = { name : 'Lee', age : 22 }
// 하드코딩해서 3개를 만들긴 했는데 앞으로 만들일이 더 많이 생길 것 같아서 constructor를 제작하려고 합니다.
// constructor문법을 사용해서 위의 오브젝트와 똑같은 오브젝트 3개를 한번 뽑아보십시오. 
// + 여기에 학생1.sayHi()라고 사용하면 "안녕 나는 Kim이야" 라는 글자가 콘솔창에 나오도록 sayHi()라는 함수도 constructor 안에 추가해보세요. 
function Student(name, age){
  this.name = name
  this.age = age
  this.sayHi = () => {
    console.log(`안녕 나는 ${this.name} 이야`)
  }
}

const 학생1 = new Student('Kim', 20)
const 학생2 = new Student('Park', 21)
const 학생3 = new Student('Lee', 22)
학생1.sayHi()
학생2.sayHi()
학생3.sayHi()

// 1. 다음 코드의 출력 결과는 무엇일까요?
function Parent(){
  this.name = 'Kim';
}
var a = new Parent();

a.__proto__.name = 'Park';
a.__proto__.age = 20;
console.log(a.name)
// 정답 Park?
// Kim이 정답임
// 부모 prototype에 Park이 추가된 것이므로 위에 있는 Kim이 출력된다 
// 내가 직접 가지고 있으면 내걸 출력해주고 부모 prototype에 속성을 확인하는 건 내가 가지고 있지 않은 경우
// 부모까지 올라가서 확인 하는 것임 



// 2. 함수가 안들어가요 엉엉
// 위에 0번 문제에서 Student라는 부모에 sayHi라는 함수를 하나 추가하라고 했죠?
// 그래서 sayHi()라고 사용하면 "안녕 나는 ~~이야" 라고 내 이름을 출력해주는 함수를 prototype에 추가했습니다. 
// 하단처럼 만들었는데 의도한 대로 이름이 출력되지 않고 있습니다. 
// 원인은 무엇일까요? 

// function Student(이름, 나이){
//   this.name = 이름;
//   this.age = 나이;
// }

// Student.prototype.sayHi = () => {
//     console.log('안녕 나는 ' + this.name + '이야');
//   }
// var 학생1 = new Student('Kim', 20);
// 학생1.sayHi(); //왜 이 코드가 제대로 안나오죠?

// 정답은 arrow function에서 this를 사용하는 것과 그냥 함수 선언식에서 this를 사용하는게 다른 this가 된다



// 3. 모든 array에 적용할 수 있는 함수를 직접 새로 만들려면 어떻게 해야할까요?
// 모든 array에 붙일 수 있는,
// array 내에 있는 3이라는 값을 제거해주는 유용한 함수를 하나 만들고 싶습니다. 

// var arr = [1,2,3];
// arr.remove3();

// console.log(arr); //[1,2]
// 이렇게 array뒤에 붙이기만 하면 array 내의 3이라는 모든 숫자 자료들이 삭제됩니다. 
// 멋있게 이름은 remove3() 이라고 하겠습니다. 
// remove3()함수는 어떻게, 어디에 만들어야 모든 array에 쓸 수 있을까요?

Array.prototype.remove3 = function () {
  let newArr = []
  this.forEach((a)=>{
    if (a !== 3) {
      newArr.push(a)
    }
  })
  return newArr
}

let arr = [1,2,3,4,5,3,3]
console.log(arr.remove3())