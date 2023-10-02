from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from reviews import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("reviews", import_name = "reviews")


@blueprint.route('/add_review', methods=["POST"])
def add_review():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.AddReview, x, config=config)
    #2. 驗證資料
    #2.1. restaurant_id是否存在
    if datahelper.is_restaurant_id_existed(obj.restaurant_id) == False:
        return json.jsonify(errors.e1001)
    #2.2. rating介於1~5之間
    if obj.rating < 1 or obj.rating > 5:
        return json.jsonify(errors.e1002)
    #2.3. comment<=45個字
    if obj.comment != None and len(obj.comment) > 45:
        return json.jsonify(errors.e1003)

    #3. 建立review
    #3.1. 建立review
    s = datahelper.create_review(obj.restaurant_id, obj.rating, obj.comment)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳review
    return json.jsonify(make_data_result(s))

@blueprint.route('/get_reviews', methods=["POST"])
def get_reviews():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.GetReviews, x, config=config)

    #2. 驗證資料
    #2.1. 驗證restaurant_id是否存在
    if datahelper.is_restaurant_id_existed(obj.restaurant_id) == False:
        return json.jsonify(errors.e2001)

    #3. 取得reviews
    s = datahelper.get_reviews(obj.restaurant_id)
    #4. 回傳reviews
    return json.jsonify(make_data_result(s))

@blueprint.route('/get_reviews_stats', methods=["POST"])
def get_reviews_stats():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.GetReviewsStats, x, config=config)

    #2. 驗證資料
    #2.1. 驗證restaurant_id是否存在
    if  isinstance(obj.restaurant_id, int) == False or \
          datahelper.is_restaurant_id_existed(obj.restaurant_id) == False:
        return json.jsonify(errors.e3001)

    #3. 取得reviews的統計資料
    s = datahelper.get_reviews_stats(obj.restaurant_id)
    #4. 回傳reviews的統計資料
    return json.jsonify(make_data_result({"avg_rating":s}))

@blueprint.route('/delete_review', methods=["POST"])
def delete_review():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.DeleteReview, x, config=config)
    
    #2. 驗證資料
    #2.1. 驗證review_id是否存在
    if  isinstance(obj.review_id, int) == False or \
          datahelper.is_review_id_existed(obj.review_id) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_review(obj.review_id)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))