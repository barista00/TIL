// html 안에 test.jpg를 보여주고 있는 이미지 태그가 있다고 칩시다. 
// 이미지를 new.jpg 라는 이미지로 바꾸고 싶으면 자바스크립트 코드를 어떻게 짜야할까요?
// 성공여부는 크롬 개발자도구 켜면 src 속성이 잘 바뀌었는지 확인가능하겠죠?
let img = document.querySelector('#image')
if (img instanceof HTMLImageElement) {
  img.src = 'new.jpg'
}

// 3개의 링크가 있는데 이 요소들의 href 속성을 전부 https://kakao.com으로 바꾸고 싶은 겁니다.
// 자바스크립트 코드를 어떻게 짜야할까요? 
let link = document.querySelectorAll('.naver')
link.forEach ((a) => {
  if (a instanceof HTMLAnchorElement) {
    a.href = 'https://kakao.com'
  }
})