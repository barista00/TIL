// Q1. for of 반복문을 이용해서
// 2단부터 9단까지의 구구단을 콘솔창에 한번 출력해보십시오.
const arr = [1,2,3,4,5,6,7,8,9]
for (let num of arr.slice(1)) {
  for (let num2 of arr) {
    console.log(`${num} X ${num2} = ${num * num2}`)
  }
}

var products = [
  {
    name1 : 'chair',
    price1 : 7000,
  },
  {
    name2 : 'sofa',
    price : 5000,
  },
  {
    name1 : 'desk',
    price3 : 9000,
  },
]; 
// Q2. 어떤 놈이 object자료의 key값에 오타를 섞어놨습니다.
// key값 마지막 문자에 한자릿수 숫자가 섞여있으면 그걸 다 제거하고 싶습니다. 
// 어떻게 코드를 짜면 될까요? 

// 방법1
// for (let product of products) {
//   for (let data in product) {
//     if (data.slice(-1) <= '9') {
//       let newValue = product[data]
//       let newKey = data.slice(0, -1)
//       product[newKey] = newValue
//       delete product[data]
//     }
//   }
// }
// console.log(products)

// 방법2
for (let product of products) {
  for (let data in product) {
    if (isNaN(parseInt(data.slice(-1))) === false) {
      let newValue = product[data]
      let newKey = data.slice(0, -1)
      product[newKey] = newValue
      delete product[data]
    }
  }
}
console.log(products)