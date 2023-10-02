餐廳評價系統API

新增評價：POST /api/reviews

接受JSON格式的評價資料，包括餐廳ID、評價分數、評語等。

回傳新評價的唯一識別碼。

獲取餐廳評價：GET /api/reviews/<restaurant_id>

接受餐廳ID，回傳特定餐廳的評價列表。

獲取評價統計：GET /api/reviews/stats/<restaurant_id>

接受餐廳ID，回傳特定餐廳的評價統計資訊，例如平均分數、評價數量等。

刪除評價：DELETE /api/reviews/<review_id>

接受評價的唯一識別碼，刪除指定評價。

所有的API：
| 方法 | 端點 | 描述 |

|--------|-------------------------------|-----------------------|

| POST | /api/reviews | 新增評價 |

| GET | /api/reviews/<restaurant_id> | 獲取餐廳評價列表 |

| GET | /api/reviews/stats/<restaurant_id> | 獲取評價統計資訊 |

| DELETE | /api/reviews/<review_id> | 刪除評價 |

需要的資料表格與欄位：
我們需要以下資料表格和欄位來支援這些API：

餐廳資料表 (restaurants)

restaurant_id (PK)：餐廳的唯一識別碼

name：餐廳名稱

address：餐廳地址

phone：餐廳聯絡電話

…

評價資料表 (reviews)

review_id (PK)：評價的唯一識別碼

restaurant_id (FK)：餐廳的唯一識別碼 (與餐廳資料表關聯)

rating：評價分數 (通常是1到5的範圍)

comment：評語

created_at：評價建立時間# restaurant_reviews
