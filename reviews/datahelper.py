from flask import g

# def add_customer(c):
#     db.append(c)

# def create_product(name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         insert into product
#         (name, price)
#         values
#         (%s, %s)  
#         ''',
#         (name, price)
#     )
#     new_id = cur.lastrowid
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (new_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def get_products():
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product
#         '''
#     )
#     ret_dicts = cur.fetchall()

#     return ret_dicts



# def is_product_id_existed(product_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product where product_id=%s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict != None

# def get_product(product_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product where product_id=%s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict

# def update_product(product_id, name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         update product
#         set name=%s, price=%s
#         where product_id=%s 
#         ''',
#         (name, price, product_id)
#     )
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def delete_product(product_id):
    # cur = g.cursor()
    # cur.execute(
    #         '''
    #         delete from product where product_id=%s
    #         ''',
    #         (product_id)
    #     )
 
    # rowcount = cur.rowcount
    
    # return rowcount > 0




def is_restaurant_id_existed(restaurant_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from restaurants where restaurant_id=%s
        ''',
        (restaurant_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

def create_review(restaurant_id, rating, comment):
    cur = g.cursor()
    cur.execute(
        '''
        insert into reviews
        (restaurant_id, rating, comment, created_at)
        values
        (%s, %s, %s, now())  
        ''',
        (restaurant_id, rating, comment)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from reviews where review_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def get_reviews(restaurant_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from reviews where restaurant_id=%s
        ''',
        (restaurant_id)
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def get_reviews_stats(restaurant_id):
    cur = g.cursor()
    cur.execute(
        '''
        select avg(rating) as avg_rating from reviews where restaurant_id=%s
        group by restaurant_id
        ''',
        (restaurant_id)
    )
    ret_dict = cur.fetchone()

    if ret_dict == None:
        return None
    else:
        return ret_dict['avg_rating']

def is_review_id_existed(review_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from reviews where review_id=%s
        ''',
        (review_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None


def delete_review(review_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from reviews where review_id=%s
            ''',
            (review_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0