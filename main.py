import matrix_multiplication
import generate_matrices


def main():
    '''
    The main function that initializes three matrices and
    solves for phi_hat using matrix multiplication and
    Gaussian Elimination

    :return: returns nothing
    '''
    # Initialize XT and X matrices
    XT = generate_matrices.generate_XT()
    X = generate_matrices.generate_X()
    Y = generate_matrices.generate_Y()

    # Multiply XT * X
    resultXTX = matrix_multiplication.multiply(XT, X)

    # Multiply XT * Y
    resultXTY = matrix_multiplication.multiply(XT, Y)

    # Augment the XTX | XTY matrices
    result = matrix_multiplication.augment_matrices(resultXTX, resultXTY)

    # For each row in the augmented matrix, perform Gaussian
    # Elimination steps:
    # 1) Find largest row and swap
    # 2) Scale
    # 3) Eliminate
    for row in range(0, len(result[0])):
        if row != len(result[0]) - 1:
            index = matrix_multiplication.find_largest_row_by_col \
                (result, len(result) - 1, len(result[0]), row)
            matrix_multiplication.swap_row(result, row, index)
        matrix_multiplication.scale_row(result, row, len(result))
        result[row][row] = 1

        matrix_multiplication.eliminate(result, row, len(result))

    # Backsolve simplified matrix
    matrix_multiplication.back_solve(result)

    # Get the phi_hat approximation formula
    matrix_multiplication.get_phi_hat(result)


if __name__ == "__main__":
    main()
