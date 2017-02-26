# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 21:48:33 2017

@author: Elise
"""
import adsk.core, adsk.fusion, traceback
from simpy import *
from numpy import *

def ask_user():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
    

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        ent = ui.selectEntity("Select a circular edge", "CircularEdges")
        
        if (isinstance(ent.entity.geometry, adsk.core.Arc3D)): 
            arcGeom = ent.entity.geometry
            
            arcInfo = getArcGeometryInfo(arcGeom)
                            
            ui.messageBox(arcInfo, "Arc Info")
        else:  
            if (isinstance(ent.entity.geometry, adsk.core.Circle3D)):
                circGeom = ent.entity.geometry
                
                circleInfo = getCircleGeometryInfo(circGeom)
                
                ui.messageBox( circleInfo, "Radius")
                
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def Fluid_mu(material):
    """
    The "Fluid_mu" function takes in the 
    name of fluid material as its input 
    from the user. It returns the value 
    of a material property called the 
    dynamic viscosity of the fluid
    """
    if material == "Oil":
        mu=5
    if material == "Mercury":
        mu=6
    if material == "Air":
        mu=1
    if material == "Water":
        mu=4
    else:
        mu=0
    return mu

def area(circleInfo):
    """
    The "area" function takes in a radius 
    from the Fusion 360 API and uses it to 
    calculate the area of the face perpendicular 
    to flow." 
    """        
    return (circleInfo**2)*(3.14)


def derive(velocity, circleInfo):
    """
    The "derive" function takes in a radius 
    from the Fusion 360 API and a flow 
    velocity from the user and uses it 
    to create a function for the velocity 
    profile of a fluid in a circular pipe.  
    """
    if propertyValue == arc2D_var.isValid:    
        propertyValue = arc2D_var.radius    
    else: 
        raise ValueError("The property value you have tried to refrence is" 
        "invalid. It may have been deleted or some other action has been done" 
        "to invalidate the refrence.")
        
    y = Symbol("y")
    u = velocity*(1-((y**2)/(propertyValue**2)))
    derivative == u.diff(y)
    return derivative    

def Shear_Force(velocity, material, circleInfo):    
    """
    The "Shear_Force" function takes in a velocity and material from the user and uses these along with 
    """    
    velocity = ask_user()[0]
    material = ask_user()[1]     
    ShearForce = derive(velocity, propertyValue)*area(propertyValue)*Fluid_mu(material)
    print(ShearForce)
