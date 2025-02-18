import yaml


class __XArmDynamics(object):
    CONFIG_NAME = None
    MASS = []
    ORIGIN = []
    INERTIA = []
    
    @classmethod
    def gen(cls):
        data = {}
        for i in range(len(cls.MASS)):
            data['link{}'.format((i + 1))] = {
                'mass': cls.MASS[i],
                'origin': {
                    'x': cls.ORIGIN[i][0],
                    'y': cls.ORIGIN[i][1],
                    'z': cls.ORIGIN[i][2]
                },
                'inertia': {
                    'ixx': cls.INERTIA[i][0],
                    'ixy': -cls.INERTIA[i][1],
                    'ixz': -cls.INERTIA[i][2],
                    'iyy': cls.INERTIA[i][3],
                    'iyz': -cls.INERTIA[i][4],
                    'izz': cls.INERTIA[i][5],
                },
            }
        try:
            with open(cls.CONFIG_NAME, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
            print('write {} success'.format(cls.CONFIG_NAME))
        except Exception as e:
            print('write {} exception, {}'.format(cls.CONFIG_NAME, e))


class XArm5x4Dynamics_HT_BR(__XArmDynamics):
    CONFIG_NAME = 'xarm5_type5_HT_BR.yaml'
    MASS = [2.177, 2.011, 2.01, 1.206, 0.17]
    ORIGIN = [
        [0.00015, 0.02724, -0.01357],
        [0.0367, -0.22088, 0.03356], 
        [0.06834, 0.22366, 0.00112],
        [0.06387, 0.02928, 0.0035],
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005433, -9.864E-06, 2.68E-05, 0.004684, 0.000826936, 0.0031118],
        [0.0271342, -0.004736, -0.00068673, 0.0053854, 0.0047834, 0.0262093],
        [0.0358513, 0.0040568, -0.0014346, 0.005795, -0.007516, 0.0343875],
        [0.0013483, 0.00042677, -0.00028758, 0.00175694, -1.244E-04, 0.002207],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm5x4Dynamics_HT_BR2(__XArmDynamics):
    CONFIG_NAME = 'xarm5_type5_HT_BR2.yaml'
    MASS = [2.3849, 2.164, 2.121, 1.3169, 0.17]
    ORIGIN = [
        [0.00013, 0.0294, -0.01239],
        [0.03788, -0.2254, 0.03447], 
        [0.06883, 0.22985, 0.00102],
        [0.06489, 0.03122, 0.00319],
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005705, -1.056E-05, 2.642E-05, 0.00489488, 0.000890795, 0.00334846],
        [0.0278053, -0.0048865, -0.000656695, 0.00551739, 0.00466808, 0.02692536],
        [0.0373639, 0.00417385, -0.00143647, 0.0058447, -0.0075398, 0.0359236],
        [0.00144315, 0.000455133, -0.000291878, 0.0018275, -1.32545E-04, 0.00231563],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm5x4Dynamics_HT_LD(__XArmDynamics):
    CONFIG_NAME = 'xarm5_type5_HT_LD.yaml'
    MASS = [2.459, 2.211, 2.158, 1.354, 0.17]
    ORIGIN = [
        [0.00013, 0.0301, -0.012], 
        [0.0382, -0.2266, 0.0347], 
        [0.069, 0.2318, 0.001], 
        [0.0652, 0.03179, 0.00311], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005795, -1.078E-05, -2.63E-05, 0.004969, 0.000911, 0.003428],
        [0.027996, -0.0049288, -0.0006482, 0.005557, 0.0046353, 0.02713],
        [0.037834, 0.0042102, -0.0014371, 0.005861, -0.007547, 0.036402],
        [0.001473, 0.00046355, -0.00029315, 0.00185, -1.35E-04, 0.0023493],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x4Dynamics_HT_BR(__XArmDynamics):
    CONFIG_NAME = 'xarm6_type6_HT_BR.yaml'
    MASS = [2.177, 2.011, 1.725, 1.211, 1.206, 0.17]
    ORIGIN = [
        [0.00015, 0.02724, -0.01357], 
        [0.0367, -0.22088, 0.03356], 
        [0.06977, 0.1135, 0.01163], 
        [-0.0002, 0.02, -0.026], 
        [0.06387, 0.02928, 0.0035], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005433, -9.864E-06, 2.68E-05, 0.004684, 0.000826936, 0.0031118],
        [0.0271342, -0.004736, -0.00068673, 0.0053854, 0.0047834, 0.0262093],
        [0.006085, 0.001500, -0.0009558, 0.0036652, -0.0018091, 0.0057045],
        [0.0046981, 6.486E-06, 1.404E-05, 0.0042541, 0.0002877, 0.00123664],
        [0.0013483, 0.00042677, -0.00028758, 0.00175694, -1.244E-04, 0.002207],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x4Dynamics_HT_BR2(__XArmDynamics):
    CONFIG_NAME = 'xarm6_type6_HT_BR2.yaml'
    MASS = [2.3814, 2.2675, 1.875, 1.3192, 1.33854, 0.17]
    ORIGIN = [
        [0.00022, 0.02951, -0.0124], 
        [0.03881, -0.22783, 0.03496], 
        [0.07041, 0.11631, 0.0107], 
        [-0.00018, 0.01798, -0.02291], 
        [0.0651, 0.03096, 0.00315], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.0058562, 1.79E-05, -3.55E-06, 0.0050316, 0.000888336, 0.003536652],
        [0.028315776, -0.005, -0.00066546, 0.0058, 0.0045741, 0.0273447],
        [0.0063483, 0.0015397, -0.00096858, 0.00379758, -0.00186567, 0.00595768],
        [0.004896, 6.925E-06, 1.418E-05, 0.00445694, 0.00023186, 0.00134332],
        [0.00146378, 0.000450624, -0.000284306, 0.00184192, -1.30866E-04, 0.002333524],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x4Dynamics_HT_LD(__XArmDynamics):
    CONFIG_NAME = 'xarm6_type6_HT_LD.yaml'
    MASS = [2.459, 2.211, 1.925, 1.36, 1.354, 0.17]
    ORIGIN = [
        [0.00013, 0.0301, -0.012], 
        [0.0382, -0.2266, 0.0347], 
        [0.0706, 0.11715, 0.0104], 
        [0.00018, 0.0177, -0.023], 
        [0.0652, 0.03179, 0.00311], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005795, -1.078E-05, -2.63E-05, 0.004969, 0.000911, 0.003428],
        [0.027996, -0.0049288, -0.0006482, 0.005557, 0.0046353, 0.02713],
        [0.0064294, 0.00155127, -0.0009724, 0.00384075, -0.00188257, 0.00603585],
        [0.004887, 6.996E-05, 1.334E-05, 0.0044147, 0.0002229, 0.0013373],
        [0.001473, 0.00046355, -0.00029315, 0.00185, -1.35E-04, 0.0023493],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x4Dynamics_HT2_LD(__XArmDynamics):
    CONFIG_NAME = 'xarm6_type6_HT2_LD.yaml'
    MASS = [2.459, 2.663, 2.27, 1.36, 1.354, 0.2136]
    ORIGIN = [
        [0.00013, 0.0301, -0.012], 
        [0.04096, -0.2363, 0.03154], 
        [0.0717, 0.1159, 0.00884], 
        [0.00018, 0.0177, -0.023], 
        [0.0652, 0.03179, 0.00311], 
        [0, -0.00704, -0.00993]
    ]
    INERTIA = [
        [0.005795, -1.078E-05, -2.63E-05, 0.004969, 0.000911, 0.003428],
        [0.02992763, -0.00528326, -0.000777505, 0.0063873, 0.00501448, 0.02868],
        [0.00672878, 0.00153395, -0.000989667, 0.0040289, -0.001857759, 0.00632038],
        [0.004887, 6.996E-05, 1.334E-05, 0.0044147, 0.0002229, 0.0013373],
        [0.001473, 0.00046355, -0.00029315, 0.00185, -1.35E-04, 0.0023493],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x5Dynamics_HT2_BR2(__XArmDynamics):
    """
    1M reach version, new Benrun, new HT motor at J3
    """
    CONFIG_NAME = 'xarm6_type8_HT2_BR2.yaml'
    MASS = [2.3814, 3.6325, 1.7269, 2.04, 1.325, 0.17]
    ORIGIN = [
        [0.00022, 0.02951, -0.0124], 
        [0.02539, -0.3017, -0.0032], 
        [0.07047, -0.11575, 0.012], 
        [-0.00022, 0.01039, -0.099],
        [0.0651, 0.03096, 0.00315], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.0058562, 1.79E-05, -3.55E-06, 0.0050316, 0.000888336, 0.003536652],
        [0.071521173, -0.010673573, -0.0020764, 0.009574546, 0.01384463, 0.069974876],
        [0.005889, -0.00137112, -0.00088143, 0.00359703, 0.001762155, 0.00543244],
        [0.004896, 6.925E-06, 1.418E-05, 0.00445694, 0.00023186, 0.00134332],
        [0.00146378, 0.000450624, -0.000284306, 0.00184192, -1.30866E-04, 0.002333524],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm7x3Dynamics_YT_SP(__XArmDynamics):
    CONFIG_NAME = 'xarm7_type3_YT_SP.yaml'
    MASS = [1.77, 1.51, 1.33, 1.43, 0.99, 0.9, 0.236]
    ORIGIN = [
        [0.00017, 0.02867, -0.00967], 
        [1E-05, -0.13885, 0.0139], 
        [0.04387, 0.02142, -0.00835], 
        [0.07059, 0.11905, 0.01071], 
        [-0.00014, 0.0234, -0.03053], 
        [0.06596, 0.00669, 0.00097], 
        [-3.5072E-05, 9.5542E-06, -0.022065]
    ]
    INERTIA = [
        [0.0039077, 2.49E-06, -1.69E-06, 0.0035025, -0.00054831, 0.0024964], 
        [0.0071397, 3.02E-06, -3.01E-05, 0.0026516, 0.001979, 0.0061118],
        [0.0023676, 0.00021885, 0.00049035, 0.0023241, 0.00025284, 0.0018927],
        [0.0046571, 0.0012392, -0.00056448, 0.0028189, -0.0011969, 0.0046273],
        [0.0042795, -3.42E-06, -1.61E-06, 0.004111, 0.00032311, 0.00092663],
        [0.0006881, 4.074E-05, -4.565E-05, 0.0010127, -3.39E-06, 0.0011106],
        [0.00018795, 2.4125E-07, 1.7234E-07, 0.00018921, -4.3124E-08, 0.00022645]
    ]

class XArm7x4Dynamics_HT_BR(__XArmDynamics):
    CONFIG_NAME = 'xarm7_type7_HT_BR.yaml'
    MASS = [2.177, 1.716, 1.4854, 1.574, 1.209, 1.214, 0.17]
    ORIGIN = [
        [0.00015, 0.02724, -0.01357], 
        [2.2E-04, -0.1247, 0.0189], 
        [0.046, -0.02229, -0.00847],
        [0.06976, -0.1125, 0.01318],
        [-0.00035, 0.0176, -0.02838], 
        [0.06365, 0.03084, 0.0217], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005433, -9.864E-06, 2.68E-05, 0.004684, 0.000826936, 0.0031118],
        [0.009158, -2.86E-06, -5.56E-06, 0.003666, 0.0030445, 0.00717573],
        [0.0029386, -0.000286, 0.00057699, 0.002522, -0.000309475, 0.00249567],
        [0.005601, -0.00133, -0.00086675, 0.0034567, 0.0016944, 0.00516],
        [0.005186, -1.4454E-05, -6.42E-07, 0.0048332, 2.748E-04, 0.0012837],
        [0.0013748, 0.000459, -2.907E-04, 0.001824, -1.3886E-04, 0.0022514],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm7x4Dynamics_HT_BR2(__XArmDynamics):
    CONFIG_NAME = 'xarm7_type7_HT_BR2.yaml'
    MASS = [2.382, 1.869, 1.6383, 1.7269, 1.3203, 1.325, 0.17]
    ORIGIN = [
        [-0.0002, 0.02905, -0.01233],
        [2.2E-04, -0.12856, 0.01735],
        [0.0466, -0.02463, -0.00768], 
        [0.07047, -0.11575, 0.012], 
        [-0.00032, 0.01604, -0.026], 
        [0.06469, 0.03278, 0.02141], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.0056905, 1.579E-05, -5.125E-06, 0.0049566, 0.000873378, 0.003316654],
        [0.0095989, -1.541E-06, -5.56E-06, 0.00382472, 0.00317156, 0.007565669],
        [0.00310955, -0.00030837, 0.00058453, 0.00264483, -0.000338893, 0.0026624],
        [0.005889, -0.00137112, -0.00088143, 0.00359703, 0.001762155, 0.00543244],
        [0.00534665, -1.5117E-05, 3.69E-07, 0.0049779, 2.2132E-04, 0.0013624],
        [0.0014745, 0.000488, -2.953E-04, 0.0019037, -1.4749E-04, 0.0023652],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm7x4Dynamics_HT_LD(__XArmDynamics):
    CONFIG_NAME = 'xarm7_type7_HT_LD.yaml'
    MASS = [2.459, 1.916, 1.6854, 1.774, 1.357, 1.362, 0.17]
    ORIGIN = [
        [0.00013, 0.0301, -0.012], 
        [0.0002, -0.12964, 0.01692], 
        [0.04676, -0.02526, -0.00746], 
        [0.07066, -0.11664, 0.0117], 
        [-0.00031, 0.01558, -0.0253], 
        [0.065, 0.03336, 0.02131], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005795, -1.078E-05, -2.63E-05, 0.004969, 0.000911, 0.003428],
        [0.0097184, -1E-06, -4.83E-06, 0.0038705, 0.0032, 0.007672145],
        [0.00315878, -3.1443E-04, 5.8658E-04, 0.002682, -3.469E-04, 0.0027105],
        [0.005967, -0.00138232, -0.00088544, 0.00363897, 0.0017806, 0.005509226],
        [0.005396, -1.5312E-05, -6.7E-07, 0.0050232, 0.00020544, 0.00138734],
        [0.0015057, 0.000496735, -2.9968E-04, 0.0019297, -1.5E-04, 0.0024],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x8Dynamics_HT_LD(__XArmDynamics):
    """
    800mm xarm6
    """
    CONFIG_NAME = 'xarm6_type11_HT_LD.yaml'
    MASS = [2.280, 2.545, 1.836, 1.41, 1.354, 0.17]
    ORIGIN = [
        [-0.00033, 0.02745, -0.014], 
        [0.04025, -0.3603, 0.0102], 
        [0.06865, -0.1133, 0.0132], 
        [0.00033, 0.0148, -0.0307], 
        [0.0652, 0.03179, 0.00311], 
        [0, -0.00677, -0.01098]
    ]
    INERTIA = [
        [0.005768, 1.6654E-05, -2.528E-06, 0.005052, 0.0008984, 0.003212],
        [0.076034, -8.6817E-03, -3.44615E-03, 0.0131983, 0.01936147, 0.068486],
        [0.0068547, -1.8093E-03, -0.001098, 4.08725E-03, 0.00212676, 0.0064999],
        [0.004887, 6.996E-05, 1.334E-05, 0.0044147, 0.0002229, 0.0013373],
        [0.001473, 0.00046355, -0.00029315, 0.00185, -1.35E-04, 0.0023493],
        [9.3E-05, 0.0, 0.0, 5.87E-05, 3.6E-06, 1.32E-04]
    ]

class XArm6x6Dynamics_HT_BR2(__XArmDynamics):
    """
    Lite6
    """
    CONFIG_NAME = 'xarm6_type9_HT_BR2.yaml'
    MASS = [1.411, 1.34, 0.953, 1.284, 0.804, 0.130]
    ORIGIN = [
        [-0.00036, 0.04195, -0.0025],
        [0.179, 0.0, 0.0584],
        [0.072, -0.0357, -0.001],
        [-0.002, -0.0285, -0.0813],
        [0.0, 0.010, 0.0019],
        [0.0, -0.00194, -0.0102]
    ]
    INERTIA = [
        [1451.64*1E-06, 12.4*1E-06, -6.7*1E-06, 887.3*1E-06, 125.5*1E-06, 1319.93*1E-06],
        [1585.4*1E-06, -6.766*1E-06, -1151.36*1E-06, 5609.7*1E-06, 1.14*1E-06, 4850*1E-06],
        [886.1*1E-06, -392.87*1E-06, 70.66*1E-06, 1578.5*1E-06, -24.45*1E-06, 1846.77*1E-06],
        [3705*1E-06, -2.0*1E-06, 7.17*1E-06, 3045.5*1E-06, -931.88*1E-06, 1541.3*1E-06],
        [566.8*1E-06, 0.6*1E-06, -5.3*1E-06, 507.7*1E-06, -0.48*1E-06, 530*1E-06],
        [77.26*1E-06, 1E-06, 0.4*1E-06, 85.665*1E-06, -0.6*1E-06, 148.14*1E-06]
    ]


if __name__ == '__main__':
    XArm5x4Dynamics_HT_BR.gen()
    XArm5x4Dynamics_HT_BR2.gen()
    XArm5x4Dynamics_HT_LD.gen()

    XArm6x4Dynamics_HT_BR.gen()
    XArm6x4Dynamics_HT_BR2.gen()
    XArm6x4Dynamics_HT_LD.gen()
    XArm6x4Dynamics_HT2_LD.gen()
    
    XArm6x5Dynamics_HT2_BR2.gen()

    XArm7x3Dynamics_YT_SP.gen()
    
    XArm7x4Dynamics_HT_BR.gen()
    XArm7x4Dynamics_HT_BR2.gen()
    XArm7x4Dynamics_HT_LD.gen()
    
    XArm6x8Dynamics_HT_LD.gen()
    
    XArm6x6Dynamics_HT_BR2.gen()
