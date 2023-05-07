// 다음 타입을 변환기 돌려보십시오.
// type Bus = {
//   color : string,
//   model : boolean,
//   price : number
// }
// 동료가 잘못 만든 타입입니다.
// color, model, price 속성은 전부 string 또는 number 타입이어야합니다.
// 1. 변환기 하나 만드시고
// 2. 기존 Bus 타입을 변환기 돌려서 위 조건을 충족하는 새로운 타입을 하나 만들어보십시오.
type Bus = {
  color : string,
  model : boolean,
  price : number
}
type Changer<T> = {
  [key in keyof T] : string | number
}
type NewBus = Changer<Bus>
let bus :NewBus= {
  color : 'red',
  model : 'a-10',
  price : 100
} 


// 이런 변환기는 어떻게 만들어야할까요?
// object안에 들어있는 모든 속성을
// string, number 이렇게 고정된 타입으로 변환해주는게 아니라
// 내가 원하는 타입을 입력하면 그걸로 변환해주는 범용성 좋은 변환기를 만들어보십시오.
type AnnyType = {
  country : string,
  number : number,
}
type TypeChanger<T, Type> = {
  [key in keyof T] : Type
}
type NewAnnyType = TypeChanger<AnnyType, string>

let annoymous :NewAnnyType= {
  country : 'Korea',
  number : '+82'
}