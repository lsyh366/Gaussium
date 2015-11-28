##Introduction
A basic quantum chemical program written in python using the numpy and scipy library and is currently at the very beginnings. My time is tight as I try to balance this between my job and real-life so development may go slowly.

Currently I'm looking to write HF in python and then to more accurate methods such as CI, CCSD and DFT. After this project is complete I may try out other languages such as Fortran, C, C++, Java, C# or even Haskell if I have the time.

I'm basing this work on Attlia Szabo and Neil S. Ostlunds "Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory". It is a old but well written book, and is by far the best introduction to the computational chemistry I have read. The only other textbook that comes close to this is probably Robert G. Parr and Weitao Yangs "Density Functional Theory of Atoms and Molecules". After this I intend to check out David B. Cooks "Handbook of Computational Chemistry" which appears to be quite in depth.

I must apologies for the bad/ugly code, I'm going to try refactor the code sometime in future and begin developing properly when I get more comfortable with writing and unit testing in python.

##Calculation of HeH<sup>+</sup> in STO-3G
Completed my first calculation of HeH<sup>+</sup> with a bond-length of 1.4632 a<sub>0</sub> using the STO-3G basis set. Below is the output from Spartan Student Edition v5,

    SCF model:
     A restricted Hartree-Fock SCF calculation will be
     performed using Pulay DIIS + Geometric Direct Minimization
    
     SCF total energy:      -2.8418365 hartrees
    
      Reason for exit: Successful completion 
      Quantum Calculation CPU Time :          .39
      Quantum Calculation Wall Time:         2.85

and the output from my program,
  
    ORBITAL COEFFICIENTS
    [[-0.87660574  0.79774813]
     [-0.20247895 -1.16783645]]
    
    TOTAL ENERGY: -2.841836483 a.u.
    
    
    Time Taken: 0.10287352007652968s

##Calculation of HeH<sup>+</sup> in 6-311+G**
Able to run calculations for all types of orbitals now, below shows the HeH+ molecule using the 6-311+G basis set which contains polarization functions for H and He. This calculation in particular takes quite a lot longer then Spartan and has a lot of inefficiencies that need sorting out. 
        
        SPARTAN STUDENT Quantum Mechanics Program:  (PC/x86)   Release  5.0.0v4
    
    Job type: Single point.
    Method: RHF
    Basis set: 6-311+G**
    Number of shells: 8
    Number of basis functions: 12
    Charge :     +1 
    Multiplicity: 1
    
    SCF model:
     A restricted Hartree-Fock SCF calculation will be
     performed using Pulay DIIS + Geometric Direct Minimization
    
     SCF total energy:      -2.9292278 hartrees
    
      Reason for exit: Successful completion 
      Quantum Calculation CPU Time :          .36
      Quantum Calculation Wall Time:          .42
    
    SPARTAN STUDENT Properties Program:  (PC/x86)                  Release  5.0.0  
      Use of molecular symmetry enabled
    
                         Cartesian Coordinates (Angstroms)
           Atom            X             Y             Z     
        ---------    ------------- ------------- -------------
    
      1 He He1          0.0000000     0.0000000     0.2580967
      2 H  H2           0.0000000     0.0000000    -0.5161934
    
  
and from my program,
    
    ORBITAL ENERGY EIGENVALUES
    [[-1.63347727  0.          0.          0.          0.          0.          0.          0.          0.          0.          0.          0.        ]
     [ 0.         -0.26339532  0.          0.          0.          0.          0.          0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.00716821  0.          0.          0.          0.          0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.19356385  0.          0.          0.          0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.51942552  0.          0.          0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.99158389  0.          0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.          1.24983604  0.          0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.          0.          1.27372407  0.          0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.          0.          0.          1.79599137  0.          0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.          0.          0.          0.          1.99898165  0.          0.        ]
     [ 0.          0.          0.          0.          0.          0.          0.          0.          0.          0.          2.63498222  0.        ]
     [ 0.          0.          0.          0.          0.          0.          0.          0.          0.          0.          0.          6.32406869]]
    
    ORBITAL COEFFICIENTS
    [[  2.58584881e-01   1.11419466e-01   2.73005263e-03  -7.48702927e-19  -1.50423550e-01  -2.17948523e-16  -3.72200990e-02  -2.43457458e-16  -3.57433126e-03   4.31291086e-17  -1.58309597e-01   1.50918881e+00]
     [  4.89277720e-01   2.18077259e-01  -2.54503646e-02  -3.89395314e-17  -1.02707500e+00  -1.71143424e-15  -1.44392943e-01  -1.33010178e-15  -1.11641553e+00  -1.07023484e-14  -8.32880510e-01  -2.39835532e+00]
     [  2.32338183e-01   7.71565750e-01  -3.74263305e-01   8.12637263e-17   2.19846827e+00   1.30572863e-15   5.38904289e-01   4.02502750e-15  -5.49526145e-01  -5.29239641e-15  -1.23816513e+00   5.47280694e-01]
     [ -1.25675432e-16   2.56879167e-17  -1.04247031e-16   8.03584886e-02  -9.91392876e-17  -5.13306318e-01   5.08038445e-15  -7.69007413e-01  -5.63271700e-15   8.22484898e-01   2.64406368e-16  -4.66076768e-16]
     [  6.53480280e-17  -1.62541951e-16  -3.27766428e-17   3.00963956e-01   1.68977446e-16  -5.92396533e-01  -1.27676743e-15   2.53213997e-01   5.17763633e-15  -6.77431289e-01   1.40030086e-15   1.78471452e-16]
     [ -3.66592789e-02   1.14004491e-02   2.56705689e-02   2.97908164e-17  -1.85959507e-01   9.46754943e-16  -9.76269455e-01  -7.36822876e-15   7.31784078e-01   7.11763402e-15   1.76790563e+00   6.57679110e-01]
     [  1.27877984e-01  -1.70963252e-01   1.37050368e-01  -6.19877633e-17   8.55676316e-02   5.03408197e-16   3.71779872e-01   2.10088016e-15  -9.93418756e-01  -8.23540608e-15   1.21321808e+00   3.36052584e-01]
     [  1.17371441e-01  -5.91943042e-01   1.39013492e+00   7.69131846e-17  -1.74032110e-01   1.63879483e-15  -1.50194617e+00  -1.04975903e-14   2.61898375e+00   2.31358612e-14   9.62907113e-01   7.54303786e-01]
     [ -1.49407535e-02  -8.12768101e-01  -1.34903802e+00  -8.21709122e-17  -1.00787879e+00  -1.70029375e-15   5.29569491e-01   3.87901327e-15  -6.64240646e-01  -5.17130086e-15   2.84762775e-01  -3.48352445e-01]
     [  2.17834896e-16   1.95532778e-18   1.01103199e-16   7.45884503e-02   7.42025366e-17   4.58927764e-01   5.41556012e-15  -7.25045215e-01   7.04395046e-15  -8.92146837e-01  -8.39941456e-16   5.15019913e-16]
     [ -7.87827883e-17   1.66899763e-16   3.15134977e-17   2.82351090e-01  -2.07608673e-16   6.14132132e-01  -1.37417874e-15   1.43240922e-01  -5.75952414e-15   6.97957777e-01  -1.10206255e-15  -1.73449863e-16]
     [  3.38599636e-02   7.08226655e-03   8.12018394e-02  -1.33539218e-17  -2.75256643e-01   1.28549614e-15   2.43088515e-01   2.02747055e-15   1.41948897e+00   1.33137247e-14   1.62046309e+00   7.45186953e-01]]
    
    TOTAL NUCLEAR REPULSION ENERGY: 1.36687066232 a.u.
    TOTAL ENERGY: -2.92922773418 a.u.
    
    *********************************************************************************************************
    
    Time Taken: 10.986138812057659s

##Calculation of C<sub>2</sub>H<sub>4</sub> in 3-21G
With some tweaking the code is fast enough to calculate C<sup>2</sup>H<sup>4</sup>.

    Job type: Single point.
    Method: RHF
    Basis set: 3-21G(*)
    Number of shells: 14
    Number of basis functions: 26
    Multiplicity: 1
    
    SCF model:
     A restricted Hartree-Fock SCF calculation will be
     performed using Pulay DIIS + Geometric Direct Minimization
    
     SCF total energy:     -77.6009882 hartrees
    
      Reason for exit: Successful completion 
      Quantum Calculation CPU Time :          .30
      Quantum Calculation Wall Time:          .35
    
    SPARTAN '10 Semi-Empirical Program:  (WIN)               Release  5.0.0        
        Semi-empirical Property Calculation 
    
      M0001                                                                      
    
      Guess from Archive
        
      Energy Due to Solvation
       Solvation Energy                  8.942
      Memory Used:          73.48 Kb
       
    
      Reason for exit: Successful completion 
      Semi-Empirical Program CPU Time :          .06
      Semi-Empirical Program Wall Time:          .03
    
    SPARTAN STUDENT Properties Program:  (PC/x86)                  Release  5.0.0  
      Use of molecular symmetry enabled
    
                         Cartesian Coordinates (Angstroms)
           Atom            X             Y             Z     
        ---------    ------------- ------------- -------------
    
      1 H  H1           1.2248823    -0.9114147    -0.0000143
      2 C  C1           0.6574730     0.0000000     0.0000000
      3 H  H3           1.2248823     0.9114147     0.0000143
      4 C  C2          -0.6574730     0.0000000     0.0000000
      5 H  H2          -1.2248823    -0.9114147     0.0000143
      6 H  H4          -1.2248823     0.9114147    -0.0000143

Python Program,

    *********************************************************************************************************
    
    BEGIN SCF PROCEDURE
    SCF ENERGY: -98.13083597760205 a.u.
    SCF ENERGY: -103.10103791181984 a.u.
    SCF ENERGY: -108.57696254167776 a.u.
    SCF ENERGY: -110.64249187909161 a.u.
    SCF ENERGY: -110.9912179022255 a.u.
    SCF ENERGY: -111.03694043628029 a.u.
    SCF ENERGY: -111.04221107635888 a.u.
    SCF ENERGY: -111.04280455999499 a.u.
    SCF ENERGY: -111.04287091023491 a.u.
    SCF ENERGY: -111.04287832467162 a.u.
    SCF ENERGY: -111.04287915320292 a.u.
    SCF ENERGY: -111.04287924581624 a.u.
    SCF ENERGY: -111.04287925617108 a.u.
    SCF ENERGY: -111.04287925732933 a.u.
    SCF ENERGY: -111.04287925745884 a.u.
    
    ORBITAL ENERGY EIGENVALUES
    [[-11.17000222   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.         -11.16995794   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.          -1.03229544   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.          -0.78742061   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.          -0.64468601   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.          -0.58458886   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.          -0.50146589   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.          -0.37555661   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.18220965   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.29581505   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.31291926   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.34090057   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.43660802   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.53744771   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.87963818   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.92856354   0.           0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.9929878    0.           0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.07712723   0.           0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.1033016    0.           0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.12450178   0.           0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.31984817   0.           0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.35572466   0.           0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.39846053   0.           0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.64850096   0.           0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.66153763   0.        ]
     [  0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           0.           1.96473069]]
    
    ORBITAL COEFFICIENTS
    [[ -6.97614743e-01   6.97913107e-01   1.65848902e-01   1.28241887e-01   3.89787402e-16   8.46520544e-03  -1.73227387e-16   7.28270733e-17   3.01691838e-17   9.11127198e-02  -5.94826012e-14   1.21815014e-01  -5.43876819e-15   9.34837869e-02   1.66034000e-02   7.68318565e-17  -9.63346676e-16  -3.61635887e-15  -9.10910505e-02   3.68168086e-02  -6.18472768e-16   5.62882412e-16   2.53011297e-02   2.64267872e-14   3.36807762e-02  -2.67204025e-03]
     [ -6.53932718e-02   7.07880714e-02  -1.81582874e-01  -1.31871982e-01  -5.14129017e-16  -2.11211074e-02   3.85275740e-16  -2.46890959e-17   3.93709820e-17  -3.13841203e-02   1.99819759e-14  -4.65202889e-02   1.24708989e-14   4.11783572e-03   9.79460749e-02   2.04439665e-15  -8.20236818e-15  -1.17424475e-14   1.66584457e-03   3.61609066e-01  -2.84009209e-14  -1.85198084e-14  -1.22756959e-01  -9.18192088e-13  -1.20423641e+00  -1.41682885e+00]
     [  8.47264334e-16  -1.34012014e-15  -1.27486436e-15  -7.00383244e-16   2.78835850e-01  -5.49309149e-16  -2.60746057e-01   9.21327764e-15   1.17884946e-19  -3.26333920e-14  -2.17922383e-01  -1.40371621e-13   2.39466516e-01   1.49844204e-14  -1.77620120e-14   4.30107470e-01  -6.25840563e-14   3.38894965e-15   7.85876833e-15  -3.12753200e-15   8.22898443e-01  -6.87907813e-01  -9.48904999e-14   3.09284035e-01  -2.78282678e-13   2.94602733e-14]
     [ -1.57418704e-03  -1.87325426e-03   1.06722214e-01  -1.41579491e-01   1.29312689e-15   3.63485681e-01   9.89552145e-16   6.62230521e-16   7.99917278e-17  -1.29426033e-01   5.55776829e-14  -8.67398944e-02   2.06161816e-14   1.50787941e-01  -6.47940359e-01  -3.29200245e-14   6.76240078e-15  -8.43146779e-15  -5.78901177e-01  -2.12162392e-01  -5.92412394e-14   2.81189487e-14  -7.15313296e-01  -1.25382090e-13  -1.63368439e-01   8.72874133e-02]
     [ -2.59541571e-16  -2.78516918e-16  -5.27333796e-19  -2.50276292e-16   1.00307050e-16  -8.15904516e-16   1.40092637e-14   3.20168711e-01  -3.03705120e-01   3.29474513e-16  -6.48930330e-16   5.33909275e-16  -8.41064942e-16   1.03240232e-15  -6.42709424e-15  -9.96019962e-14  -7.64764267e-01   7.94991675e-01  -5.31990429e-15   1.45545194e-14  -6.67214109e-15   3.08673158e-15  -5.25347265e-15   9.73589174e-15  -3.97548983e-17   4.23943837e-15]
     [  3.13383008e-02  -6.62070284e-02  -3.70579272e-01  -4.19458456e-01   2.20988323e-15   2.45043498e-02  -3.04609067e-15  -2.31105514e-15  -3.49056835e-16  -1.37610823e+00   8.43910481e-13  -1.60732784e+00  -5.81944273e-14  -2.54852993e+00   4.21005199e-01   3.02606303e-14   1.32070938e-14   2.91767428e-14   3.03054109e-01  -4.42750494e-01  -1.14718162e-15   3.08066832e-14  -3.70953368e-01   1.21082813e-12   1.65398635e+00   3.83906898e+00]
     [  1.11842162e-15   4.94046729e-16   1.60405105e-15   5.21115548e-15   1.93638787e-01   1.08038112e-14  -2.75541690e-01   1.06259652e-14   1.35544276e-15   6.45986696e-14  -8.07360436e-01  -5.05543924e-13   1.64352357e+00   2.66951356e-14   1.09855438e-14  -7.07775279e-01   1.01946296e-13   1.23053930e-14  -1.04969669e-14  -1.21532876e-14  -1.84877050e+00   8.45050286e-01   1.83679124e-13  -2.49731090e+00   2.19645469e-12  -2.01014614e-13]
     [  4.25782833e-03   1.51947544e-02   1.65749600e-02  -6.26203724e-02  -9.62333719e-16   2.24595982e-01   7.39510235e-15   2.55801409e-15  -1.14269231e-15  -6.18188542e-01   2.61416333e-13  -2.91385316e-01   2.72848900e-13   2.55842418e+00   1.02589181e+00   2.35001003e-14  -1.15293035e-14   1.05506679e-14   4.92552256e-01  -4.90779423e-02   1.16518963e-13  -3.55449025e-14   1.31681217e+00   2.65117451e-13   3.35355262e-01  -1.15165930e+00]
     [ -7.11841215e-17  -1.84363408e-16   1.25947783e-16  -1.11458062e-16  -3.34874393e-16  -6.39045293e-16   1.56770860e-14   3.75405918e-01  -7.51466877e-01  -6.95549517e-16   1.86145982e-16   1.45942502e-15   4.59230113e-16  -2.13197822e-15   4.44042545e-15   7.51619753e-14   5.80139443e-01  -9.45568644e-01   8.72764297e-15  -2.12023005e-14   8.29224281e-15  -1.04540242e-15   3.98437029e-15  -1.53812949e-14   1.08666701e-15  -4.90832680e-15]
     [ -6.97612207e-01  -6.97915643e-01   1.65848902e-01  -1.28241887e-01   3.32195463e-16   8.46520542e-03   3.88594431e-16  -1.03826900e-16  -1.13769143e-16   9.11127198e-02   8.13735581e-15  -1.21815014e-01  -4.49736969e-16  -9.34837869e-02   1.66034001e-02   1.46260429e-15   1.60058991e-17   9.01946841e-16   9.10910505e-02   3.68168086e-02  -2.63382012e-16   1.97317149e-15  -2.53011297e-02   2.94460080e-14   3.36807762e-02   2.67204024e-03]
     [ -6.53930146e-02  -7.07883091e-02  -1.81582874e-01   1.31871982e-01   2.63827311e-15  -2.11211074e-02  -6.60339772e-16  -7.78640816e-17  -1.59761138e-16  -3.13841203e-02   1.34247670e-14   4.65202889e-02  -6.73283516e-15  -4.11783574e-03   9.79460749e-02   1.31291895e-14  -1.01295784e-15  -1.23376206e-14  -1.66584454e-03   3.61609066e-01  -2.30264089e-14  -4.76550084e-14   1.22756959e-01  -1.01259495e-12  -1.20423641e+00   1.41682885e+00]
     [ -1.25726109e-15   5.16389540e-16  -2.33369335e-16   8.53828992e-16   2.78835850e-01  -6.94911720e-16   2.60746057e-01  -9.63908085e-15   2.89037485e-16  -5.84930683e-14  -2.17922383e-01  -1.44204936e-13  -2.39466516e-01   2.65050360e-15  -3.25909457e-14   4.30107470e-01  -6.40763886e-14  -6.12011133e-15  -6.68653497e-15  -3.07096595e-14  -8.22898442e-01  -6.87907814e-01  -6.89360953e-14  -3.09284035e-01   3.10686155e-13  -4.96508386e-14]
     [  1.57419385e-03  -1.87324854e-03  -1.06722214e-01  -1.41579490e-01  -1.37739884e-15  -3.63485681e-01  -9.52659848e-16  -9.87506698e-16  -3.15801030e-16   1.29426033e-01  -1.01290680e-14  -8.67398944e-02   1.35872603e-14   1.50787941e-01   6.47940359e-01   1.30810712e-14  -8.75344201e-15  -2.21414568e-14  -5.78901177e-01   2.12162392e-01  -6.79789156e-14   4.13432424e-14  -7.15313296e-01   1.31988631e-13   1.63368439e-01   8.72874132e-02]
     [  3.10265973e-16   2.93132431e-16  -2.41219673e-16   1.12915147e-16   1.25110353e-15  -8.61469783e-16   1.39301044e-14   3.20168711e-01   3.03705120e-01   4.36059374e-17  -3.54754834e-17  -8.45956379e-16   1.14520202e-15  -6.51463676e-16  -6.04719405e-15  -1.01872989e-13  -7.64764267e-01  -7.94991675e-01   1.29108735e-14  -3.07352210e-14   7.88950811e-15   6.56125403e-15   1.80469237e-15  -8.57965930e-15   7.64485039e-16   3.65648874e-15]
     [  3.13380602e-02   6.62071423e-02  -3.70579272e-01   4.19458456e-01  -1.00049533e-14   2.45043498e-02   6.83701457e-16   2.55507586e-15   1.65223068e-15  -1.37610823e+00  -8.70459346e-14   1.60732784e+00   1.46385687e-13   2.54852993e+00   4.21005199e-01  -8.09511772e-15  -1.23947888e-14   5.13529043e-15  -3.03054109e-01  -4.42750494e-01   7.08387436e-14   5.52039381e-14   3.70953368e-01   1.41080340e-12   1.65398634e+00  -3.83906898e+00]
     [ -3.94024312e-16  -3.51950167e-16  -5.00283318e-16  -5.45592207e-15   1.93638787e-01  -1.55911112e-14   2.75541690e-01  -1.09064217e-14   8.21488873e-16  -4.54188948e-13  -8.07360436e-01  -4.21719490e-13  -1.64352357e+00  -2.71424204e-14   7.76699183e-14  -7.07775279e-01   1.07673009e-13  -9.74297268e-15   2.17445806e-14   4.96977394e-14   1.84877050e+00   8.45050289e-01   3.34372860e-14   2.49731090e+00  -2.24023049e-12   2.34389373e-13]
     [ -4.25788356e-03   1.51947389e-02  -1.65749600e-02  -6.26203723e-02  -5.83911363e-16  -2.24595982e-01   7.57048246e-15   1.92778317e-15  -1.58702664e-15   6.18188542e-01  -8.93378214e-14  -2.91385317e-01   2.30325070e-13   2.55842418e+00  -1.02589181e+00  -4.34397802e-14   6.09330520e-15   4.94759108e-15   4.92552256e-01   4.90779425e-02   1.11256710e-13  -5.73510986e-14   1.31681217e+00  -2.48330074e-13  -3.35355262e-01  -1.15165930e+00]
     [ -1.02045787e-16  -1.64072928e-16  -3.32020522e-16  -1.33893725e-16   8.30742211e-16  -1.12213586e-15   1.62613672e-14   3.75405918e-01   7.51466877e-01   6.91408174e-16   6.55113765e-16  -1.31843546e-15   5.68285799e-16   2.27949003e-15   4.55878897e-15   7.76539072e-14   5.80139442e-01   9.45568644e-01  -1.40498032e-14   3.34485068e-14  -8.97168417e-15  -6.29334747e-15  -9.91885154e-16   1.48040615e-14  -1.38585881e-15  -1.54494397e-15]
     [  1.76882291e-03  -2.66730040e-04  -7.81813183e-02  -1.37580403e-01   1.46846533e-01   1.18481388e-01  -1.78672284e-01   6.61465882e-15  -7.57393295e-16   1.79895092e-02   5.06374568e-02   2.45267668e-02   3.95339135e-02  -7.04630289e-02  -1.41345381e-01   4.40818201e-01  -6.75068141e-14  -3.52872780e-14  -4.58003445e-01   6.01195088e-01  -2.88625322e-01   4.78288172e-01   4.75066734e-01   6.93358294e-01   2.02311598e-01  -1.12396387e-01]
     [ -9.59019683e-03   7.99870493e-03  -5.26029709e-03  -6.74748316e-02   1.08962883e-01   1.11147549e-01  -1.55729759e-01   5.00306917e-15  -3.99683122e-16   9.51383057e-01   1.00253175e+00   9.91805058e-01  -1.39107686e+00  -4.14223137e-01  -1.19352039e-01  -2.06713664e-02   1.67338143e-15   5.41717797e-15   9.71601377e-02  -2.36546055e-01   1.07213253e+00  -8.85468497e-01  -7.59270208e-01   6.03147157e-01  -6.67925679e-01  -3.58852134e-01]
     [  1.76882291e-03  -2.66730040e-04  -7.81813183e-02  -1.37580403e-01  -1.46846533e-01   1.18481388e-01   1.78672284e-01  -6.07074083e-15   3.91995921e-16   1.79895092e-02  -5.06374568e-02   2.45267668e-02  -3.95339135e-02  -7.04630289e-02  -1.41345381e-01  -4.40818201e-01   5.23901911e-14  -2.03088636e-14  -4.58003445e-01   6.01195088e-01   2.88625322e-01  -4.78288172e-01   4.75066734e-01  -6.93358294e-01   2.02311598e-01  -1.12396387e-01]
     [ -9.59019683e-03   7.99870493e-03  -5.26029709e-03  -6.74748316e-02  -1.08962883e-01   1.11147549e-01   1.55729759e-01  -5.55223934e-15   2.52273341e-15   9.51383057e-01  -1.00253175e+00   9.91805058e-01   1.39107686e+00  -4.14223137e-01  -1.19352039e-01   2.06713664e-02   5.65615812e-15   8.49381171e-15   9.71601377e-02  -2.36546055e-01  -1.07213253e+00   8.85468497e-01  -7.59270208e-01  -6.03147157e-01  -6.67925679e-01  -3.58852134e-01]
     [  1.76882194e-03   2.66736468e-04  -7.81813183e-02   1.37580403e-01   1.46846533e-01   1.18481388e-01   1.78672284e-01  -6.50174616e-15   6.90409269e-17   1.79895091e-02   5.06374568e-02  -2.45267668e-02  -3.95339135e-02   7.04630288e-02  -1.41345381e-01   4.40818201e-01  -6.11887041e-14  -2.38479630e-15   4.58003445e-01   6.01195088e-01   2.88625321e-01   4.78288172e-01  -4.75066734e-01  -6.93358294e-01   2.02311598e-01   1.12396387e-01]
     [ -9.59016776e-03  -7.99873978e-03  -5.26029709e-03   6.74748316e-02   1.08962883e-01   1.11147549e-01   1.55729760e-01  -5.82636833e-15  -3.77405080e-15   9.51383056e-01   1.00253175e+00  -9.91805058e-01   1.39107686e+00   4.14223137e-01  -1.19352038e-01  -2.06713665e-02  -9.27714155e-16   5.02888238e-15  -9.71601378e-02  -2.36546055e-01  -1.07213253e+00  -8.85468499e-01   7.59270208e-01  -6.03147157e-01  -6.67925679e-01   3.58852134e-01]
     [  1.76882194e-03   2.66736468e-04  -7.81813183e-02   1.37580403e-01  -1.46846533e-01   1.18481388e-01  -1.78672284e-01   7.06802824e-15  -4.52888059e-17   1.79895091e-02  -5.06374568e-02  -2.45267668e-02   3.95339135e-02   7.04630288e-02  -1.41345381e-01  -4.40818201e-01   5.84736871e-14  -1.97203530e-14   4.58003445e-01   6.01195088e-01  -2.88625321e-01  -4.78288172e-01  -4.75066734e-01   6.93358294e-01   2.02311598e-01   1.12396387e-01]
     [ -9.59016776e-03  -7.99873978e-03  -5.26029709e-03   6.74748316e-02  -1.08962883e-01   1.11147549e-01  -1.55729760e-01   6.49771022e-15   2.85881514e-16   9.51383056e-01  -1.00253175e+00  -9.91805058e-01  -1.39107686e+00   4.14223137e-01  -1.19352038e-01   2.06713665e-02   7.63951320e-15   5.05872917e-15  -9.71601378e-02  -2.36546055e-01   1.07213253e+00   8.85468499e-01   7.59270208e-01   6.03147157e-01  -6.67925679e-01   3.58852134e-01]]
    
    TOTAL NUCLEAR REPULSION ENERGY: 33.4424184132 a.u.
    TOTAL ENERGY: -77.6004608443 a.u.
    
    *********************************************************************************************************
    
    Time Taken: 72.70841306778921s