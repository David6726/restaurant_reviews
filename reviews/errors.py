from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給add_review API使用的error
e1001 = make_error_result("e1001","restaurant_id不存在")
e1002 = make_error_result("e1002","rating需介於1~5之間")
e1003 = make_error_result("e1003","comment需<=45個字")

#給get_reviews API使用的error
e2001 = make_error_result("e2001","restaurant_id不存在")

#給get_reviews_stats API使用的error
e3001 = make_error_result("e3001","restaurant_id不存在")

#給delete_review API使用的error
e4001 = make_error_result("e4001","review_id不存在")