import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


CV_TXT = '''
# 소개
- 이름: 이동현
- E-mail: dlehdgus0127@handapartners.com
- 육군 병장 만기전역(2015~2016)
- 관심 분야: 데이터 엔지니어링, 데이터 사이언스
# 학력
- 창원남고등학교 졸업(2010~2012)
- 한양대학교 수학과(경제금융학 부전공) 졸업(2013~2018)
- 한양대학교 경영대학 재무금융전공 석박사통합과정 재학중(2019~)
# 회사경력
- 한양비즈랩 quantitative analytics lab 인턴십(2018.09~2018.12)
- 한다파트너스 researcher(2019~)
# 활동
- NICE 신용평가 입문 교육 수료(2018)
- 제 16회 SAS 분석 챔피언십 입선(2018): 빅데이터를 활용한 교통사고 위험 구역 예측과 교통 안전을 위한 방안 도출 
- 한양대학교 경영대학 프로젝트 제안 공모전 우수(2018)
- 한양대학교 자연과학대학 학술 활동 발표 장려(2018): 통계적 방법론과 머신러닝을 이용한 열람실 이용인원 예측
- 데이터 분석 준전문가
- 컴퓨터 활용능력 2급
# 연구중인 분야
- Do Some Bitcoin Exchanges Lead the Others? An Empirical Analysis ‘in preparation’ 
- Agnostic fundamental analysis works in Korea ‘in preparation’ 
- Han, M., Lee, D. H., & Kang, H. G. (2020). Market anomalies in the Korean stock market. Journal of Derivatives and Quantitative Studies: Seonmul yeon’gu.
'''


def create_layout():
    return html.Div(
        [
            html.Div(
               [], className='col-2'
            ),
            html.Div(
               dcc.Markdown(CV_TXT), className='col-8'
            ),
            html.Div(
               [], className='col-2'
            )
        ],
        className='row',
        style={
            "padding": "1%", 'align-items': 'center', 'color': '#C9C8BF'
        }
    )
