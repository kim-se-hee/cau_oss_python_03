"""
figure 모듈은 도형의 넓이를 구하는데 도움을 주는 모듈입니다
모듈 안에는 선과 관련된 line 클래스와
넓이를 구하는 여러 함수들로 구성되어 있습니다
line 클래스는 생성자 또는 setter를 이용해 선의 길이를 정해줄 수 있으며 getter를 통해 선의 길이를 반환할 수도 있습니다
함수로는 정사각형 원 정삼각형의 넓이를 구할 수 있습니다
"""
import math

class line:
    """
    멤버 변수로는 length가 있고 이는 private으로 선언이 되어 외부 참조가 자유롭지 않습니다
    생성자나 setter 통해 length를 설정할 수 있습니다
    getter를 통해 length의 값을 받을 수도 있습니다
    """
    __length = 0
    def __init__(self, length):
        """
        생성자
        멤버 변수를 초기화
        매개변수로는 길이인 length가 있다
        """
        self.__length = length
    
    def set_length(self, length):
        """
        setter
        멤버 변수의 값을 설정
        매개변수로는 길이인 length가 있다
        """
        self.__length = length

    def get_length(self):
        """
        getter
        멤버 변수의 현재 값을 반환
        매개변수는 없다
        """
        return self.__length

    
def area_square(length):
    """
    한변의 길이를 입력하면 정사각형의 넓이를 반환
    매개변수로는 길이인 length가 있다
    """
    return length**2

def area_circle(length):
    """
    한변의 길이를 입력하면 원의 넓이를 반환
    매개변수로는 길이인 length가 있다
    """
    return length**2*math.pi    
    
def area_regular_triangle(length):
    """
    한변의 길이를 입력하면 정삼각의 넓이를 반환
    매개변수로는 길이인 length가 있다
    """
    return (3**(1/2)) / 4 * (length**2)
