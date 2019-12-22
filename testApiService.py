import unittest

from apiservice import ApiService

class TestApiService(unittest.TestCase):

    def setUp(self):
        self.s1 = ApiService()

    def testEmotionAnalysis(self):
        self.assertEqual(self.s1.emotionAnalysis(0, "누구인가? 누가 어려운 소리를 내었는가?"), {'result':'success','prob': 87, 'emotion': '부정'})
        self.assertEqual(self.s1.emotionAnalysis(1, "누구인가? 누가 어려운 소리를 내었는가?"), {'result':'success','prob': 74, 'emotion': '분노'})
        self.assertEqual(self.s1.emotionAnalysis(0, ""), '잠시 후 다시 이용해주세요.')


    def testFormatReturnValue(self):
        dic1 = {'label': '긍정', 'score': 0.9999995231628418, 'query': '한국의 가을은 매우 아름답습니다.', 'type': '감성분석'}
        self.assertEqual(self.s1.formatReturnValue(dic1),
                         {'result':'success','prob': 99, 'emotion': '긍정'})
        dic2 = {'type': '감정분석', 'query': '한국의 가을은 매우 아름답습니다.', 'Result': [[0.9482486844062805, '신뢰']]}
        self.assertEqual(self.s1.formatReturnValue(dic2),
                         {'result':'success','prob': 94, 'emotion': '신뢰'})


if __name__ == '__main__':
    unittest.main()
