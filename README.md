# scrapy_demo

* 팀원
  - 한성필, 한승호
  
* 프로젝트 설명
  - 삼성전자의 주식 정보를 네이버 금융에서 가져와 mysql에 삽입하기
  - 가지고 오는 정보
    - 종목 코드
    - 거래량
    - 현재 가격
    - 고가
    - 저가

* 프로그램 설명
  - anaconda와 scrapy를 사용하여 개발
    - anaconda와 scrapy를 사전에 설치해야 함
    - 기본적으로 my_python_env 아나콘다 가상환경을 사용하도록 설정됨
      - 필요시 가상환경은 stockscrap/regist_schedule.bat 파일에서 수정하여 사용
  - stockscrap/regist_schedule.bat 파일을 실행시키면 자동으로 윈도우 스케줄러에 10분마다 크롤링을 수행하도록 등록
    - 필요시 파일 내에서 시간을 수정하여 사용
  
  
