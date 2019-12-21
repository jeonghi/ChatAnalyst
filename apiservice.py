# -*- coding: utf-8 -*-

import json
import requests


class ApiService:
    # private 로  키 값과 서버 기본 Url
    __key = "8126976894976747987"
    __baseURL ="http://api.adams.ai/datamixiApi/omAnalysis"
    __headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }

    def __init__(self):
        self.params = {'key': ApiService.__key}

    def emotionAnalysis(self, type, query):
        #보낼 데이터 셋팅.
        if type == 0:
            self.params['type'] = type
        elif type == 1:
            self.params['type'] = type

        self.params['query'] = query

        # 서버통신
        response = requests.get(ApiService.__baseURL, headers=ApiService.__headers, params=self.params)
        result = response.json()

        if result['result_code'] == 'success':
            # 결과값 dic 형태로 리턴.
            return self.formatReturnValue(result['return_object'])
        else:
            # 결과 코드가 실패일 경우 상황에 맞는 에러 메세지 리턴.
            return {'result':'fail', 'msg': result['error_msg']}

    def formatReturnValue(self, resultDic):
        tempDic={}

        if resultDic['type'] == '감성분석':
            score = int(resultDic['score']*100)
            label = resultDic['label']

        elif resultDic['type'] == '감정분석':
            score = int(resultDic['Result'][0][0]*100)
            label = resultDic['Result'][0][1]
        tempDic['result'] = 'success'
        tempDic['prob'] = score
        tempDic['emotion'] = label
        return tempDic


if __name__ == "__main__":
    r = ApiService().emotionAnalysis(0, '한국의 가을은 매우 아름답습니다.')
    print(r)
