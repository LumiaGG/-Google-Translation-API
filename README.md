# Google-Translation-API
在网上发现该 API 后通过, 将其中的 JS 转为了 Python

## 一些示例
`print(cn_to_en("中文"))`
```
[[['Haha', '哈哈', None, None, 3,
None, None, [[]], [[['51171d70a5b6c2485a24361038890141', 'zh_en_2020q2.md']]]], [None, None, None, 'Hāhā']], None, 'zh-CN', None, None,
[['哈哈', None, [['Haha', 0, True, False]], [[0, 2]], '哈哈', 0, 0]], 1.0, [], [['zh-CN'], None, [1.0], ['zh-CN']]]
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
