import numpy as np
from src.main.common import SFunction
from src.main.common import BinomialCoefficientsFunction

class OverlapIntegral:

    def __init__(self, basis_set_array):
        self.basis_set_array = basis_set_array

    def calculate(self, i, j):
        s_ij = 0
        if i == j:
            return 1.00
        else:
            basis_coefficients_i = self.basis_set_array[i].get_array_of_coefficients()
            print(basis_coefficients_i)
            basis_coefficients_j = self.basis_set_array[j].get_array_of_coefficients()
            r_a = self.basis_set_array[i].get_coordinates()
            r_b = self.basis_set_array[j].get_coordinates()
            r_ab = np.linalg.norm(r_a - r_b)
            for a in range(0, len(basis_coefficients_i)):
                for b in range(0, len(basis_coefficients_j)):
                    if self.basis_set_array[i].get_orbital_type() == 'S' and self.basis_set_array[j].get_orbital_type() == 'S':
                        a_1 = basis_coefficients_i[a][1]
                        a_2 = basis_coefficients_j[b][1]
                        c_1 = basis_coefficients_i[a][0]
                        c_2 = basis_coefficients_j[b][0]
                        n_1 = ((2 * a_1) / np.pi)**(3/4)
                        n_2 = ((2 * a_2) / np.pi)**(3/4)
                        r_p = (a_1 * r_a + a_2 * r_b) / (a_1 + a_2)

                        s = SFunction(BinomialCoefficientsFunction)

                        r_pa_xyz = r_a - r_p
                        r_pb_xyz = r_b - r_a
                        gamma = a_1 + a_2
                        s_x = s.calc(0, 0, r_pa_xyz.item(0), r_pb_xyz.item(0), gamma)
                        s_y = s.calc(0, 0, r_pa_xyz.item(1), r_pb_xyz.item(1), gamma)
                        s_z = s.calc(0, 0, r_pa_xyz.item(2), r_pb_xyz.item(2), gamma)
                        s_ij += c_1 * c_2 * n_1 * n_2 * (np.pi / gamma)**(3/2) * np.exp(- a_1 * a_2 * r_ab**2 / gamma) * s_x * s_y * s_z
                    else:
                        s_ij += 0
            return s_ij