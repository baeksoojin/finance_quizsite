# Samdasu
Description : 금융지식을 얻고 싶은 사람들을 위한 사이트

## 1. 실행방법

#### 서버 실행방법
###### backend, frontend
- manage.py와 동일한 위치에서 진행
``` c
python manage.py runserver
```


###### 데이터베이스 모델 저장 및 적용
- manage.py와 동일한 위치에서 진행
``` c
python manage.py makemigrations
python manage.py migrate
```

## 2. 구현현황

### 홈페이지
<img width="1512" alt="스크린샷 2022-05-19 오전 3 36 54" src="https://user-images.githubusercontent.com/74058047/169121083-721fd19a-7284-49a5-9fc8-0c800d4dd4a7.png">
<img width="1512" alt="스크린샷 2022-05-19 오전 3 37 12" src="https://user-images.githubusercontent.com/74058047/169121094-b9c4b0aa-982f-4ecf-82a3-fdb8cf227c88.png">

### 단어암기 페이지
<img width="1512" alt="스크린샷 2022-05-19 오전 3 37 28" src="https://user-images.githubusercontent.com/74058047/169121103-1e2bf094-15aa-4b61-a3cf-1fd0cec6dbe8.png">
- 5개의 금융관련 단어를 랜덤으로 보여줍니다.
- change 버튼을 누를경우, 새로운 단어들이 제공됩니다.
- quiz 버튼을 누를경우, 아래와 같습니다.
<img width="1512" alt="스크린샷 2022-05-19 오전 3 37 44" src="https://user-images.githubusercontent.com/74058047/169121114-b7591409-558a-43ab-add3-275826619302.png">
- quiz는 외우던 5개의 단어로 문제를 제공합니다.
<img width="1512" alt="스크린샷 2022-05-19 오전 3 37 57" src="https://user-images.githubusercontent.com/74058047/169121128-919e71a0-b24d-4aa8-ba24-c47e1efdd6c1.png">
- 맞은 개수와 체점결과를 보여줍니다.
