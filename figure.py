"""
figure 모듈은 도형의 넓이를 구하는데 도움을 주는 모듈입니다
모듈 안에는 선과 관련된 line 클래스와
넓이를 구하는 여러 함수들로 구성되어 있습니다
line 클래스는 생성자 또는 setter를 이용해 너비와 높이를 정해줄 수 있으며 getter를 통해 너비와 높이를 반환할 수도 있습니다
함수로는 직사각형 타원 직각삼각형의 넓이를 구할 수 있습니다
"""
import math

class line:
    """
    멤버 변수로는 width, height가 있고 이는 private으로 선언이 되어 외부 참조가 자유롭지 않습니다
    생성자나 setter 통해 width, height의 값을 설정할 수 있습니다
    getter를 통해 width, height의 값을 받을 수도 있습니다
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """
        생성자
        멤버 변수를 초기화
        매개변수로는 너비인 width와 높이인 height가 있다
        """
        self.__width = width
        self.__height = height
    
    def set_width(self, width):
        """
        setter
        멤버 변수 __width의 값을 설정
        매개변수로는 너비인 width가 있다
        """
        self.__width = width

    def get_width(self):
        """
        getter
        멤버 변수 __width의 현재 값을 반환
        매개변수는 없다
        """
        return self.__width
    
    def set_height(self, height):
        """
        setter
        멤버 변수 __height의 값을 설정
        매개변수로는 높이인 height가 있다
        """
        self.__width = height

    def get_height(self):
        """
        getter
        멤버 변수 __height의 현재 값을 반환
        매개변수는 없다
        """
        return self.__height

    
def area_rectangle(width, height):
    """
    가로가 width 세로가 height인 직사각형의 넓이를 반환
    매개변수로는 너비인 width와 높이인 height가 있다
    """
    if width <= 0 or height <= 0: 
        raise ValueError
    
    return width * height

    

def area_ellipse(width, height):
    """
    두 축이 2 * width, 2 * height인 타원의 넓이를 반환
    매개변수로는 축의 길이의 절반인 width와 height가 있다
    """
    if width <= 0 or height <= 0: 
        raise ValueError
    return width * height * math.pi    
   
    
def area_right_triangle(width, height):
    """
    밑변의 길이가 width 높이가 height인 직각삼각형의 넓이를 반환
    매개변수로는 밑변인 width와 높이인 height가 있다
    """
    if width <= 0 or height <= 0: 
        raise ValueError
    return width * height / 2
    
