#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# #### 請寫一個函式用來計算 Mean Square Error
# $ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $
# 
# ### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)

# # [作業目標]
# - 仿造範例的MAE函數, 自己寫一個MSE函數(參考上面公式)

# # [作業重點]
# - 注意程式的縮排
# - 是否能將數學公式, 轉換為 Python 的函式組合? (In[2], Out[2])

# In[1]:


# 載入基礎套件與代稱
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 定義 mean_squared_error 這個函數, 計算並傳回 MSE
# def mean_squared_error():
    """
    請完成這個 Function 後往下執行
    """
def mean_Square_Error(y,yp):
    """
    計算 MSE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mse: MSE
    """ 
    mse = MES = sum((y-yp)**2)/len(y)
    return mse


# In[8]:


# 與範例相同, 不另外解說
w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[4]:


# 與範例相同, 不另外解說
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[10]:


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))


# # [作業2]
# 
# 請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：
# 
# 1. 你選的這組資料為何重要
#    ANS:選擇Brazilian E-Commerce Public Dataset by Olist的資料包含消費紀錄ID,消費者ID,消費者居住洲別與城市等等, olist是巴西電商,利用這些資料分析消費者購買行為,消費者地理分布,及商品銷售狀況,消費者評分
#    可以了解商品流通情形改進物流,可以幫助做行銷決策之外,透過評分可以改善消費者使用體驗
# 
# 2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
#    ANS:提供者由olist電商公司公開資訊
# 
# 3. 蒐集而來的資料型態為何
# ANS:資料檔案為CSV檔,每個項目以列表的形式儲存
# 4. 這組資料想解決的問題如何評估
#    ANS:將評分透過文字雲的方式,顯示出最多評分的內容,而針對多數評分進行改進,透過消費者地理位置分析,可以評估物流是否有可以改進的流程,在觀察消費者消費習慣,發現其消費行為,進行預測與行銷決策
# 
# # [作業3]
# 
# 想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
# 
# 1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
#    Ans:假設車隊人員工作時間為彈性工時,客戶有需求時,會前往乘客指定的地點載客,透過app平台媒合駕駛與乘客外,車隊人員亦可以在路邊隨機載客
#    價格則依照照一邊計程車按里程與時間收費
#    提升業績則是提高載客量(一天中提歌載客的次數)
# 2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
#    Ans:資料可以由本公司app平台蒐集乘客乘車上下車地點,時間,行車距離,行車時間,消費者個人資料(性別,年齡,職業)
# 
# 3. 蒐集而來的資料型態為何
#    ANS:資料型態以列表分是紀錄每個項目
# 
# 4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
#    ANS:透過分析資料可以觀察尖峰時間與尖峰地點,車隊可以根據時間與地點出現,以提高載客率
# 
