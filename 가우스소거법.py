import numpy as np

def gaussian_elimination(A, b):
    """
    가우스 소거법을 사용하여 선형 시스템의 해를 찾는 함수

    Parameters:
    - A: 계수 행렬
    - b: 상수 벡터

    Returns:
    - x: 해 벡터
    """

    # 행렬 A와 벡터 b를 확장 행렬로 합침
    augmented_matrix = np.column_stack((A, b))

    # 전진 소거(forward elimination)
    n = len(b)
    for i in range(n):
        # 현재 행의 대각 원소를 1로 만듦
        pivot_row = augmented_matrix[i] / augmented_matrix[i, i]
        augmented_matrix[i] = pivot_row

        # 현재 행을 제외한 다른 행에서 현재 열의 값을 0으로 만듦
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * pivot_row

    # 해 벡터 추출
    x = augmented_matrix[:, -1]

    return x

# 예제 데이터
A = np.array([[2, -1, 1],
              [1, 1, -1],
              [3, 1, 3]])

b = np.array([8, -2, 10])

# 가우스 소거법으로 해 찾기
solution = gaussian_elimination(A, b)

print("Solution:", solution)
