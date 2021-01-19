import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from main import app


CV_TXT = '''
## Intro
- Name: Dong-Hyun Lee
- E-mail: lee@donghyun.app
- Discharged upon completing military service(2015~2016)
- Interests: Data-science, data-analysis
- Hobby: Knowledge integration, Keyboard
## Education
- Changwon-Nam High School (2010~2012)
- Hanyang University Department of Mathematics (Economics and Finance Minor) Bachelor(2013~2018)
- Hanyang University Business School (Finance) Ph.D. student(2019~)
## Career
- Hanyang Biz-lab quantitative analytics internship(2018.09~2018.12)
- Handa-partners researcher(2019~)
## Research
- Han, M., Lee, D. H., & Kang, H. G. (2020). Market anomalies in the Korean stock market. Journal of Derivatives and Quantitative Studies: Seonmul yeon’gu.
- Do Some Bitcoin Exchanges Lead the Others? An Empirical Analysis ‘in preparation’ 
- Agnostic fundamental analysis works in Korea ‘in preparation’ 
## Activity
- Advanced Data Analytics Semi-Professional(ADsP)
- NICE Completion of introductory credit rating training(2018)
- SAS analysis championship Participation Award(2018): Prediction of dangerous areas of traffic accidents using big data and derivation of measures for traffic safety
- Hanyang University Business School Project Proposal Competition Excellence award(2018)
- Hanyang University College of Natural Sciences Academic Activities Participation Award(2018): Predicting number of library users using statistical methodology and machine learning
'''


def create_layout():
    return html.Div([
        html.Div(
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
        ),
        dbc.Row([
            dbc.Col([], md=8),
            dbc.Col([
                dbc.Row([
                    dbc.Col(html.A([
                        html.Img(
                            src=app.get_asset_url('GitHub-Mark-Light-120px-plus.png'),
                            height='60 px',
                            width='auto')
                    ], href='https://github.com/movinghyun', target='_blank'), md=3),
                    dbc.Col(html.A([
                        html.Img(
                            src=app.get_asset_url('LI-In-Bug.png'),
                            height='60 px',
                            width='auto')
                    ], href='https://www.linkedin.com/in/movinghyun', target='_blank'), md=3),
                    dbc.Col(html.A([
                        html.Img(
                            src=app.get_asset_url('youtube_social_icon_red.png'),
                            height='60 px',
                            width='auto')
                    ], href='https://www.youtube.com/channel/UCDtjhl3QW1IEtf0TQr9i4mQ', target='_blank'), md=3),
                ])
            ], md=2),
            dbc.Col([], md=2)
            ], style={
                "padding": "1%", 'align-items': 'center', 'color': '#C9C8BF'
            }),
        ])
