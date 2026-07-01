def build_profile(first, last, **user_info) :
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')

user_profile = build_profile('Lebron', 'James', team='golden state warriors',
                             position='SF', height="6'9")
print(user_profile)