# Google-Translation-API
在网上发现该 API 后通过, 将其中的 JS 转为了 Python

## 一些示例
`print(cn_to_en("中文"))`
```
[[['Chinese', '中文', None, None,
2], [None, None, None, 'Zhōngwén']], [['名词', ['Chinese'], [['Chinese', ['中文', '汉语', '华人', '华
语', '汉'], None, 0.56094915]], '
中文', 1]], 'zh-CN', None, None, [['中文', None, [['Chinese', 1000,
True, False]], [[0, 2]], '中文', 0, 0]], 0.58841187, [], [['zh-CN',
'ja'], None, [0.58841187, 0.41158813], ['zh-CN', 'ja']]]
```

`print(en_to_cn("chinese"))`
```
[[['中文', 'chinese', None, None,
2], [None, None, 'Zhōngwén']], [['名词', ['中文', '汉语', '华人', '
华语', '汉'], [['中文', ['Chinese'], None, 0.12713574], ['汉语', ['Chinese'], None, 0.034756977], ['华
人', ['Chinese', 'ethnic Chinese', 'Chinaman'], None, 0.010600278],
['华语', ['Chinese'], None, 0.0042828997], ['汉', ['Chinese', 'Han Dynasty', 'man', 'fellow'], None, 0.0036633583]], 'Chinese', 1], ['形
容词', ['中国的', '中国话的', '中
华的'], [['中国的', ['Chinese', 'China']], ['中国话的', ['Chinese']], ['中华的', ['Chinese']]], 'Chinese', 3]], 'en', None, None, [['chinese', None, [['中文', 1000, True, False], ['中国人', 0, True, False], ['中国', 0, True, False]], [[0, 7]], 'chinese', 0, 0]], 0.98046875, [], [['en'], None, [0.98046875], ['en']], None, None, None, [['形
容词', [['relating to China or its language, culture, or people.', 'm_en_gbus0177150.005']], 'Chinese'], ['名词', [['the Sino-Tibetan language of China.', 'm_en_gbus0177150.010'], ['a native or inhabitant of China, or a person of Chinese
descent.', 'm_en_gbus0177150.013']], 'Chinese']]]
```

`print(cn_to_en("COVID-19 终将被战胜"))`
```
[[['COVID-19 will eventually be defeated', 'COVID-19 终将被战胜', None, None, 3, None, None, [[]], [[['51171d70a5b6c2485a24361038890141', 'zh_en_2020q2.md']]]], [None, None, None, 'COVID-19 zhōng jiāng bèi zhànshèng']], None, 'zh-CN', None, None, [['COVID-19 终将被战胜',
None, [['COVID-19 will eventually
be defeated', 0, True, False], ['COVID-19 will eventually be overcome', 0, True, False]], [[0, 14]], 'COVID-19 终将被战胜', 0, 0]], 1.0, [], [['zh-CN'], None, [1.0], ['zh-CN']]]
```

`print(en_to_cn("COVID-19 will eventually be defeated"))`

```
[[['COVID-19最终将被击败', 'COVID-19 will eventually be defeated', None, None, 3, None, None, [[]], [[['b3ad15e7a0073e77814019b341d18493', 'en_zh_2019q3.md']]]], [None, None, 'COVID-19 zuìzhōng jiāng bèi
jíbài']], None, 'en', None, None,
[['COVID-19 will eventually be defeated', None, [['COVID-19最终将被
击败', 0, True, False], ['COVID-19最终将被打败', 0, True, False]], [[0, 36]], 'COVID-19 will eventually be defeated', 0, 0]], 1.0, [], [['en'], None, [1.0], ['en']]]
```
