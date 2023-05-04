export
// 다음 4개에 타입을 지정해보자
let user :string= 'kim';
let age :undefined | number= undefined;
let married :boolean= false; 
let 철수 :(string | undefined | number | boolean)[]= [user, age, married];

// 학교라는 변수에 타입을 지정하자
// let 학교 = {
//   score : [100, 97, 84],
//   teacher : 'Phil',
//   friend : 'John'
// }
// 학교.score[4] = false;
// 학교.friend = ['Lee' , 학교.teacher]
let 학교 :{ 
  score : (number | boolean)[], 
  teacher : string,
  friend : string | string[]
} = {
  score : [100, 97, 84],
  teacher : 'Phil',
  friend : 'John'
}
학교.score[4] = false;
학교.friend = ['Lee', 학교.teacher]