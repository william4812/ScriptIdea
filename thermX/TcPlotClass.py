import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

class TcPlotClass():
    #def __init__
    
    def genTable(self):
        labels = np.linspace(1,25,25)
        
        tableCol = [['TC Wafer', 'SP']]
        for i, label in enumerate(labels):
            tmp = 'TC' + str(int(label)) + ' ($^\circ$C)'
            

        
        # average marks data for 5 consecutive years 
        dataRaw = [[380.46, 379.39, 382.02, 380.67, 379.53,
                383.30, 382.54, 381.63, 380.06, 378.75,
                381.26, 378.56, 377.14, 379.11, 381.15,
                378.21, 380.44, 381.72, 381.83, 380.32, 
                380.53, 377.57, 380.48, 376.55, 377.99]]
        
        Tavg = sum(dataRaw[0])/len(dataRaw[0])
        Tmax = max(dataRaw[0])
        Tmin = min(dataRaw[0])
        print(Tavg, Tmax, Tmin)
        dataRaw[0].append(Tmin)
        dataRaw[0].append(Tmax)
        dataRaw[0].append(Tavg)

        data = np.array(dataRaw).T
        print(data, '\n', dataRaw)
        

        # average marks data for 5 consecutive years 
        '''
        data = [[98, 95,  93, 96,  97], 
                [97, 92,  95, 94,  96], 
                [98, 95,  93, 95,  94], 
                [96, 94,  94, 92,  95], 
                [95, 90,  91, 94,  98]] 
        '''

        columns = ('SP1', 'SP2') 
        rows = ['TC %d' % x for x in range(1,26)] 
        rows.append('Tmin')
        rows.append('Tmax')
        rows.append('Tavg')
        
        # Get some pastel shades for the colors 
        colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows))) 
        n_rows = len(data) 
        
        index = np.arange(len(columns)) + 0.3
        bar_width = 0.4
        
        # Initialize the vertical-offset for 
        # the line plots. 
        y_offset = np.zeros(len(columns)) 
        
        # Plot line plots and create text labels  
        # for the table 
        cell_text = [] 
        for row in range(n_rows): 
                #plt.plot(index, data[row], color=colors[row]) 
                y_offset = data[row] 
                cell_text.append([x for x in y_offset]) 
        
        # Reverse colors and text labels to display 
        # the last value at the top. 
        #colors = colors[::-1] 
        #cell_text.reverse() 
        
        # Add a table at the bottom of the axes 
        the_table = plt.table(cellText=cell_text, 
                        rowLabels=rows, 
                        rowColours=colors, 
                        colLabels=columns, 
                        loc='right') 
        
        # Adjust layout to make room for the table: 
        plt.subplots_adjust(left=0.08, 
                            bottom=0.09,
                            right=0.53,
                            top = 0.88) 
                           
        
        #plt.ylabel("marks".format(value_increment)) 
        #plt.xticks([]) 
        #plt.title('average marks in each consecutive year') 
        #plt.tight_layout()
        plt.show() 
                
    def temp2Dmap(self, tcLocDic, tcAvgList):
        print(tcLocDic)
        print(tcAvgList)

        fig, ax = plt.subplots()
        center = (0, 0)     # set center to be origin
        radius = 150        # set radius as 150 mm
        
        # create circle object with grey color
        circle = plt.Circle(xy = center, 
                            radius = radius, 
                            color='grey',
                            alpha=0.9)
        
        ax.add_patch(circle) # add circle object to plot

        # set aspect ratio of the plot to be equalpip 
        # install tkinterpip install tkinter
        ax.set_aspect("equal")

        # set limits slightly higher than radius and offset by center coordinates
        plt.xlim([-radius - radius/5 + center[0], 
                radius + radius/5 + center[0]])
        plt.ylim([-radius - radius/5 + center[1], 
                radius + radius/5 + center[1]])

        # TC coordnates
        x_coords=[]
        z_coords=[]
        for key, value in tcLocDic.items():
            if key in range(1,26):
                x_coords.append(value[0])
                z_coords.append(value[1])        

        Ttmp = tcAvgList

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
        #plt.imshow(Ttmp, cmap='hot', interpolation='nearest')
        plt.tight_layout()
        plt.show(block=False)

    def temp2Dmap2(self):
        fig, ax = plt.subplots()
        
        # set center to be origin
        center = (0, 0) 

        # set radius as 1
        radius = 150

        # create circle object with grey color
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
        #plt.imshow(Ttmp, cmap='hot', interpolation='nearest')
        plt.tight_layout()
        plt.show(block=False)

'''
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
#from scipy.interpolate import griddata

# Generate sample data
max_r = 1  # Maximum radius
max_theta = 2.0 * np.pi  # Full circle
num_points = 500  # Number of sample points

# Create random points within the circle
points = np.random.rand(num_points, 2) * [max_r, max_theta]

# Assign temperature values to the points (modify as needed)
values = points[:, 0] * np.sin(points[:, 1]) * np.cos(points[:, 1])

# Create grids for interpolation
theta = np.linspace(0.0, max_theta, 200)
r = np.linspace(0, max_r, 100)
grid_r, grid_theta = np.meshgrid(r, theta)

# Interpolate data onto the grid
data = griddata(points, values, (grid_r, grid_theta), method='cubic', fill_value=0)

# Create polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Plot the heatmap
cax = ax.pcolormesh(theta, r, data.T, cmap='coolwarm')  # Adjust colormap as desired

# Add colorbar
fig.colorbar(cax, ax=ax, label='Temperature')

# Set labels and title
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_title('Temperature Map on a Circular Shape')

plt.show()
'''


def main():
    pltObj = TcPlotClass()
    pltObj.genTable()
    #pltObj.temp2Dmap()

    #print(f"{os.environ['home']}")

    ## run other commands on the system
    #program = "python"
    #arguments = ["hello.py"]
    #print(os.execvp(program, (program,) +  tuple(arguments)))
    
    

    #currentFiles = os.system("'test' > users.txt")

if __name__ == "__main__":
    main()