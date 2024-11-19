# 사용자 정보 저장용 변수
user_info = {"school": None, "department": None, "year": None}

def save_user_info(school, department, year):
    """사용자 정보를 저장하는 함수"""
    user_info["school"] = school
    user_info["department"] = department
    user_info["year"] = year
    return f"저장된 정보: {school}, {department}, {year}"

def get_user_info():
    """저장된 사용자 정보를 반환"""
    return user_info
