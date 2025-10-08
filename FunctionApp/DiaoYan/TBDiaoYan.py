class TBDiaoYan(object):
    # 给出关键词后，在淘宝的市场调研
    # 1. 市场体量：分析淘宝上的商品数量、用户数量、订单数量等指标，了解市场规模和用户基础。
    # 2. 主要品牌：分析淘宝上的主要品牌，了解品牌知名度、用户忠诚度和市场份额。
    # 3. 主要品牌深度分析。品牌主要产品，主要产品的销量、销售额
    # 4. 关键词分析。关键词搜索量、搜索趋势、品牌词数量及搜索占比
    def __init__(self, name):
        self.name = name
    def DiaoYanTB(self, name):
        # 市场体量、主要品牌、主要品牌深度分析
        print('{} 进行了调研'.format(name))
        return name
