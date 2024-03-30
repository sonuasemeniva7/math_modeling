#марс1 вен2 сатурн3 юпт4 

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
sec_y=365*24*60*60
sec_d=24*60*60
years=10
t=np.arange(0,years*sec_y,sec_d*10)

m_p = 1.67262192* 10 ** (-27) 
q_p= 1.6022 * 10 ** (-19) 
m_n = 1.6749274980495 * 10 ** (-24)
                               
q_core=4*q_p 
q_e=-1.60217663 * 10**(-19)

mass_core = m_p * 4 + m_e * 5
m_p = 1,6022 * 10 ** (−19) 
m_n = 1.6749274980495 * 10 ** (−24)
                               
q_=4*q_p 
q_e= ///

def grav_func(z,t):
     (x_1, v_x_1, y_1, v_y_1,
      x_2, v_x_2, y_2, v_y_2,
      x_3, v_x_3, y_3, v_y_3,
      x_4, v_x_4, y_4, v_y_4)= z
     
     dxdt_1= v_x_1
     dv_xdt_1= -G*mass_core* x_1/(x_1**2+y_1**2)**1.5 
     + k * (q_e**2) / m_e * (x1 - x2) 
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
     + k * (q_e**2) / m_e * (x1 - x3) 
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
     + k * (q_e**2) / m_e * (x1 - x4) 
               / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
     + k * q_e * q_p / m_e * (x1 - x2) 
               / ((x1 - xp)**2 + (y1 - yp)**2)**1.5
     dydt_mars= v_y_1
     dv_ydt_mars= -G * mass_core * y_1/(x_1**2+y_1**2)**1.5

     dv_ydt_1= -G * mass_core * x_1/(x_1**2+y_1**2)**1.5 
     + k * (q_e**2) / m_e * (y1 - y2) 
               / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5
     + k * (q_e**2) / m_e * (y1 - y3) 
               / ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 1.5
     + k * (q_e ** 2) / m_e * (y1 - y4) 
               / ((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 1.5
     + k * q_e * q_p / m_e * (y1 - y2) 
               / ((x1 - xp) ** 2 + (y1 - yp) ** 2) ** 1.5
     dydt_1= v_y_1
     dv_ydt_1= -G* mass_core * y_1/(x_1**2+y_1**2)**1.5
     
     dxdt_2= v_x_ven
     dv_xdt_2= -G*mass_core* x_ven/(x_2 **2+y_v2**2)**1.5
     dydt_2= v_y_ven
     dv_ydt_2= -G* mass_core* y_ven/(x_v2**2+y_2**2)**1.5
     
     dxdt_3= v_x_saturn
     dv_xdt_3= -G* mass_core* x_saturn/(x_3**2+y_3**2)**1.5
     dydt_3= v_y_saturn
     dv_ydt_3= -G* mass_core * y_saturn/(x_3**2+y_3**2)**1.5
     
     dxdt_4= v_x_4
     dv_xdt_4= -G* mass_core* x_yup/(x_4**2+y_4p**2)**1.5
     dydt_4= v_y_4
     dv_ydt_4= -G* mass_core * y_yup/(x_4**2+y_4**2)**1.5
     
     return(dxdt_1, dv_xdt_1, dydt_1, dv_ydt_1, dxdt_2, dv_xdt_2, dydt_2, 
            dv_ydt_2,dxdt_3,dv_xdt_3, dydt_3, dv_ydt_3,
            dxdt_4,dv_xdt_4,dydt_4, dv_ydt_4)

	
q1 = - 1.1 * 10**(20)

q2 = 2.1 * 10**(20)

x0_1= 0
v_x0_1=24100
y0_1=-228*10**9
v_y0_1=0

x0_2 =-108*10**9
v_x0_2 =0
y0_2 =0
v_y0_2 =-35000

x0_3=0
v_x0_3=-9690
y0_3=1430*10**9
v_y0_3=0

x0_4=0
v_x0_4=-13070
y0_4=778.57*10**9
v_y0_4=0


z0=(x0_1, v_x0_1,y0_1, v_y0_1, 
    x0_2, v_x0_2, y0_2,v_y0_2,
    x0_3, v_x0_3,y0_3,v_y0_3,
    x0_4, v_x0_4, y0_4, v_y0_4)

G=6.67*10**(-11)
k = 8.98755 * 10**9

sol = odeint(grav_func, z0, t)

fig=plt.figure()
planets=[]

for i in range(0, len(t), 1):
    p_1, =plt.plot([0], [1], 'yo', ms=10)
    n_1, =plt.plot([0], [2], 'yo', ms=10)
    sun, =plt.plot([0], [3], 'yo', ms=10)
    
    e_1, = plt.plot(sol[:i,0], sol[:i, 2], '-', color='orangered')
    e1_line, = plt.plot(sol[i,0], sol[i, 2], 'o', color='orangered')
    
    e_2,= plt.plot(sol[:i,4], sol[:i, 6], '-', color= 'maroon' )
    e2_line, = plt.plot(sol[i,4], sol[i, 6],'o', color= 'maroon')
    
    e_3,= plt.plot(sol[:i,8], sol[:i, 10],  '-', color= 'wheat')
    e3_line, = plt.plot(sol[i,8], sol[i, 10], 'o', color='wheat')
    
    e_4,= plt.plot(sol[:i,12], sol[:i, 14], '-', color='burlywood')
    e4_line, = plt.plot(sol[i,12], sol[i, 14], 'o', color='burlywood')
    
    
    
    planets.append([sun, e_1, e1_line, 
                    e_2, e2_line,
                    e_3,e3_line, 
                    e_4, e4_line])
ani = ArtistAnimation(fig, planets, interval= 50)
plt.axis('equal')
ani.save('solarsys.gif')

