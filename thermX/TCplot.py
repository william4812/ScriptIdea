import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# set center to be origin
center = (0, 0) 

# set radius as 1
radius = 150

# create circle object with red color
circle = plt.Circle(xy = center, 
                    radius = radius, 
                    color='grey',
                    alpha=0.9)

# add circle object to plot
ax.add_patch(circle)

# set aspect ratio of the plot to be equalpip install tkinterpip install tkinter
ax.set_aspect("equal")

# set limits slightly higher than radius and offset by center coordinates
plt.xlim([-radius - radius/5 + center[0], 
           radius + radius/5 + center[0]])
plt.ylim([-radius - radius/5 + center[1], 
           radius + radius/5 + center[1]])

# TC coordnates
x_coords = [-140, -104.3, -104.3,   -90, -81.3,
           -81.3,    -40,    -40,   -30,     0,
               0,      0,      0,     0,     0,
               0,     30,     40,    40,  81.3,
            81.3,     90,  104.3, 104.3,   140]
z_coords = [   0, -104.3,  104.3,     0, -81.3,
            81.3,    -40,     40,     0,  -140,
             -90,    -30,      0,    30,    90,
             140,      0,    -40,    40, -81.3,
            81.3,      0, -104.3, 104.3,     0]
'''
#3 zone with embedded data new lift pin_surface fitting_case power.mph
T_sim = [379.3796457, 378.958463,  378.8708679, 380.9947258, 380.8022983,
         380.7004107, 380.9762826, 380.9732125, 379.3632171, 379.5360298,
         381.1546752, 379.5111195, 378.798137,  379.4965356, 381.1836409,
         379.3807668, 379.6488067, 381.2287609,	381.130725,  381.0081608, 
         380.8912831, 381.3092924, 379.1567859,	379.0491118, 379.7592945]
'''
'''
#3 zone with embedded data new lift pin_surface fitting_case emissivity.mph
T_sim = [380.0905401, 379.9188281, 379.8343934,	379.5487714, 379.7384971,
         379.6402057, 380.6953779, 380.7036429, 379.5437241, 380.2822075,
         379.7506895, 379.7419264, 379.2088574, 379.7284933, 379.8015012,
         380.1539047, 379.9232591, 381.0184389,	380.9073049, 380.0385686,
         379.8870027, 379.9586473, 380.1791314,	380.0588152, 380.613764
]
'''

#3 zone with embedded data new lift pin_surface fitting_case emissivity_vs_power.mph
T_sim = [380.257468, 380.0271236, 379.9354136, 379.9331481, 380.2017722,	
         380.0937186, 380.6743508, 380.6765641, 379.3127225, 380.445136,	
         380.1283373, 379.5084579, 378.9120356, 379.4935427, 380.1811207,	
         380.3039797, 379.6876713, 380.9928172, 380.8788075, 380.4889559,	
         380.3378671, 380.3382463, 380.2809258,	380.1579979, 380.7729868
]

Ttmp = T_sim
'''         
T_exp = [380.46, 379.39, 382.02, 380.67, 379.53,
         383.30, 382.54, 381.63, 380.06, 378.75,
         381.26, 378.56, 377.14, 379.11, 381.15,
         378.21, 380.44, 381.72, 381.83, 380.32, 
         380.53, 377.57, 380.48, 376.55, 377.99]
Ttmp = T_exp
'''
labels = np.linspace(1,len(x_coords),len(x_coords))
plt.scatter(x_coords, z_coords, s=100, c='red', marker='x')

for i, label in enumerate(labels):
    tmp = 'TC' + str(int(label)) + ',\n ' + str(round(Ttmp[i],2)) + '$^\circ$C'
    plt.annotate(tmp, (x_coords[i], z_coords[i]), 
                 xytext=(5, -5), textcoords='offset points')

# label x and y axes
plt.xlabel("X (mm)")
plt.ylabel("Z (mm)")

# set title
plt.title('TC map')

plt.show()