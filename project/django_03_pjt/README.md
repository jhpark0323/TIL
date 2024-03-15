# 03_pjt

1. bootstrap을 활용

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<!-- head 마지막줄 -->

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
<!-- body 마지막줄 -->
```
2. nav 가져와서 수정

```html
<nav style="position: fixed; top: 0; width: 100%;" class="navbar navbar-expand-lg bg-body-tertiary">
<!-- style의 position: fixed, top: 0으로 스크롤을 내려도 위에 고정, width: 100%로 nav바가 전체 크기에 맞게 설정됨 -->
```

3. nav에서 글자를 누르면 해당 div로 이동

```html
<a class="nav-link" aria-current="page" href="#aboutme">About Me</a>
<!-- href="#aboutme" 를 이용한 id가 aboutme인 곳으로 이동  -->
```

4. 제목의 display: flex로 가운데 정렬

```html
<h1 class="gaegu-regular m-2" style="padding-top: 60px; font-size: 65px; display: flex; justify-content: center;">박재현 포트폴리오</h1>
```

5. container class와 row, col 이용

```html
<div class="container">
  <div class="standard row content">
    <div class="col">
      <div>이름 : 박재현</div>
      <div>주소 : 부산</div>
      <div>이메일 : brianwogus@naver.com</div>
    </div>
    <div class="col">
      <div>생년월일 : 1999.03.23</div>
      <div>연락처 : 010-6300-1386</div>
      <div>학력 : 부경대학교(응용수학과/빅데이터 융합전공)</div>
    </div>
  </div>
</div>
```

추가적인 Tip!
- 구글 폰트 설정  
  https://fonts.google.com/?subset=korean&noto.script=Kore
  위 사이트를 이용해 import 해서 사용
  import는 무조건 맨 윗줄에!! -> 아니면 import 안됨

  ```css
  @import url('https://fonts.googleapis.com/css2?family=Madimi+One&family=Nanum+Pen+Script&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Gaegu&family=Madimi+One&family=Nanum+Pen+Script&family=Sunflower:wght@300&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Gaegu&family=Madimi+One&family=Nanum+Pen+Script&family=Sunflower:wght@300&display=swap');

  .standard {
    font-family: "Nanum Pen Script", cursive;
    font-weight: 400;
    font-style: normal;
    font-size: 30px;
  }

  .black-han {
    font-family: "Black Han Sans", sans-serif;
    font-weight: 400;
    font-style: normal;
  }


  .gaegu-regular {
    font-family: 'Gaegu';
    font-style: normal;
    font-weight: 400;
  }
  ```

- 외부css파일 참조
  ```html
  <link rel="stylesheet" href="./style.css">
  ```