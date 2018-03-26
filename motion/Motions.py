import ir2_base as ir
import time

def Archit_motion():
  ir.initall()
  #move neck from 90 to 135
  ir.nk(100)
  ir.nk(135)
  ir.rsu(120)
  ir.reu(90)
  ir.lsu(80)
  ir.lss(120)
  ir.leu(135)

  for x in range(0, 3):  
    ir.hd(40)
    #time.sleep(1)
    ir.hd(150)
    
  ir.initall()
    
def Mohak_motion():
  ir.initall()
  
  ir.rsu(150) #up
  ir.lsu(30) #up
  ir.rss(45)
  ir.lss(120)

  for x in range(0, 3):
    ir.reu(90) #inward
    ir.leu(110)
    #ir.rer(45)
    #ir.ler(90)
    time.sleep(0.3)
    ir.reu(135) #outward
    ir.leu(80)
    #ir.rer(90)
    #ir.ler(45)
    
  #ir.initall()
    
def shashwat_motion():
  ir.initall()
  
  for x in range(0,3):
    ir.rsu(135) #down
    ir.lsu(125) #up
    ir.leu(90) #inward
    time.sleep(0.5)
    ir.leu(90) #outward
    
    ir.leu(180) #reset
    ir.lsu(45) #down
    ir.rsu(65) #up
    ir.reu(125) #inward
    time.sleep(0.5)
    ir.reu(135) #outward
    
    ir.reu(180)
  #ir.initall()
    
def sandeep_motion():
  ir.initall()
   
  ir.lsu(60) #down
  ir.rsu(10) #up
  ir.lss(120)
  ir.leu(120) #inward
  time.sleep(1)
  ir.leu(90)
  ir.lsu(150) #down
  #ir.initall()
  
  
def surya_motion():
  ir.initall()
  
  for x in range(0,3):
    ir.lsu(60) #inward
    ir.rsu(120) #inward
    ir.hd(120) 
    ir.lss(120) #inward
    ir.rss(45) #inward
  
    ir.reu(90)
    ir.leu(90)
    time.sleep(0.2)
  
    ir.hd(60) #down
    ir.reu(135)
    ir.leu(115)
  ir.lsu(170) #inward
  ir.rsu(20) #inward
  #ir.initall()
    

def unknown_motion():
  ir.initall()
  
  ir.rsu(135) #down
  ir.lsu(45) #down
  
  ir.rer(135) #inward
  ir.ler(45) #inward
  
  for x in range(0,4):
    ir.nk(135)
    ir.nk(45)
  ir.lsu(170) #inward
  ir.rsu(20) #inward
  ir.nk(90) #down
  #ir.initall()

  
  
